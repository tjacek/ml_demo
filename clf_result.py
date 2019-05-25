import os
import itertools
from collections import defaultdict

def clf_result(in_path):
    result=defaultdict(list)
    for name_i,dict_i in read_results(in_path):
    	result[name_i].append(dict_i)
    return result.keys()

def read_results(dir_path):
    filepaths= [ [root_i +'/'+ files_ji for files_ji in files_i]  
                    for root_i,dir_i,files_i in os.walk(dir_path) 
                        if(files_i)]
    filepaths=list(itertools.chain.from_iterable(filepaths))
    return [from_csv(file_i) for file_i in filepaths]

def from_csv(in_path):
    with open(in_path) as f:
         lines = f.readlines()
    lines=[line_i.strip().split(',') for line_i in lines]     
    names,data= lines[0],lines[1:]
    dicts=[{ name_j:data_j 
    	        for name_j,data_j in zip(names,line_i)}
    	            for line_i in data]
    data_id=in_path.split("/")[-1]
    return data_id,dicts

def get_postfix(filename):
    return filename.split(".")[-1]	

print(clf_result("result"))