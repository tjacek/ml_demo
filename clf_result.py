import os,os.path
import itertools
from collections import defaultdict

def clf_result(in_path,out_path):
    name_dict={}#defaultdict(list)
    data_dict=defaultdict(list)
    for id_i,name_i,data_i in read_results(in_path):
        name_dict[id_i]=name_i
        data_dict[id_i].append(data_i)
    result={ name_i:   list(itertools.chain.from_iterable(value_i)) 
                for name_i,value_i in data_dict.items()}
    #print(result['mhad_LR.csv'])
    make_dir(out_path)
    for id_i,data_i in result.items():
        f=open(out_path+'/'+id_i,'w')
        f.write(to_csv(data_i,name_dict[id_i]))
        f.close()

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
    #dicts=[{ name_j:data_j 
    #	        for name_j,data_j in zip(names,line_i)}
    #	            for line_i in data]
    data_id=in_path.split("/")[-1]
    return data_id,names,data

def to_csv( dicts,names):
#    names=dicts[0].keys()
    lines=[",".join(names)]
    lines+=[ ",".join(dict_i)
                for dict_i in dicts]
    return "\n".join(lines)

def get_postfix(filename):
    return filename.split(".")[-1]	

def make_dir(path):
    if(not os.path.isdir(path)):
        os.mkdir(path)

clf_result("result","out")