import numpy as np

def load_data(filename):
    #Read subject names and count
    with open(filename,'r',encoding='utf-8') as f:
        header = f.readline().strip().split(',')
        subjects = header[1:]
        no_of_subs = len(subjects)
    data = np.genfromtxt(filename,delimiter=',', dtype=str, encoding='utf-8', skip_header=1)
    names = data[:, 0]
    marks = data[:, 1:].astype(int)
  
    return names,marks,no_of_subs,subjects