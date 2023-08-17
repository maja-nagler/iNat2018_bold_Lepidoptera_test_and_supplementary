#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pygbif


# In[2]:


import gbif_dl
import pygbif 


# In[3]:


from pygbif import occurrences


# In[39]:


# Open the file for reading
try:
    with open('../inat2018-bold-lep/iNat/shared_categories.tsv', 'r') as file:
        content = file.readlines()
except FileNotFoundError:
    print("The file was not found.")
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
print("Two-dimensional array with the first two words:")
for row in cat_with_ID:
    print(row)


# In[144]:


#Reading IDs (from cat_with_ID in shared categories)
cat_with_TaxonKey = []
shame = []
max = len(cat_with_ID)
for i in range(0, max):
    res = occurrences.search(scientificName = cat_with_ID[i][0], order='Lepidoptera', year='2019,2022', limit=1, mediatype = 'StillImage')
    print(cat_with_ID[i][0])
    print(res['results'])
    print(bool(res['results']))
    if (bool(res['results'])):
        taxon = res['results'][0]['speciesKey']
        cat_with_TaxonKey.append([cat_with_ID[i][0], taxon])
    else:
        shame.append(cat_with_ID[i][0])
for row in cat_with_TaxonKey:
    print(row)


# In[167]:


queries = {
    "speciesKey": [],
    "year": [2019,2022]
}
SpeciesKeyList = []
queries["speciesKey"] = SpeciesKeyList
for i in range(0, len(cat_with_TaxonKey)):
#     print(cat_with_TaxonKey[i][1])
    SpeciesKeyList.append(cat_with_TaxonKey[i][1])
#     print(row)


# In[170]:


import gbif_dl

data_generator = gbif_dl.api.generate_urls(
    queries=queries,
    label="speciesKey",
    nb_samples_per_stream=10,
#     weighted_streams=True,
    split_streams_by=["speciesKey"],
)
data_table = []


# In[173]:


for i in data_generator:
    data_table.append(i)


# In[183]:


print(len(data_table))
# for i in data_table:
#     print(i)
print(data_table[2])
type(data_table[0])


# In[191]:


print(data_table[0])


# In[198]:


import os
import requests
from PIL import Image
w_and_h = []

def download_image(url, folder_path, filename):
    filepath = os.path.join(folder_path, filename)
    if(os.path.exists(filepath)):
        return
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Get the file name from the URL
        

        # Save the image in the folder
        with open(filepath, "wb") as file:
            file.write(response.content)

        print(f"Image downloaded and saved as {filename} in the {folder_path} folder")

        # Get the size of the image in pixels
        img = Image.open(filepath)
        width, height = img.size
        w_and_h.append([width, height])
    except requests.exceptions.RequestException as e:
         print("An error occurred while downloading the image:", e)

# Enter the image URL and the folder path where you want to save it


for i in range(0, len(data_table)):
    image_url = data_table[i]['url']
    save_folder = "images/" + data_table[i]['label']
    filename = data_table[i]['basename'] + '.jpg'
     # Check if the folder exists, if not, create it
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Download and save the image, and display its dimensions
    download_image(image_url, save_folder, filename)


# In[204]:


cat_with_ID_copy = cat_with_ID.copy()


# In[206]:


for i in cat_with_ID_copy:
    print(i)


# In[208]:


def remove_element_by_name(lst, target_name):
    index_to_remove = None
    for index, element in enumerate(lst):
        if element[0] == target_name:
            index_to_remove = index
            break
    
    if index_to_remove is not None:
        lst.pop(index_to_remove)
        print(f"Removed element with the name '{target_name}'.")
    else:
        print(f"Element with the name '{target_name}' not found.")

# Sample nested list where the first cell contains the name
cat_with_ID_copy

for i in shame:
    remove_element_by_name(cat_with_ID_copy, i)
    print("List after removal:")
print(cat_with_ID_copy)


# In[2]:


len(cat_with_ID_copy)


# In[224]:


desc = {"description": "iNat"}
type(desc)
descList = []
descList.append(desc)
desc["description"]


# In[228]:


print(cat_with_ID[0])
print(cat_with_TaxonKey[0])
print(data_table[0])


# In[248]:


for j in dictForJson["licenses"]:
#     print(j["url"])
    if(j["url"] == 'http://creativecommons.org/licenses/by-nc/4.0/'):
        print(j["url"])
        


# In[284]:


def list_to_dictionary(lst):
    dictionary = {}
    for element in lst:
        key = element[0]
        rest_of_elements = element[1]  # Ignoring the second element as the key
        dictionary[key] = rest_of_elements
    return dictionary

def list_to_dictionary_reverse(lst):
    dictionary = {}
    for element in lst:
        key = element[1]
        rest_of_elements = element[0]  # Ignoring the second element as the key
        dictionary[key] = rest_of_elements
    return dictionary

cat_with_TaxonKeyDict = list_to_dictionary_reverse(cat_with_TaxonKey)
print(cat_with_TaxonKeyDict)
cat_with_ID_copyDict = list_to_dictionary(cat_with_ID_copy)
print(cat_with_ID_copyDict)


# In[307]:


#dicitonary
dictForJson = {
    "info": descList[0],
    "images":[],
    "licenses": [{"url": "http://creativecommons.org/licenses/by-nc-nd/4.0/", "id": 1, "name": "Attribution-NonCommercial-NoDerivatives License"}, {"url": "http://creativecommons.org/licenses/by-nc-sa/4.0/", "id": 2, "name": "Attribution-NonCommercial-ShareAlike License"}, {"url": "http://creativecommons.org/licenses/by-nc/4.0/", "id": 3, "name": "Attribution-NonCommercial License"}, {"url": "http://creativecommons.org/licenses/by-nd/4.0/", "id": 4, "name": "Attribution-NoDerivatives License"}, {"url": "http://creativecommons.org/licenses/by-sa/4.0/", "id": 5, "name": "Attribution-ShareAlike License"}, {"url": "http://creativecommons.org/licenses/by/4.0/", "id": 6, "name": "Attribution License"}, {"url": "http://creativecommons.org/publicdomain/zero/1.0/", "id": 7, "name": "Public Domain Dedication"}, {"url": "http://en.wikipedia.org/wiki/Copyright", "id": 8, "name": "No known copyright restrictions"}],
    "annotations":[],
    "categories":[],
}
imagesList = []
annotationsList = []
categoriesList = []

# print(cat_with_ID_copy)
# print(type(cat_with_TaxonKey))
# print(type(data_table))
# print(w_and_h)
for i in range(0, len(data_table)):
    folder_path = save_folder = "images/" + data_table[i]['label']
    filename = data_table[i]['basename'] + '.jpg'
    filepath = os.path.join(folder_path, filename)
    if not (os.path.exists(filepath)): #jeżeli nie ma #moduł syst operacyjnego
        continue
    img = Image.open(filepath)
    width, height = img.size
    label = int(data_table[i]['label'])
    dictForImage ={"id":i,"license":data_table[i]["license"],"file_name":filepath,"height":width,"width":height}
    imagesList.append(dictForImage)
    category_name = cat_with_TaxonKeyDict[label]
    category_id = int(cat_with_ID_copyDict[category_name])
#     print(cat_with_ID_copyDict[category_name])
    dictForAnno = {"id":i,"image_id":i,"category_id":category_id}
    annotationsList.append(dictForAnno)
    dictForCat = {"name":category_name,"id":category_id}
    categoriesList.append(dictForCat)
    
dictForJson["images"] = imagesList           
dictForJson["annotations"] = annotationsList
dictForJson["categories"] = categoriesList

print(categoriesList)
print(dictForJson["annotations"])
# {"id":437515,"license":3,"file_name":"images\/train_val2018\/Insecta\/673\/cb75e788cfe2bfe52485a7d146bf1494.jpg","height":582,"width":800}
# "licenses":[{"url":"http:\/\/creativecommons.org\/licenses\/by-nc-nd\/4.0\/","id":1,"name":"Attribution-NonCommercial-NoDerivatives License"},{"url":"http:\/\/creativecommons.org\/licenses\/by-nc-sa\/4.0\/","id":2,"name":"Attribution-NonCommercial-ShareAlike License"},{"url":"http:\/\/creativecommons.org\/licenses\/by-nc\/4.0\/","id":3,"name":"Attribution-NonCommercial License"},{"url":"http:\/\/creativecommons.org\/licenses\/by-nd\/4.0\/","id":4,"name":"Attribution-NoDerivatives License"},{"url":"http:\/\/creativecommons.org\/licenses\/by-sa\/4.0\/","id":5,"name":"Attribution-ShareAlike License"},{"url":"http:\/\/creativecommons.org\/licenses\/by\/4.0\/","id":6,"name":"Attribution License"},{"url":"http:\/\/creativecommons.org\/publicdomain\/zero\/1.0\/","id":7,"name":"Public Domain Dedication"},{"url":"http:\/\/en.wikipedia.org\/wiki\/Copyright","id":8,"name":"No known copyright restrictions"}]
# "annotations":[{"id":437515,"image_id":437515,"category_id":673},{"id":437517,"image_id":437517,"category_id":1455},
# "categories":[{"name":"Pilocrocis ramentalis","id":"673"},{"name":"Dynamine postverta","id":"1455"},


# In[308]:


import json
    
# Data to be written

    
with open("test_set_sample.json", "w") as outfile: #file in write mode
    json.dump(dictForJson, outfile)


# In[229]:


#Saving variables
get_ipython().run_line_magic('store', 'cat_with_ID')
get_ipython().run_line_magic('store', 'shame')
get_ipython().run_line_magic('store', 'cat_with_TaxonKey')
get_ipython().run_line_magic('store', 'queries')
get_ipython().run_line_magic('store', 'data_table')
get_ipython().run_line_magic('store', 'w_and_h')


# In[202]:


for i in cat_with_TaxonKey:
    print(i)


# In[ ]:




