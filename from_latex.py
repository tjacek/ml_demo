def to_csv(in_path):
    with open(in_path) as f:
        lines=f.readlines()
        new_lines=[]
        for line_i in lines:
            line_i=line_i.replace("\\hline","")
            line_i=line_i.replace("\\","").strip()
            line_i= ",".join(line_i.split("&"))
            print(line_i) 

to_csv('tab2')