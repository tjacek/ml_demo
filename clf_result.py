import os,os.path
import itertools
from collections import defaultdict
from sets import Set

def filter_csv(in_path,out_path,oblig_set):
    oblig_set=Set(oblig_set)
    def has_common(line_i):
        feat_desc_i=line_i[0].strip().split("+")
        feat_desc_i=Set(feat_desc_i)
        return len(oblig_set.intersection(feat_desc_i))!=0
    data_id,names,data=from_csv(in_path)
    filtered=[line_i for line_i in data
                if(has_common(line_i))]
    f=open(out_path,'w')
    f.write(to_csv(filtered,names))
    f.close()

def clf_result(in_path,out_path):
    name_dict={}
    data_dict=defaultdict(list)
    for id_i,name_i,data_i in read_results(in_path):
        name_dict[id_i]=name_i
        data_dict[id_i].append(data_i)
    result={ name_i:   list(itertools.chain.from_iterable(value_i)) 
                for name_i,value_i in data_dict.items()}
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
    data_id=in_path.split("/")[-1]
    return data_id,names,data

def to_csv( dicts,names):
    lines=[",".join(names)]
    lines+=[ ",".join(dict_i)
                for dict_i in dicts]
    return "\n".join(lines)

def get_postfix(filename):
    return filename.split(".")[-1]	

def make_dir(path):
    if(not os.path.isdir(path)):
        os.mkdir(path)

#clf_result("result","out")
filter_csv("raw/inert_mhad_LR.csv",'result/inert_mhad_LR.csv',
            oblig_set=['inert'])