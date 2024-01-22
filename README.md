# OpenDroneIdLogReader

Simple and rudimentary ( for now ) , script in python that takes as input a .csv log file generated by the OpenDroneId application : 
https://github.com/opendroneid/receiver-android

The script via folium library , draws the path of the UAV on an interactive satellite map generated as an html file ( for illustration purpose I used the one from Google ) , 
on the map there are also markers that can contain various information about the drone acquired at that precise moment , the number of markers you can decide via argument ( the more markers there are the heavier the html file will be ) .

In addition to the interactive map , the script will print the average of some data such as : height,speed,horizontal/vertical accuracy/speed,rssi,distance from uav
It will also print out how many transport packets were found , BT5 , BT4 or Beacon
And also a graph via plotly , of height , speed , status of the uav

Since I have not tested whether the log is able to acquire data from several uavs at the same time , I have included the possibility to filter the data by drone ID as an argument , you will have to enter that as a  simple string .

Comands :

python parse_rid_file.py [file.csv] [ID_UAV] [NUMBER_OF_MARKER]

Working in progress...
