import xml.etree.ElementTree as ET
import csv

# 1) input to the program
base_file = input("Enter the name of the baseline file: ")
new_file = input("Enter the name of the file to be compared: ")

# base_file = 'ASR9K-SR-ISIS-v662.xml'
# new_file = 'ASR9K-SR-ISIS-v731.xml'

base_file = 'SNMPIFINDEX-Baseline.xml'
new_file = 'SNMPIFINDEX-Compare.xml'

# 2) parsing the file
base = ET.parse(base_file)
base_root = base.getroot()

new = ET.parse(new_file)
new_root = new.getroot()

# 3) tags/data comparison and 4) flagging deviations and 5) summary and output
# creating an 2d array with all of the tags and data in the base file
base_array = []

for elem in base_root:
    for sub in elem:
        base_array.append([sub.tag, sub.text.strip()])
        for child in sub:
            base_array.append([child.tag, child.text])

# creating an 2d array with all of the tags and data in the new file
new_array = []

for elem in new_root:
    for sub in elem:
        new_array.append([sub.tag, sub.text.strip()])
        for child in sub:
            new_array.append([child.tag, child.text])

# creating a formatted version of the base array
b_f_array = []
for i in range(len(base_array)):
    if base_array[i][1] == '':
        b_array = []
        b_array.append([base_array[i][0]])
        j = i + 1
        while base_array[j][1] != '':
            b_array.append([base_array[j][0], base_array[j][1]])
            if j == len(base_array) - 1:
                break
            j += 1
        b_f_array.append(b_array)

# print()
# for l in b_f_array:
#     print(l)
#
# print()
# print()
# creating a formatted version of the base array
n_f_array = []
for i in range(len(new_array)):
    if new_array[i][1] == '':
        n_array = []
        n_array.append([new_array[i][0]])
        j = i + 1
        while new_array[j][1] != '':
            n_array.append([new_array[j][0], new_array[j][1]])
            if j == len(new_array) - 1:
                break
            j += 1
        n_f_array.append(n_array)

# print()
# for l in n_f_array:
#     print(l)
#
# print()
# print()
# writing the output to a csv file
with open('deviations.csv', mode='w') as deviations_file:
    deviations_writer = csv.writer(deviations_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    deviations_writer.writerow([f'Comparison of \'{base_file}\' and \'{new_file}\''])

    # finding out which one is longer
    if len(b_f_array) > len(n_f_array):
        length = len(b_f_array)
    elif len(b_f_array) < len(n_f_array):
        length = len(n_f_array)
    else:
        length = len(b_f_array)

    for i in range(length):
        try:
            b_f_array[i][0]
        except:
            b_o_tag = None
        else:
            b_o_tag = b_f_array[i][0]

        try:
            n_f_array[i][0]
        except:
            n_o_tag = None
        else:
            n_o_tag = n_f_array[i][0]

        if b_o_tag != n_o_tag:
            if b_o_tag is None:
                print(f'TAG DEVIATION:\tBase tag: None\t New tag: {n_o_tag[0]}')
                deviations_writer.writerow([f'TAG DEVIATION:', f'Base tag: None', f'New tag: {n_o_tag[0]}'])
            elif n_o_tag is None:
                print(f'TAG DEVIATION:\tBase tag: {b_o_tag[0]}\t New tag: None')
                deviations_writer.writerow([f'TAG DEVIATION:', f'Base tag: {b_o_tag[0]}', f'New tag: None'])
            else:
                print(f'TAG DEVIATION:\tBase tag: {b_o_tag[0]}\t New tag: {n_o_tag[0]}')
                deviations_writer.writerow([f'TAG DEVIATION:', f'Base tag: {b_o_tag[0]}', f'New tag: {n_o_tag[0]}'])
        else:
            print(f'TAGS MATCH:\tBase tag: {b_o_tag[0]}\t New tag: {n_o_tag[0]}')
            deviations_writer.writerow([f'TAGS MATCH:', f'Base tag: {b_o_tag[0]}', f'New tag: {n_o_tag[0]}'])

        # to traverse the inner tags and data

        if len(b_f_array[i]) > len(n_f_array[i]):
            i_length = len(b_f_array[i])
        elif len(b_f_array[i]) < len(n_f_array[i]):
            i_length = len(n_f_array[i])
        else:
            i_length = len(b_f_array[i])
        n_tags_arr = []
        b_tags_arr = []
        both_tags = []

        # print('b_f_array[i]',len(b_f_array[i]))
        # print('n_f_array[i]',len(n_f_array[i]))
        # print('i_length', i_length)
        for j in range(i_length):
            # print(i, j)
            try:
                b_f_array[i][j][0]
            except:
                b_index = None
            else:
                b_index = b_f_array[i][j][0]

            try:
                n_f_array[i][j][0]
            except:
                n_index = None
            else:
                n_index = n_f_array[i][j][0]

            if n_index is not None:
                n_tags_arr.append(n_index)
            if b_index is not None:
                b_tags_arr.append(b_index)

            b_f_array_copy = b_f_array[:]
            n_f_array_copy = n_f_array[:]

            for n in n_tags_arr:
                for b in b_tags_arr:
                    if n == b:
                        both_tags.append(n)
                        n_tags_arr.remove(n)
                        b_tags_arr.remove(b)

        for x in b_f_array_copy[i]:
            for y in n_f_array_copy[i]:
                if x == y:
                    b_f_array_copy[i].remove(x)
                    n_f_array_copy[i].remove(y)

        # tag deviation
        for n in n_tags_arr:
            print(f"Tag deviation inside '{b_o_tag[0]}':\nBase tag: None\tNew tag: {n}")
            deviations_writer.writerow([f'Tag deviation inside \'{b_o_tag[0]}\':', f'Base tag: None', f'New tag: {n}'])

        for b in b_tags_arr:
            print(f"Tag deviation inside '{b_o_tag[0]}':\nBase tag: {b}\tNew tag: None")
            deviations_writer.writerow([f'Tag deviation inside \'{b_o_tag[0]}\':', f'Base tag: {b}', f'New tag: None'])

        # data deviation
        for a in range(len(b_f_array_copy[i])):
            for b in range(len(n_f_array_copy[i])):
                if b_f_array_copy[i][a][0] == n_f_array_copy[i][b][0]:
                    if b_f_array_copy[i][a][1] != n_f_array_copy[i][b][1]:
                        print(
                            f"Data deviation inside '{b_f_array_copy[i][a][0]}':\nBase data: {b_f_array_copy[i][a][1]}\tNew data: {n_f_array_copy[i][b][1]}")
                        deviations_writer.writerow(
                            [f'Data deviation inside \'{b_f_array_copy[i][a][0]}\':',
                             f'Base data: {b_f_array_copy[i][a][1]}',
                             f'New data: {n_f_array_copy[i][b][1]}'])
        print()
        print()
