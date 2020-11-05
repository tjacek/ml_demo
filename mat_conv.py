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
        np.savetxt(out_i,mat_i,delimiter=",")
    #print( type( data[0]))
    #print(data[0].shape)

def save_mat(in_path,out_path):
	if(not os.path.isdir(out_path)):
		os.mkdir(out_path)
	for name_i in os.listdir(in_path):
		in_i="%s/%s" % (in_path,name_i)
		out_i="%s/%s" % (out_path,name_i)
		print(out_i)
		print(in_i)
		cf_i=np.genfromtxt(in_i,delimiter=',')
		cf_i={"cf":cf_i}
		scipy.io.savemat(out_i,cf_i)

save_mat("cf",'mat')