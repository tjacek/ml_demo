import pandas
import os

def to_latex(in_path,out_path):
    if(not os.path.isdir(out_path)):
        os.mkdir(out_path)
    for path_i in os.listdir(in_path):
        in_i=f"{in_path}/{path_i}"
        out_i=f"{out_path}/{path_i}"
        out_i=out_i.replace("csv","txt")
        df_i=pandas.read_csv(in_i)
        file_i = open(out_i,'w')
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
    return latex

to_latex("data","latex")