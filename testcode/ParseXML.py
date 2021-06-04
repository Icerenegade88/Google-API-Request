import xml.etree.ElementTree as ET
tree = ET.parse('C:\\Users\\harry\\Documents\\GitHub\\Google-API-Request\\testcode\\test1.xml')
root = tree.getroot()
root = ET.fromstring(book_data_as_string)

print(root.tag)
print(root.attrib)

for child in root.iter('price'):
    print(child.text)
    p1, p2 = [child.text, child.text]
    p1 = float(p1); p2 = float(p2)

total = p1+p2
print(f"Your total is: ${total}")

