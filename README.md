# GNSS-Collector
A small programm to gather daily data from GNSS stations for PPK from the IGS Network

#### A list and map of all sites can be found [here](http://www.igs.org/network).

### Usage (executable):
From a terminal run ``` GNSS_Collector.exe <station> <date> ```

```<station>``` the first 3 or 4 (depending on the station) letters before the first numbers of the site name ([http://www.igs.org/network](http://www.igs.org/network)). Lowercase!

```<date>``` in the format of ddmmYYYY

#### Example: 
Site name : MCM400ATA

Date : 25/07/2018

``` GNSS_Collector.exe mcm 25072018 ```

The files will be downloaded into the same directory as the executable.
