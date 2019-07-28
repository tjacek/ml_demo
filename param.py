import os,re

def convert_dataset(in_path,out_path):
    if(not os.path.isdir(out_path)):
        os.mkdir(out_path)
    if(os.path.isfile(in_path)):
        to_txt(from_txt(in_path),out_path)
    else:
        paths=os.listdir(in_path)
        for path_i in paths:
            in_i=in_path+'/'+path_i
            out_i=out_path+'/'+path_i
            to_txt(from_txt(in_i),out_i)

def to_txt(ts_dict,out_path):
    lines=[make_line(name_i,data_i) 
            for name_i,data_i in ts_dict.items()]
#                if( filtr(name_i))]	
    full_txt='\n'.join(lines)
    f=open(out_path,'w')
    f.write(full_txt)
    f.close()

def make_line(name_i,data_i):
    raw=re.findall('\d+',name_i)
    return data_i+"#" +name_i
#def make_line(name_i,data_i):
#    raw=re.findall('\d+',name_i)
#    return "#".join([data_i,raw[0],raw[1],name_i])

#def filtr(name_i):
#    print(name_i)
#    return len(name_i.split('_')[3])==0

def from_txt(in_path):
    with open(in_path) as f:
         lines = f.readlines()
    lines=[line_i.replace(" ","") for line_i in lines]
    dict_i= dict([parse_line(line_i) for line_i in lines])
    return dict_i

def parse_line(line_i):
    raw_i=line_i.split('#')
    return raw_i[-1].strip(),raw_i[0]

#ts_dict=from_txt('conv_agum.txt')
#to_txt(ts_dict,'conv_agum')
convert_dataset('deep','deep_out')