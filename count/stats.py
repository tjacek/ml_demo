import os

def top_files(path):
    return [ f'{path}/{file_i}'
          for file_i in os.listdir(path)]

def count_frames(in_path):
    seq_len=[len(top_files(path_i)) 
	            for path_i in top_files(in_path)]
    print(f'All frames:{sum(seq_len)}')
    print(f'Max seq:{max(seq_len)}')

in_path='../../2021_II/3DHOI'
count_frames(in_path)