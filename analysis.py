import numpy as np


def topper(percentage):
    return np.argmax(percentage)

def subject_topper(marks):
    return np.argmax(marks, axis = 0)

def report(names,total,percentage,grade,index=None):
    if index==None:
        print("---------Student Report----------")
        for i in range(len(names)):
            print(f"{names[i]} - \nTotal ={total[i]} \nPercentage = {percentage[i]} \nGrade = {grade[i]}\n\n")

    elif 0 <= index < len(names):
         print(f"{names[index]} - \nTotal ={total[index]} \nPercentage = {percentage[index]} \nGrade = {grade[index]}\n\n")
    
    else:
        print("Invalid index")

def rank_students(names,percentage,n):
  
    sorted_indices = np.argsort(percentage)[::-1]
    ranked_list = [
            (rank + 1,names[i],round(percentage[i],2))
                for rank,i in enumerate(sorted_indices[:n])
                   ]
    return ranked_list
    