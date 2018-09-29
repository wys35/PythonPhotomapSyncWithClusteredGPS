import csv
import pandas as pd
import fileinput 
import sys

tripname = sys.argv[1]

# read in the locations
locations = {}
with open('locations.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter="|")
    for row in csvreader:
        locations[int(row[0])] = row[1]
# read in the data with labels
labeleddata = pd.read_csv('datawithlabel.csv', delimiter=',')

# construct markers, iconFeatures, images
markerstr = "var markers = [];\n"
iconFeaturestr = "var iconFeatures = [];\n"
imageHTML = ""

currLabel = -1
currLoc = ""
for i, row in labeleddata.iterrows():
    if row['label'] != currLabel and int(row['label']) != -1: # generate marker, iconFeatures, divider div
        currLabel = int(row['label'])
        currLoc = locations[currLabel]
        markerstr += "  markers.push(ol.proj.fromLonLat([" + str(row['lon']) + ", " + str(row['lat']) + "]));\n"
        iconFeaturestr += "  var iconFeature" + str(currLabel) + " = new ol.Feature({\n"
        iconFeaturestr += "    geometry: new ol.geom.Point(ol.proj.transform([" + str(row['lon']) + ", " + str(row['lat']) + "], 'EPSG:4326', 'EPSG:3857')),\n"
        iconFeaturestr += "    name : \"" + currLoc +"\",\n"
        iconFeaturestr += "    id : 'marker" + str(currLabel) + "'\n"
        iconFeaturestr += "  });\n"
        iconFeaturestr += "  iconFeatures.push(iconFeature" + str(currLabel) + ");\n"
        imageHTML += "<span><img src='img/logo.png' alt="" />&nbsp;&nbsp;" + currLoc  +"&nbsp;&nbsp;<img src='img/logo.png' alt="" /></span><br/>\n"
        #imageHTML += "<img id='marker" + str(currLabel) + "' src='img/" + tripname + "/" + row['filename'] + "' class='photo'><br/>\n"
        imageHTML += "<img id='marker" + str(currLabel) + "' src='https://raw.githubusercontent.com/wys35/wys35.github.io/master/img/" + tripname + "/" + row['filename'] + "' class='photo'><br/>\n"
    else:
	    #imageHTML +="<img src='img/" + tripname + "/" + row['filename'] + "' class='photo'><br/>\n"
        imageHTML +="<img src='https://raw.githubusercontent.com/wys35/wys35.github.io/master/img/" + tripname + "/"+ row['filename'] + "' class='photo'><br/>\n"
    

# read in template, swap in the constructed values

with open("template.html", "r") as f:
    data = f.read()

data = data.replace('// markers, locations', markerstr)
data = data.replace('// iconFeatures, Tooltips', iconFeaturestr)
data = data.replace('<!-- images -->', imageHTML)

with open(tripname + ".html", "w", encoding='utf-8') as f:
    f.write(data)