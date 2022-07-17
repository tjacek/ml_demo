import pandas
import os,re

def to_latex(in_path,out_path):
    if(os.path.isdir(in_path)):
        if(not os.path.isdir(out_path)):
            os.mkdir(out_path)
        for path_i in os.listdir(in_path):
            in_i=f"{in_path}/{path_i}"
            out_i=f"{out_path}/{path_i}"
            to_latex(in_i,out_i)
    else:
        out_path=out_path.replace("csv","txt")
        df_i=pandas.read_csv(in_path)
        file_i = open(out_path,'w')
        file_i.write(from_df(df_i))
        file_i.close()

def from_df(df_i):
    lines=[]
    latex="\\begin{tabular}{|"
    for t in range(df_i.shape[1]):
        latex+="c|"
    latex+="}\n"
    def helper(row_j):
        row_j=[str(elem) for elem in row_j.to_list()]
        line_j=" & ".join(row_j)
        return f"\\hline {line_j}\\\\ \n" 
    latex+=helper(df_i.columns)
    for index, row_j  in df_i.iterrows():
        latex+=helper(row_j)
    latex+=" \\hline \n \\end{tabular} "
    print(latex)
    return latex

def to_biblo(in_path):
    ws = re.compile(r"\s+")
    lines =[line_j
       for line_j in open(in_path, "r").readlines()
           if(not ws.match(line_j))]
    print(lines)

to_latex("tab.csv","tab.latex")