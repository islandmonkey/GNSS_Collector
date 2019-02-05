from ftplib import *
import datetime, calendar
import os, sys

def print_error():
    print("Error: Wrong or no arguments passed")
    print("Try: StationFetcher.exe <station abbreviation> <ddmmYYYY>")
    print("Example: StationFetcher.exe mbar 15072018")

if (len(sys.argv) != 3):
    print_error()
    sys.exit(2)

station = sys.argv[1]
date = sys.argv[2]

def toGPS(utc):
    """ Returns the GPS week, GPS day of Year, the GPS day of Week """
    datetimeformat = "%Y-%m-%d"
    epoch = datetime.datetime.strptime("1980-01-06",datetimeformat)
    tdiff = utc -epoch
    gpsweek = tdiff.days // 7 
    gpsdays = tdiff.days - 7*gpsweek   
    new_year_day = datetime.datetime(year=utc.year, month=1, day=1)  
    return gpsweek,(utc - new_year_day).days + 1,gpsdays

def getfile(fname):
    with open(fname, 'wb') as f:
        ftp.retrbinary('RETR ' + fname, f.write)

try:
    gps_dates = toGPS(datetime.datetime.strptime(date,"%d%m%Y"))
    print(gps_dates)
except:
    print("ERROR: Unable to parse entered date. Wrong format?")

base_url = "cddis.nasa.gov"
daily_url = "gnss/data/daily/" + date[-4:] + "/" + str(gps_dates[1]) + "/" 
products_url = "/gnss/products/" + str(gps_dates[0]) + "/"

obs_url = date[-2:] + "o/"
nav_gps_url = date[-2:] + "n/"
nav_glo_url = date[-2:] + "g/"

obs_fname = station + str(gps_dates[1]) + "0." + date[-2:] + "o.Z"
nav_gps_fname = station + str(gps_dates[1]) + "0." + date[-2:] + "n.Z"
nav_glo_fname = station + str(gps_dates[1]) + "0." + date[-2:] + "g.Z"

clk_fname = "igs" + str(gps_dates[0]) + str(gps_dates[2]) + ".clk.Z"
sp3_fname = "igs" + str(gps_dates[0]) + str(gps_dates[2]) + ".sp3.Z"

print("Connecting to: {}".format(base_url))
ftp = FTP(base_url)
print(ftp.login())

print("Downloading o/n/g files...")
try:
    ftp.cwd(daily_url)
    ftp.cwd(obs_url)
    getfile(obs_fname)
    ftp.cwd("../" + nav_gps_url)
    getfile(nav_gps_fname)
    ftp.cwd("../" + nav_glo_url)
    getfile(nav_glo_fname)
except:
    print("Couldn't download o/n/g files")
    
print("Downloading clk/sp3 files...")
try:
    ftp.cwd("../../../../../../")
    ftp.cwd(products_url)
    getfile(clk_fname)
    getfile(sp3_fname)
except:
    print("Couldn't download clk/sp3 files")

print("DONE")