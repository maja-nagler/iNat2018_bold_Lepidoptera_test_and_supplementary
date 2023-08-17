#!/usr/bin/env python
# coding: utf-8

# In[36]:


# Open the file for reading
try:
    with open('/home/maja_nagler/inat2018-bold-lep/iNat/shared_categories.tsv', 'r') as file:
        content = file.readlines()
except FileNotFoundError:
    print("File was not found.")
    content = ""

# Split the content into words

# Create a two-dimensional array and assign the first two words
cat_with_ID = []
max = len(content)
for i in range(1, max):

    words = content[i].split('\t')
    if len(words) >= 2:
        cat_with_ID.append([words[0], words[1]])

# Display the two-dimensional array
# print("Two-dimensional array with the first two words:")
# for row in cat_with_ID:
#     print(row)

# Convert the matrix to a dictionary
matrix_dict = {}
for row in cat_with_ID:
    key = row[1]
    value = row[0]
    matrix_dict[key] = value

# print(matrix_dict)
if "596" in matrix_dict:
    print("Key 'age' exists in the dictionary.")
else:
    print("Key 'age' does not exist in the dictionary.")


# In[46]:


import json

# Step 1: Open and read the JSON file
with open('/home/maja_nagler/inat2018-bold-lep/BOLD/train.json', 'r') as file:
    json_data = file.read()

# Step 2: Convert JSON to dictionary
data_dict = json.loads(json_data)

# Now you can use data_dict as a regular Python dictionary
# print(data_dict)


# In[40]:


print(matrix_dict)


# In[53]:


# for cat in cat_with_ID:
#     print(cat[1])

annotations_to_delete = {}
images_to_delete = {}
categories__to_delete = {}
for i, row in enumerate(data_dict['annotations']):
#     print(row['category_id'])
    cat_id = str(row['category_id'])
    if cat_id in matrix_dict:
        pass
#          print("Key 'age' exists in the dictionary.")
    else:
        print("Key 'age' does not exist in the dictionary.")
print('1')


# In[ ]:




