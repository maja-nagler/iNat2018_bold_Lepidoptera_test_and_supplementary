#!/usr/bin/env python
# coding: utf-8

# In[70]:


import json
import csv

# Get result of validating data
image_basedir = './images/'
test_filename = 'test_set_sample.json'
result_filename = 'checkpoint_20_test_data.csv'

# Read data we are testing
with open(test_filename, 'r') as json_file:
    json_data = json.load(json_file)

test = json_data
headings = [test_filename]

images = {}
categories = {}
image_to_category = {}

# Populate images and categories dictionaries
for image in test['images']:
    images[image['id']] = image

for category in test['categories']:
    categories[category['id']] = category
    categories[category['id']]['images'] = {}

for annotation in test['annotations']:
    category_id = annotation['category_id']
    image_id = annotation['image_id']
    categories[category_id]['images'][image_id] = images[image_id]
    image_to_category[image_id] = category_id

row_count = 0

with open(result_filename, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        row = [item.strip() for item in row]

        if len(row) > 1:
            if row_count == 0:
                headings = row
            else:
                id = int(row[0])
                predictions = list(map(int, row[1].split()))

                cat_id = image_to_category[id]
                categories[cat_id]['images'][id]['predictions'] = predictions

        row_count += 1



# In[59]:


print(category_id)


# In[60]:


print(image_id)


# In[61]:


images


# In[62]:


categories


# In[63]:


image_to_category


# In[ ]:





# In[71]:


import csv

# Initialize an empty dictionary to store the data
id_to_family_dict = {}

family_score = {}
# Open the TSV file for reading
with open('../inat2018-bold-lep/Lepidoptera-iNat.tsv', 'r', newline='') as tsvfile:
# Create a CSV reader with tab delimiter
    tsvreader = csv.reader(tsvfile, delimiter='\t')

    # Skip the header row
    next(tsvreader)

    # Iterate through the rows in the TSV file
    for row in tsvreader:
        # Extract the relevant columns
        id = row[0]  # Genus column
        family = row[7]
        # Create a dictionary entry with genus as the key
        # and the rest of the row data as the value

        id_to_family_dict[id] = family
        if family not in family_score:  
            family_score[family] = {
            'bo1': 0,
            'bo3': 0,
            'total images': 0
        }
# Print the resulting dictionary
for key, value in family_score.items():
    print(f'key: {key}')
    print(f'Data: {value}')


# In[72]:


total_images = 0
acc_bo1 = 0
acc_bo3 = 0
for category in categories.values():
    print(f'<h2>{category["name"]} [{category["id"]}]</h2>')
#     print('<div class="gallery">')
#     print('<ul>')
    acc_cat_bo1 = 0
    acc_cat_bo3 = 0
    cat_images_total = 0

    for image in category['images'].values():
#         print(category['id'])
        cat_images_total += 1
        style = ''
        if category['id'] in image['predictions']:
            
            acc_cat_bo3 += 1
            if image['predictions'][0] == category['id']:
                style = ' style="background:#2dc937;"'
                acc_cat_bo1 += 1
            else:
                style = ' style="background:#e7b416;"'
        else:
            style = ' style="background:#cc3232;"'

#         print(f'<li{style}>')
#         print(f'<img src="{image_basedir}/{image["file_name"]}" title="[{image["id"]}]">')
#         print('</li>')
    
    total_images += cat_images_total
    acc_bo1 += acc_cat_bo1
    acc_bo3 += acc_cat_bo3
#     print(category['id'])
    family = (id_to_family_dict[(str)(category['id'])])
    family_score[family]['bo1']+=acc_cat_bo1
    family_score[family]['bo3']+=acc_cat_bo3
    family_score[family]['total images']+=cat_images_total
    if (acc_cat_bo1 > acc_cat_bo3):
        print(str(avg_bo1) + ' >>>>>>>>>' + str(avg_bo3))
    avg_bo1 = acc_cat_bo1 / cat_images_total * 100
    avg_bo3 = acc_cat_bo3 / cat_images_total * 100
    avg_bo1 = "{:.2f}".format(avg_bo1)
    avg_bo3 = "{:.2f}".format(avg_bo3)

    print(f'cat acc bo1: {avg_bo1}% ({acc_cat_bo1}/{cat_images_total})<br>')
    print(f'cat acc bo3: {avg_bo3}% ({acc_cat_bo3}/{cat_images_total})<br>')
#     print('<li></li>')
#     print('</ul>')
#     print('</div>')

avg_bo1 = acc_bo1 / total_images * 100
avg_bo3 = acc_bo3 / total_images * 100
avg_bo1 = "{:.2f}".format(avg_bo1)
avg_bo3 = "{:.2f}".format(avg_bo3)

print(f'total acc bo1: {avg_bo1}% ({acc_bo1}/{total_images})<br>')
print(f'total acc bo3: {avg_bo3}% ({acc_bo3}/{total_images})<br>')
# print('</body>')
# print('</html>')


# In[73]:


for key, value in family_score.items():
    print(f'key: {key}')
    print(f'Data: {value}')

