#------------------------------------------------------------
#Imports
# ------------------------------------------------------------
import numpy as np

#------------------------------------------------------------
#Functions
# ------------------------------------------------------------

#Line Function
def drawLine(sp,ep,angle_base):
    angle=angle_base-sp.azimuth(ep)
    name="line_%.2f" %(angle)
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
    
    #------------------------------------------------------------
#Main
# ------------------------------------------------------------

#Get active layer
layer_points=iface.activeLayer()
print "Selected layer name: " ,layer_points.name()

#Creates reference Points
pt_ML = QgsPoint(-74.0647,4.60274)
pt_ig = QgsPoint(-74.0554,4.60565)
angle_MLig=pt_ML.azimuth(pt_ig)

#Reads points in layer

for f in layer_points.getFeatures():
    geom=f.geometry()
    pt_act=QgsPoint(geom.asPoint().x(),geom.asPoint().y())
    drawLine(pt_ML,pt_act,angle_MLig)





