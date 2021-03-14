os.chdir('C:/Users/guestname/data/sample_shp')

layers = []
for file in glob.glob('*') :
    if 'shp' in file.split('.', 2) :
        slayer = QgsVectorLayer(os.path.basename(file), file.split('.', 2)[0], "ogr")
        layers.append(slayer)

QgsProject.instance().addMapLayers(layers)