import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

def show_confusion(in_path):
    cf_matrix=np.genfromtxt(in_path,delimiter=',')
    dim=cf_matrix.shape
    df_cm = pd.DataFrame(cf_matrix, range(dim[0]),range(dim[1]))
    sn.set(font_scale=1.0)#for label size
    sn.heatmap(df_cm, annot=True,annot_kws={"size": 8}, fmt='g')
    plt.show()

show_confusion("msr.csv")
show_confusion("mhad.csv")
