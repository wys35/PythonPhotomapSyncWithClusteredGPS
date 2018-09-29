from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import os
import sys

def _get_if_exist(data, key):
    if key in data:
        return data[key]
 
    return None

def get_exif_data(fn):
    image = Image.open(fn)

    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for t in value:
                    sub_decoded = GPSTAGS.get(t, t)
                    gps_data[sub_decoded] = value[t]

                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value
    return exif_data

def _convert_to_degrees(value):
    """Helper function to convert the GPS coordinates stored in the EXIF to degrees in float format"""
    d0 = value[0][0]
    d1 = value[0][1]
    d = float(d0) / float(d1)
 
    m0 = value[1][0]
    m1 = value[1][1]
    m = float(m0) / float(m1)
 
    s0 = value[2][0]
    s1 = value[2][1]
    s = float(s0) / float(s1)
 
    return d + (m / 60.0) + (s / 3600.0)

def get_lat_lon(exif_data):
    """Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)"""
    lat = None
    lon = None
 
    if "GPSInfo" in exif_data:
        gps_info = exif_data["GPSInfo"]
 
        gps_latitude = _get_if_exist(gps_info, "GPSLatitude")
        gps_latitude_ref = _get_if_exist(gps_info, 'GPSLatitudeRef')
        gps_longitude = _get_if_exist(gps_info, 'GPSLongitude')
        gps_longitude_ref = _get_if_exist(gps_info, 'GPSLongitudeRef')
 
        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = _convert_to_degrees(gps_latitude)
            if gps_latitude_ref != "N":
                lat = 0 - lat
 
            lon = _convert_to_degrees(gps_longitude)
            if gps_longitude_ref != "E":
                lon = 0 - lon
 
    return lat, lon    

pics = sorted(os.listdir("img/" + sys.argv[1]))
pics = (p for p in pics if p.endswith(".JPG") or p.endswith(".jpg") or p.endswith(".JPEG") or p.endswith(".jpeg"))

csv = open("data.csv", "w") 
csv.write("filename,lat,lon,label,locname\n")

curlat = 0
curlon = 0

for pic in pics:
    try:
        gpsvalue = get_lat_lon(get_exif_data("img/" + sys.argv[1] + "/" + pic))
        lat = gpsvalue[0]
        lon = gpsvalue[1]
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
