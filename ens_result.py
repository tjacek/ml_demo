def to_csv(in_path,out_path):
    with open(in_path) as f:
         lines = f.readlines()
    lines=[line_i.strip() for line_i in lines]
    lines=list(dict.fromkeys(lines))
    size= int(len(lines)/2)
    rows=[]
    for i in range(size):
        desc=lines[2*i]
        result=lines[2*i+1]
        desc=desc.split("/")
        feats=desc[-1].split("_")
        new_line=[desc[-2]]+feats
        new_line.append(result)
        rows.append(",".join(new_line))
    save(rows,out_path)

def save(rows,out_path):
    csv_txt="\n".join(rows)
    f=open(out_path,'w')
    f.write(csv_txt)
    f.close()


to_csv("LR.txt","LR.csv")