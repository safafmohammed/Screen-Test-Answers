keys = [1,2,3,4,5,6,7,8,9]
print("keys:",keys)
inputlist = []
for i in range(0, 11):
    n=i+1
    item = int(input("Enter element %d:" % n))
    inputlist.append(item)
print("input list:",inputlist)

count=[]
for i in keys:
    c = 0
    for j in inputlist:
        if j%i==0:
            c+=1
    count.append(c)
dictionary = dict(zip(keys, count))
print("dictionary:",dictionary)


