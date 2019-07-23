def to_txt(ts_dict,out_path):
    lines=[make_line(name_i,data_i) 
            for name_i,data_i in ts_dict.items()]	
    full_txt='\n'.join(lines)
    f=open(out_path,'w')
    f.write(full_txt)
    f.close()

def make_line(name_i,data_i):
    raw=name_i.split('_')
    return "#".join([data_i,raw[0],raw[1],name_i])

def from_txt(in_path):
    with open(in_path) as f:
         lines = f.readlines()
    lines=[line_i.replace(" ","") for line_i in lines]
    return dict([parse_line(line_i) for line_i in lines])

def parse_line(line_i):
    raw_i=line_i.split('#')
    return raw_i[1].strip(),raw_i[0]



ts_dict=from_txt('conv_person.txt')
to_txt(ts_dict,'out')