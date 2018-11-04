### requires some changes to meet demand
### 1. import the sys library to make the file accept a json file as parameter, for now its hardcoded
### 2. since the excersice description was not clear, for now both of the bucket limits are not included
### 3. since the excersice description was not clear, for now a bucket from 0-11 does not exist
### 4. yuml dump returns sort of json, need to search a parameter to fix it
### 5. still didn't figure how to incorporate error handeling
### 6. the yaml dump returns some jibrish, need to look for a parameter to return as utf-8
### 7. all around messy code should consider re do it from the grounds up

import json
import yaml

#take a json file as parameter and returns it, need to return a dictionary- does not handle it yet
def load_json_and_return(j_file):
    with open(j_file, "r") as read_file:
        data = json.load(read_file)
        return data

#take the dictionary and returns the highest integer value
def d_keys(dictio):
    v_list = []
    for i in dictio["ppl_ages"].values():
        v_list.append(i)
    v_list.sort()
    max_val = v_list[-1]
    return max_val

#takes the "ppl_ages" dictionary and return a sorted list of the ages values
def l_keys(dictio):
    v_list = []
    for i in dictio["ppl_ages"].values():
        v_list.append(i)
    v_list.sort()
    return v_list

json_file_path = "./document_for_ex1.json"
from_j_to_p = load_json_and_return(json_file_path)
from_j_to_p["buckets"].sort()
from_j_to_p["buckets"].append(d_keys(from_j_to_p))

ages_dic_values = l_keys(from_j_to_p)
new_dict={}
for i in range(0,len(from_j_to_p["buckets"])-1):
    temp_list = []
    for i2 in from_j_to_p["ppl_ages"]:
        age_val = from_j_to_p["ppl_ages"].get(i2)
        if age_val > from_j_to_p["buckets"][i] and age_val < from_j_to_p["buckets"][i + 1]:
            temp_list.append(i2)
    new_dict[str(from_j_to_p["buckets"][i]) + "-" + str(from_j_to_p["buckets"][i + 1])] = temp_list

yaml_file_path = "./yaml_post.yaml"
with open(yaml_file_path, "w") as write_file:
    yaml.dump(new_dict, write_file)
