import pandas as pd
import json
data = pd.read_csv("/home/vishal/Music/Data_RA1.csv")



columns_list = ["col1","col2","col3","col4","col8","col9","col11","col12","col13","col14","col15","col16","col17",
                "col17","col19","col20","col21","col23","col26"]

i=0
for column in columns_list:

    unique_col_vals = list(set(data[column].tolist()))
    counter = 0
    mapping_dict = {}
    for each_val in unique_col_vals:
        mapping_dict[each_val] = counter
        counter+=1

    with open("/home/vishal/Music/"+column+".json","w") as out:
        json.dump(mapping_dict,out)
    print(i)
    i+=1





