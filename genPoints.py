import numpy as np

def addPoint(pr,ptML,ptIg,angl,r):
    alpha=(angl)*np.pi/180
    x=ptML.x()+r*np.cos(alpha)
    y=ptML.y()+r*np.sin(alpha)
    pt_add=QgsPoint(x,y)  
    # add a feature
    fet = QgsFeature()
    fet.setGeometry( QgsGeometry.fromPoint(pt_add) )
    pr.addFeatures( [ fet ] )
    return pt_add
#Get active layer
layer_points=iface.activeLayer()
pr=layer_points.dataProvider()

print "Selected layer name: " ,layer_points.name()

#Reads points in layer
pointsX=np.zeros((0,0))
pointsY=np.zeros((0,0))

for f in layer_points.getFeatures():
    geom=f.geometry()
    pointsX=np.append(pointsX,geom.asPoint().x())
    pointsY=np.append(pointsY,geom.asPoint().y())

pt_ML = QgsPoint(pointsX[0],pointsY[0])
pt_ig = QgsPoint(pointsX[1],pointsY[1])  

angl=20

#Starts Editing mode to layer
layer_points.startEditing()
pt_add=addPoint(pr,pt_ML,pt_ig,angl,1080)
# Commit changes
layer_points.commitChanges()
