import xml.etree.ElementTree as ET
import csv

# 1) input to the program
base_file = input("Enter the name of the baseline file: ")
new_file = input("Enter the name of the file to be compared: ")

base_file = 'ASR9K-SR-ISIS-v662.xml'
new_file = 'ASR9K-SR-ISIS-v731.xml'

# 2) parsing the file
base = ET.parse(base_file)
base_root = base.getroot()
print(base_root)
print(len(base_root))

new = ET.parse(new_file)
new_root = new.getroot()
print(new_root)
# print(len(base_root))

# 3) tags/data comparison and 4) flagging deviations and 5) summary and output
num_deviations = 0  # this statement isnt used currently
# checking to see what file is longer
if len(base_root[0]) > len(new_root[0]):
    length = len(base_root[0])
elif len(base_root[0]) < len(new_root[0]):
    length = len(new_root[0])
else:
    length = len(base_root[0])

base_array = []

for elem in base_root:
    for subelem in elem:
        # print(sub.tag)
        base_array.append([subelem.tag, subelem.text])
        for child in subelem:
            # print(child.tag)
            # print("data: ",child.text)
            base_array.append([child.tag, child.text])
print(base_array)


with open('deviations.csv', mode='w') as deviations_file:
    deviations_writer = csv.writer(deviations_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    deviations_writer.writerow([f'Comparison of \'{base_file}\' and \'{new_file}\''])

    # comparing tags and printing out if they are different
    for i in range(length):
        base_tag = None
        new_tag = None
        # base file
        # try:  # checking to make sure there is a value
        #     base_root[0][i].tag
        # except:  # prints out error
        #     print(f"Tag deviation\nBase tag: {base_tag} \nNew tag: {new_tag}")
        #     deviations_writer.writerow([f'Tag deviation', f'Base tag: {base_tag}', f'New tag: {new_tag}'])
        #     num_deviations += 1
        # else:
        #     base_tag = base_root[0][i].tag
        #     print(f"Tag deviation\nBase tag: {base_tag} \nNew tag: {new_tag}")
        #
        # # new file
        # try:  # checking to make sure there is a value
        #     new_root[0][i].tag
        # except:  # prints out error
        #     print(f"Tag deviation\nBase tag: {base_tag} \nNew tag: {new_tag}")
        #     deviations_writer.writerow([f'Tag deviation', f'Base tag: {base_tag}', f'New tag: {new_tag}'])
        #     num_deviations += 1
        # else:
        #     new_tag = new_root[0][i].tag
        #     print(f"Base tag: {base_tag} \nNew tag: {new_tag}")

        try:
            base_root[1][1].tag
        except:
            print("no data")
        else:
            print(base_root[1][1].tag)


        # comparison
        # if base_tag != new_tag and base_tag is not None and new_tag is not None:
        #     print(f"Tag deviation\nBase tag: {base_tag} \nNew tag: {new_tag}")
        #     deviations_writer.writerow([f'Tag deviation', f'Base tag: {base_tag}', f'New tag: {new_tag}'])
        #     num_deviations += 1
        # elif base_tag == new_tag:
        #     # print(f"Tags match\nBase tag: {base_tag} \nNew tag: {new_tag}")
        #     # 3) data comparison
        #     base_data = None
        #     new_data = None
        #     # base file
        #     try:  # checking to make sure there is a value
        #         base_root[0][i].text
        #     except:  # prints out error
        #         print(f"Data deviation\nTag: {base_tag}\nBase data: {base_data} \nNew data: {new_data}")
        #         deviations_writer.writerow(
        #             [f'Data deviation', f'Tag: {base_tag}', f'Base data: {base_data}', f'New data: {new_data}'])
        #         num_deviations += 1
        #     else:
        #         base_data = base_root[0][i].text
        #
        #     # new file
        #     try:  # checking to make sure there is a value
        #         new_root[0][i].text
        #     except:  # prints out error
        #         print(f"Data deviation\nTag: {base_tag}\nBase data: {base_data} \nNew data: {new_data}")
        #         deviations_writer.writerow(
        #             [f'Data deviation', f'Tag: {base_tag}', f'Base data: {base_data}', f'New data: {new_data}'])
        #         num_deviations += 1
        #     else:
        #         new_data = new_root[0][i].text
        #
        #     # comparison
        #     if base_data != new_data and base_data is not None and new_data is not None:
        #         print(f"Data deviation\nTag: {base_tag}\nBase data: {base_data} \nNew data: {new_data}")
        #         deviations_writer.writerow(
        #             [f'Data deviation', f'Tag: {base_tag}', f'Base data: {base_data}', f'New data: {new_data}'])
        #         num_deviations += 1
        #     # elif base_data == new_data:
        #     # print(f'Data matches\nData in base: {base_data} \nData in new: {new_data}')
        #     print()

# EXTRA: printing out elements and tags, mainly for testing to get comfortable with the ET module
'''
# prints out length
print(len(base_root[0]))
print(base_root[0][0].tag) #prints out to
print(base_root[0][0].text) #prints out tove
# prints out all tags in the file
for elem in base.iter():
    print(elem.tag)
# prints out all the tags
for i in range(len(base_root[0])):
    print(base_root[0][i].tag)
# creates a list with all tags in the doc
elem_list = []
for elem in base.iter():
    elem_list.append(elem.tag)
print(elem_list)
# prints something related to tags
for elem in base_root:
    for sub in elem:
        if elem.tag:
            print(elem.tag)
#simplest way to print tags and data
for elem in base_root:
    for sub in elem:
        print(sub.text)
print()
for elem in new_root:
    for sub in elem:
        print(sub.text)
'''
