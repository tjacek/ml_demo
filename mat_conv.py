import os,os.path
import scipy.io
import numpy as np

def read_mat(in_path,out_path):
    if(not os.path.isdir(out_path)):
        os.mkdir(out_path)
    for name_i in os.listdir(in_path):
        in_i=in_path+'/'+name_i
        out_i=out_path+'/'+name_i
        mat_i=scipy.io.loadmat(in_i)['d_iner']
        np.savetxt(out_i,mat_i)
    #print( type( data[0]))
    #print(data[0].shape)

read_mat("Inertial",'inert_seqs')