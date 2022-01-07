
def compact(lst):
    return list(filter(bool, lst))

print(compact([0,1,False, 2,'word',False,3,"a",36,True]))