import pandas
import os,re
from functools import wraps


def dir_function(func):
    @wraps(func)
    def helper(in_path,out_path):
        if(os.path.isdir(in_path)):
            if(not os.path.isdir(out_path)):
                os.mkdir(out_path)
            for path_i in os.listdir(in_path):
                in_i=f"{in_path}/{path_i}"
                out_i=f"{out_path}/{path_i}"
                func(in_i,out_i)
        else:
            func(in_path,out_path)

def csv_function(func):
    @wraps(func)
    def helper(in_path,out_path):
        out_path=out_path.replace("csv","txt")
        df_i=pandas.read_csv(in_path)
        result_i=func(df_i)
        if(result_i):
            file_i = open(out_path,'w')
            file_i.write(result_i)
            file_i.close()     
        return result_i
    return helper

#@csv_function
def to_latex(df_i):
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

@csv_function
def acc(df):
    base=df['raw']
    voting=['borda', 'opv_acc', 'opv_auc', 'opv_f1']
    for vote_i in voting:
        df[vote_i]+=base
        df[vote_i]=df[vote_i].round(decimals=4) 
    return to_latex(df)

acc("tab2.csv","tab2.latex")