from icecream import ic

alist = ["brad!!", "steve12", "amanda82", "whocares?"]

for i in range(0,len(alist)):
    people = [char for char in alist[i] if not char.isdigit()]
    people = "".join(people)
    alist[i] = people
    ic(people)
    people = [char for char in alist[i] if char.isalnum()]
    people = "".join(people)
    alist[i] = people
print(alist)