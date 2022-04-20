import pandas
import os

def to_latex(in_path):
    paths=[f"{in_path}/{path_i}"
        for path_i in os.listdir(in_path)]
    for path_i in paths:
        df_i=pandas.read_csv(path_i)
        from_df(df_i)

def from_df(df_i):
    lines=[]
    print(dir(df_i))
    latex="\\begin{tabular}{|"
    for t in range(df_i.shape[1]):
        latex+="c|"
    latex+="}\n"
    
    for index, row_j  in df_i.iterrows():
        row_j=[str(elem) for elem in row_j.to_list()]
        line_j=" & ".join(row_j)
        latex+=f"\\hline {line_j}\\\\ \n" 
    latex+=" \\hline \n \\end{tabular} "
    print(latex)

to_latex("data")