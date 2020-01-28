list1=[4,6,2,7,4,8,9]
list2=[6,5,8,7,9,5,5]
list3=[]

lstelm1=list1[4:]
print(lstelm1)

lstelm2=list2[4:]
print(lstelm2)

list3.extend(lstelm1)
list3.extend(lstelm2)

print(list3)



