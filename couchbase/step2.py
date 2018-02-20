import pandas as pd
import os
import json
import unicodedata

data = pd.read_csv("/home/vishal/Music/Data_RA1Final.csv")
data_for_write = data.copy()

source_folder = "/home/vishal/Documents/"

for file in os.listdir(source_folder):

    if file.endswith(".json"):

        print(file)
        column_header = file.split(".")[0]

        mapping_dict = json.loads(open(source_folder + "/" + file).read())
        old_vals = [unicodedata.normalize('NFKD', each).encode('ascii', 'ignore') for each in list(mapping_dict.keys())]
        new_vals = list(mapping_dict.values())
        print(type(old_vals), type(new_vals))

        # if file=="col22.json":
        #     data_for_write[column_header].replace([True,False],new_vals,inplace=True)

        data_for_write[column_header].replace([True,False], new_vals, inplace=True)

data_for_write.to_csv("/home/vishal/Music/Data_RA1Final_22.csv",index=False)

