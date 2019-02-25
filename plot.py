import numpy as np
import random
import os.path
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

def show_features(in_path,title="handcrafted features"):
    X,y=read_datasets(in_path)
    X=TSNE(n_components=2,perplexity=30).fit_transform(X)
    color_helper=make_cat_helper(y)
    plot(X,y,color_helper,title)

def read_datasets(in_path):
    if(os.path.isfile(in_path)):
        text = open(in_path, "r").read()
        return parse_dataset(text)
    else:
        all_paths=os.listdir(in_path)
        all_paths=[ in_path+'/'+path_i for path_i in all_paths]
        all_texts=[ open(path_i, "r").read() for path_i in all_paths]
        all_tuples=[parse_dataset(text_i) for text_i in all_texts]
        y=all_tuples[0][1]
        x=[x_i for x_i,y_i in all_tuples]
        return np.concatenate(x,axis=1),y

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
    return np.array(X),y

def read_file(in_path):
    if(os.path.isfile(fname)):
        f = open(in_path, "r")
    return f.read() 

def plot(X,y,color_helper,title=None):
    X=norm_x(X)
    n_points=X.shape[0]
    plt.figure()
    ax = plt.subplot(111)
    for i in range(n_points):
        color_i= color_helper(y[i])
        plt.text(X[i, 0], X[i, 1], str(y[i]),
                   color=plt.cm.tab20( color_i),
                   fontdict={'weight': 'bold', 'size': 9})
    plt.xticks([0.0,0.5]), plt.yticks([])
    steps=[0.1*i for i in range(11)]
    plt.xticks(steps), plt.yticks(steps)
    if title is not None:
        plt.title(title)
    plt.show()

def norm_x(X):
    x_min, x_max = np.min(X, 0), np.max(X, 0)
    return (X - x_min) / (x_max - x_min)

def make_cat_helper(y):
    cats=np.unique(y)
    random.shuffle(cats)
    def color_helper(y_i):
        return  float(cats[y_i-1])/float(cats.shape[0])
    return color_helper


show_features("msr_handcrafted",title="MSR - all handcrafted features")
show_features("msr_handcrafted/I.txt",title="MSR - Statistical Temporal Features")
show_features("mhad_handcrafted",title="MHAD - all handcrafted features")
show_features("mhad_handcrafted/I.txt",title="MHAD - Statistical Temporal Features")