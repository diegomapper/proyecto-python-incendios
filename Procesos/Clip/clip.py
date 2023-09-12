import arcpy, os

arcpy.env.workspace = 'Z:/Desktop/GIS/proyecto-python-incendios/'
arcpy.env.overwriteOutput = True

mxd = arcpy.mapping.MapDocument('incendios.mxd')
df = arcpy.mapping.ListDataFrames(mxd,"Layers")[0]
