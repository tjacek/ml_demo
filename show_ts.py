import re,os
import matplotlib.pyplot as plt
import numpy as np

def group_show_ts(in_path,out_path):
    if(not os.path.isdir(out_path)):
        os.mkdir(out_path)
    all_paths=os.listdir(in_path)
    txt_paths=[ path_i for path_i in all_paths
                if( path_i.split(".")[-1]=="txt")]
    #png_paths=[ txt_i.replace(".txt",".png") for txt_i in txt_paths]
    #def paths_helper(txt):
    #    in_i=in_path+'/'+txt_i
    #    out_i=out_path+'/'+txt_i
    #    out_i=out_i.replace(".txt",".png")
    #    return in_i,out_i
    all_paths= [ (in_path+'/'+txt_i,out_path+'/'+txt_i) 
                    for txt_i in txt_paths] 
    for in_i,out_i in all_paths:
        basic_show_ts(in_i,out_i)

def basic_show_ts(in_path,out_path):
    with open(in_path) as f:
         lines = f.readlines()
    header,lines=get_header(lines)
    y=np.array([get_number(line_i)  for line_i in lines])
    x=np.arange(y.shape[0])
    plt.title(header)
    plt.xlabel("Number of iterations")
    plt.ylabel("Loss function value")
    plt.plot(x,y)
    out_path=out_path.split(".")[0]+".png"
    plt.savefig(out_path)
    plt.close()

def get_header(all_lines,str_id="Iter"):
    header,lines=[],[]
    for line_i in all_lines:
    	line_i=line_i.strip()
        if(str_id in line_i):
            lines.append(line_i)
        else:
            header.append(line_i)
    header=[h_i for h_i in header
                if(h_i)]
    print(header)
    return "\n".join(header),lines

def get_number(text):
    raw_number=re.findall("\d+\.\d+", text)
    return float(raw_number[0])

def bottom_files(path):
    all_paths=[]
    for root, directories, filenames in os.walk(path):
    	all_paths.append()


group_show_ts("lorenz","test")
