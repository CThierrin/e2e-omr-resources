import xml.etree.ElementTree as ET
ET.register_namespace("mei","http://www.music-encoding.org/ns/mei")
def main(filename):

    tree=ET.parse(filename)
    root = tree.getroot()
    flag = False
    for child in root.iter("*"):

        if child.tag.endswith("clef"):
            flag = False
            for attr, value in child.attrib.items():
                
                if attr.endswith("shape") and value=="C":
                       flag = True
                       child.attrib["oct"]= "4"
                       break
        if child.tag.endswith("nc"):
            for attr, value in child.attrib.items():
                if attr.endswith("oct") and flag:
                       oct = int(value) +1
                       child.attrib[attr]= str(oct)
                       break
        


    new_tree = ET.ElementTree(root)
    new_tree.write(filename[:-4] + "NEW.mei", encoding="unicode", xml_declaration=True)