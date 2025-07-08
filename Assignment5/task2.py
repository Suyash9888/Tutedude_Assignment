list=[]
for x in range(1,11):
    list.append(x)
print(f"Original list :{list}")
list1=list[:5]
print(f"Extracted first five elements :{list1}")
list1.reverse()
print(f"Reversed extracted elements :{list1}")
