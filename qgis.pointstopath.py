import processing

for file in glob.glob('./*') :
    processing.run("qgis:pointstopath", {'INPUT' : 'delimitedtext://file:///C:/Users/guestname/data/sample/' + file + '?type=csv&maxFields=10000&detectTypes=yes&xField=Longitude&yField=Latitude&crs=EPSG:4326&spatialIndex=no&subsetIndex=no&watchFile=no',
'ORDER_FIELD' : 'Timestamp', 'OUTPUT' : 'C:/Users/guestname/data/sample_shp/' + os.path.splitext(file)[0] + '.shp'})