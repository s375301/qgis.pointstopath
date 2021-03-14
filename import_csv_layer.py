import os, glob
os.chdir('/Users/guestname/data')

layers = []
for file in glob.glob('./*') :
    uri = "file:///C:/Users/guestname/data/sample" + file + "?type=csv&maxFields=10000&detectTypes=yes&xField=Longitude&yField=Latitude&crs=EPSG:4326&spatialIndex=no&subsetIndex=no&watchFile=no"
    vlayer = QgsVectorLayer(uri, os.path.basename(file), "delimitedtext")
    layers.append(vlayer)
#    QgsProject.instance().addMapLayer(vlayer)

QgsProject.instance().addMapLayers(layers)