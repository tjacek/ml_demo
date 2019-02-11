import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

def show_features(in_path):
    text=read_file(in_path)
    X,y=parse_dataset(text)
    X=TSNE(n_components=2,perplexity=30).fit_transform(X)
    plot(X,y)

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
    f = open(in_path, "r")
    return f.read() 

def plot(X,y):
    X=norm_x(X)
    n_points=X.shape[0]
    ax = plt.subplot(111)
    for i in range(n_points):
        color_i= 3#color_helper(i,y[i])
        plt.text(X[i, 0], X[i, 1], str(y[i]),
                   color=plt.cm.tab20( color_i),
                   fontdict={'weight': 'bold', 'size': 9})
    plt.xticks([]), plt.yticks([])
#    if title is not None:
#        plt.title(title)
    plt.show()

def norm_x(X):
    x_min, x_max = np.min(X, 0), np.max(X, 0)
    return (X - x_min) / (x_max - x_min)

show_features("MVC/mhad/conv_agum.txt")