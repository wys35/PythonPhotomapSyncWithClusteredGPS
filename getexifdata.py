from GPSPhoto import gpsphoto
import os
import sys

pics = sorted(os.listdir("img/" + sys.argv[1]))
pics = (p for p in pics if p.endswith(".JPG") or p.endswith(".jpg") or p.endswith(".JPEG") or p.endswith(".jpeg"))

csv = open("data.csv", "w") 
csv.write("filename,lat,lon,label,locname\n")

curlat = 0
curlon = 0

for pic in pics:
    try:
        gpsvalue = gpsphoto.getGPSData("img/" + sys.argv[1] + "/" + pic)
        lat = gpsvalue['Latitude']
        lon = gpsvalue['Longitude']
        if lat is None and lon is None:
            lat = curlat
            lon = curlon
        else:
            curlat = lat
            curlon = lon
        row = pic + ",%s,%s,,\n" % (lat, lon)
        print(pic, lat, lon)
        csv.write(row)
    except Exception as e:
        print(e)
