import xml.etree.ElementTree as ET

xml_data = """
<person>
    <id>1</id>
    <first_namename>John</first_namename>
    <last_name>Doe</last_name>
    <age>30</age>
    <email>john.doe@mail.ru</email>
    <address>
        <street>Main Street</street>
        <city>New York</city>
    </address>
</person>
"""

root = ET.fromstring(xml_data)

print(root.find("id").text)