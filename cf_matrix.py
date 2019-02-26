import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

def show_confusion(in_path,labels=None):       	
    cf_matrix=np.genfromtxt(in_path,delimiter=',')
    dim=cf_matrix.shape
    if(not labels):
        labels=range(dim[0])
    df_cm = pd.DataFrame(cf_matrix, labels,labels)
    sn.set(font_scale=0.7)#for label size
    sn.heatmap(df_cm, #xticklabels=,yticklabels=df_cm.columns,
    	annot=True,annot_kws={"size": 4}, fmt='g')
    plt.yticks(rotation=0) 
    plt.xticks(rotation=90)
    plt.show()

cats_msr=['high arm wave','horizontal arm wave','hammer','hand catch','forward punch',
          'high throw','draw x','draw tick','draw circle','hand clap',
          'two hand wave','side-boxing','bend','forward kick','side kick',
          'jogging','tennis swing','tennis serve','golfswing','pick up & throw']

cats_mhad=['right arm swipe to the left', 'right arm swipe to the right', 'right hand wave','two hand front clap','right arm throw',
 'cross arms in the chest','basketball shoot','right hand draw x', 'draw circle (clockwise)','draw circle (counter clockwise)', 
 'draw triangle','bowling', 'front boxing', 'baseball swing from right', 'tennis right hand forehand swing','arm curl', 
 'tennis serve', 'two hand push', 'right hand knock on door', 'right hand catch an object', 'right hand pick up and throw', 'jogging in place', 
 'walking in place', 'sit to stand', 'stand to sit','forward lunge','squat']

show_confusion("msr.csv",cats_msr)
show_confusion("mhad.csv",cats_mhad)
