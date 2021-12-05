#Note: set python interpreter to the one provided by arcgis pro, 'arcgispro-py3'
#import necessary packages
import os, sys, arcpy

#Help the script find the data its working with
counties = r'D:\Projects\Final Project\Data\government_units\county_nrcs_a_al.shp'

#Folder to store outputs
output_path = ''

#set workspace
arcpy.env.workspace = ''

#List features in workspace
feature_list = arcpy.ListFeatureClasses()
print(feature_list)

#Make temporary layer
arcpy.MakeFeatureLayer_management(counties, 'JeffersonCounty')

#Select (county) by attribute
arcpy.SelectLayerByAttribute_management('JeffersonCounty', 'NEW_SELECTION', """ "COUNTYNAME" = 'Jefferson' """)

#Save the selection as a feature layer
arcpy.CopyFeatures_management("JeffersonCounty", "D:\Projects\Final Project\Data\JeffersonCountyAL")
