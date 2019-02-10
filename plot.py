import numpy as np

def parse_dataset(text,num_sep=",",cat_sep="#"):
    lines=text.split("\n")
    X,y=[],[]
    for line_i in lines:
        line_i=line_i.split(cat_sep)
        data_i=np.array([float(cord_i) 
                            for cord_i in line_i[0].split(num_sep)])
        cat_i=int(line_i[1])
        X.append(data_i)
        y.append(cat_i)
    return X,y

def read_file(in_path):
    f = open(in_path, "r")
    return f.read() 

text=read_file("MVC/mhad/conv_agum.txt")
parse_dataset(text)