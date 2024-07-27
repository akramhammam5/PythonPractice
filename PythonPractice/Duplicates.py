#Check For Duplicates in List:

My_List = ['a','b','c','b','d','m','n','n'] 
Check_List = []
for i in My_List:
   if My_List.count(i) > 1:
     if i not in Check_List:
       Check_List.append(i)
   else:
     pass

print(Check_List)
