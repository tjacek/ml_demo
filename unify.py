import os
from shutil import copyfile

def unify_dict(in_path1,in_path2,out_path):
    if(not os.path.isdir(out_path)):
        os.mkdir(out_path)
    all_paths=read_file(in_path1)+read_file(in_path2)
    for i,path_i in enumerate(all_paths):
        out_i=out_path+'/'+path_i.split('/')[-1]
        out_i+=str(i)
        copyfile(path_i,out_i)

def read_file(in_path):
    return [ os.path.join(in_path,name_i) 
                for name_i in os.listdir(in_path)]

dataset="MSR"
in_path1="../votes/"+dataset+"/SVC"
in_path2="../votes/"+dataset+"/LR"
out_path="../votes/"+dataset+"/full"
unify_dict(in_path1,in_path2,out_path)