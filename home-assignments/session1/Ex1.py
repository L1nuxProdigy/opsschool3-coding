### requires some changes to meet demand
### 5. still didn't figure how to incorporate error handeling
### 7. all around messy code should consider re do it from the grounds up

### 1-4 + 6 issues dealt with :]], also 5 had been dealt with a little bit

import json
import yaml
import sys
import os.path

def accept_json_as_argument():
    if len(sys.argv) <= 1:
        print("dude where is the file?")
        sys.exit()
    json_as_argument = sys.argv[1]
    if not os.path.exists(json_as_argument):
        print("Hey, the %s file was not found, give me correct path and file"% json_as_argument)
        sys.exit()
    # json_to_py_obj = open(json_as_argument,"r")
    # return json.load(json_to_py_obj)
    with open(json_as_argument, "r") as json_to_py_obj:
        return_json_as_python = json.load(json_to_py_obj)
    return return_json_as_python


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

from_j_to_p = accept_json_as_argument()
from_j_to_p["buckets"].sort()
if from_j_to_p["buckets"][0] > 0:
    from_j_to_p["buckets"].insert(0,0)
from_j_to_p["buckets"].append(d_keys(from_j_to_p))

ages_dic_values = l_keys(from_j_to_p)
new_dict={}
for i in range(0,len(from_j_to_p["buckets"])-1):
    temp_list = []
    for i2 in from_j_to_p["ppl_ages"]:
        age_val = from_j_to_p["ppl_ages"].get(i2)
        if age_val > from_j_to_p["buckets"][i] and age_val <= from_j_to_p["buckets"][i + 1]:
            temp_list.append(i2)
    new_dict[str(from_j_to_p["buckets"][i]) + "-" + str(from_j_to_p["buckets"][i + 1])] = temp_list

yaml_file_path = "./yaml_post.yaml"
with open(yaml_file_path, "w") as write_file:
    yaml.dump(new_dict, write_file, default_flow_style=False, allow_unicode=True)
    write_file.close()

