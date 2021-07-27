import xml.etree.ElementTree as ET

# 1) input to the program
base_file = input("Enter the name of the baseline file: ")
new_file = input("Enter the name of the file to be compared: ")

base_file = 'xml1.xml'
new_file = 'xml2.xml'

# 2) parsing the file
base = ET.parse(base_file)
base_root = base.getroot()

new = ET.parse(new_file)
new_root = new.getroot()

# printing out elements and tags
'''
# prints out all the tags
for elem in base_root:
    for subelem in elem:
        print(subelem.tag)

print()

# prints out all data in file
for elem in base_root:
    for subelem in elem:
        print(subelem.text)
'''

# 3) tags comparison

for i in range(len(base_root[0])):
    print()
    base_tag = None
    new_tag = None
    # base file
    try:  # checking to make sure there is a value
        base_root[0][i].tag
    except:  # prints out error
        print(f"Tags do not match\nBase tag: {base_tag} \nNew tag: {new_tag}")
    else:
        base_tag = base_root[0][i].tag

    # new file
    try:  # checking to make sure there is a value
        new_root[0][i].tag
    except:  # prints out error
        print(f"Tags do not match\nBase tag: {base_tag} \nNew tag: {new_tag}")
    else:
        new_tag = new_root[0][i].tag

    # comparison
    if base_tag != new_tag and base_tag is not None and new_tag is not None:
        print(f"Tags do not match\nBase tag: {base_tag} \nNew tag: {new_tag}")
    elif base_tag == new_tag:
        print(f"Tags match\nBase tag: {base_tag} \nNew tag: {new_tag}")

print()
# 3) data comparison
print()
for elem in base_root:
    for subelem in elem:
        print(subelem.text)
print()
for elem in new_root:
    for subelem in elem:
        print(subelem.text)

# 4) flagging deviations
# 5) summary and output

# EXTRA: printing out elements and tags
'''
# prints out length
print(len(base_root[0]))
'''

# print(base_root[0][0].tag) #prints out to
# print(base_root[0][0].text) #prints out tove

'''
# prints out all tags in the file
for elem in base.iter():
    print(elem.tag)
'''

'''
# prints out all the tags
for i in range(len(base_root[0])):
    print(base_root[0][i].tag)
'''

'''
# creates a list with all tags in the doc
elem_list = []
for elem in base.iter():
    elem_list.append(elem.tag)
print(elem_list)
'''

'''
# prints something related to tags
for elem in base_root:
    for subelem in elem:
        if elem.tag:
            print(elem.tag)
'''