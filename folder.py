Dropbox/Karthik/python/folder.py
import os
import json
import xmltodict

swf = "../boy1"

os.system("swfmill swf2xml "+swf+".swf " + swf + ".xml")

with open(swf+".xml", 'r') as f:
    xmlString = f.read()
 
print("XML input (sample.xml):")
print(xmlString)
     
jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)
 
print("\nJSON output(" + swf + ".json):")
print(jsonString)
 
with open(swf+".json", 'w') as f:
    f.write(jsonString)
