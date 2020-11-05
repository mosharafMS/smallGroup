from typing import List
import numpy as np
import pickle as pk
import numpy
import os

from numpy.core.defchararray import replace
from numpy.core.fromnumeric import shape

def main():
    #check for saved files
    pickle_file="smallGroup.pickle"
    keep_saved='n'
    if os.path.isfile(pickle_file):
        big_array=pk.load(open(pickle_file,mode="rb"))
        print("Found saved list from last run")
        print("The list is \n",big_array)
        keep_saved=input("Do you want to keep this list or add a new list? (type y or n)  \n")

    if keep_saved=='n':
        big_array=get_input()
    
    
    happy='n'
    while happy=='n':
        team_size=input("What is the size of the group?\n")
        team_size=int(team_size)
        result=split_groups(big_array,team_size)
        print("Dividing into ",result.shape[0], " groups")
        print(result)
        happy=input("Are you happy with the distribution? (type y or n)\n")

    confirm_save=input("Do you want to save the list for future shuffling? (type y or n)\n")

    if confirm_save:
        pk.dump(big_array,open(pickle_file,mode="wb"))

def split_groups(origninal_array,group_size):
    number_of_groups=np.math.ceil(origninal_array.shape[0]/group_size)
    print("Number of groups: ",number_of_groups)
    vec_len=np.vectorize(len)
    max_name_len=np.max(vec_len(origninal_array))
    array_dtype="S"+str(max_name_len) #choose the result array datatype based on the max length
    result=np.full(shape=(number_of_groups,group_size),fill_value="EMPTY",dtype=array_dtype)

    tmp_array=origninal_array
    for i in range(number_of_groups):
        if tmp_array.shape[0] <= group_size:
            result[i,:tmp_array.shape[0]]=tmp_array #the remaining if lower than the group size
            return result
        group=np.random.choice(tmp_array,group_size,replace=False)
        result[i]=group
        for g in group:
            tmp_array=np.delete(tmp_array,np.where(tmp_array==g))
    return result

def get_input():
    strList=input("Enter the names of the list separated by comma:\n")
    myList=strList.split(',')
    npArray=np.array(myList)
    return npArray



def check_unique():
    pass

if __name__ == "__main__":
    main()