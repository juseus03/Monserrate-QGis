#------------------------------------------------------------
#Imports
# ------------------------------------------------------------
import numpy as np

#------------------------------------------------------------
#Functions
# ------------------------------------------------------------

#Line Function
def drawLine(sp,ep,name):
    # create a new memory layer
    v_layer = QgsVectorLayer("LineString", name, "memory")
    pr = v_layer.dataProvider()
    # create a new feature
    seg = QgsFeature()
    # add the geometry to the feature, 
    seg.setGeometry(QgsGeometry.fromPolyline([sp, ep]))
    # ...it was here that you can add attributes, after having defined....
    # add the geometry to the layer
    pr.addFeatures( [ seg ] )
    # update extent of the layer (not necessary)
    v_layer.updateExtents()
    # show the line  
    QgsMapLayerRegistry.instance().addMapLayers([v_layer])

#Calcuates distance btwn points
def calcDist(sp,ep):
    distance = QgsDistanceArea()
    distance.setEllipsoidalMode(True)
    distance.setEllipsoid('WGS84')
    return distance.measureLine(sp,ep)

#------------------------------------------------------------
#Main
# ------------------------------------------------------------

#Get active layer
layer_points=iface.activeLayer()
print "Selected layer name: " ,layer_points.name()

#Reads points in layer
pointsX=np.zeros((0,0))
pointsY=np.zeros((0,0))

for f in layer_points.getFeatures():
    geom=f.geometry()
    pointsX=np.append(pointsX,geom.asPoint().x())
    pointsY=np.append(pointsY,geom.asPoint().y())

line_start = QgsPoint(pointsX[2],pointsY[2])
line_end = QgsPoint(pointsX[0],pointsY[0])
line_end1 = QgsPoint(pointsX[1],pointsY[1])
line = QgsGeometry.fromPolyline([line_start,line_end])

drawLine(line_start,line_end,"lineML-Max1")
drawLine(line_start,line_end1,"lineML-Iglesia")
drawLine(line_end1,line_end,"lineIglesiaMax1")
