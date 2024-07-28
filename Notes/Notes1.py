


print(3 + 4)
print(4 - 3)
print(3 * 4)
print(type(3 / 3)) #flaoting-point output 
print(10 // 4)

#Math Functions
print(round(3.6))
print(abs(-3.6))

#operaters precedence

#Strings
long_string = '''
I am  typing a full 
<p>Paqragraph</p> 
using python
'''
print(long_string)

#Type Conversion

str1 = str(50) 
intt = int(str1)
result = type(intt)
# Same as type(int(str(50)))

print(f'{result}\n')

#Formatted String

Name = 'Johnny'
Age = 45

print('Hi {New_Name}. You are {New_Age} years old\n'.format(New_Name = 'Ziad' , New_Age = '40'))

print(f'Hi {Name}. You are {Age} years old\n') #Cleaner way of doing it

#String Indexes

VAR = "stepOver" #Strings are immutable thus we cannot directly access and modify its contents
print(VAR.upper())
print(VAR.capitalize())

#print(VAR[0:8:2])
print(VAR.replace('step', 'Jump'))
print(VAR[0:len(VAR)])

print(bool()) # If anything exists except 0 then Ture and Vice Versa

#Lists
list1 = [1, 2, 3, 4, 5]
list2 = ['akram', 'b', 'c']
list3 = [1, 2, 'a', True] #Mixed data types

list2[0] = "ziad"
print(list1[2])
print(list2[0::2])
list1[3] = 1 #Lists are mutable

'''You didn't copy the list but you just pointed to the same list'''
#testlist = list2 #Both list1 and testlist are pointing to the same memory location

#testlist[0] = 'Hamed'
#print(testlist)
#print(list2)

testlist = list2[:] #Copied the list 

testlist[0] = 'Hamed'
print(testlist)
print(list2)

#Matrix
matrix = [
  [1,2,3],
  ['a','b','c'],
  ['akram','ziad','Joo'],
]
new = matrix.append(100)
print(len(matrix))
print(matrix)
print(new) #None as append() change in assigned place only 
matrix.insert(1,200) #Insert also modifies the list in place only
print(matrix)
matrix.pop() #pops out the end of the list 
matrix.pop(0) #pops item at index
print(matrix)
matrix.remove(200)
print(matrix)
print('a' in matrix[0])

'''
Different methods do different things for example pop() removes the last item but remove() removes the item at index, also pop() returns the value that it removed in case it is assigned to a variable 
'''

basket = ['Bannana', 'Apples', 'Oranges', 'Blueberries']
basket[::-1]
print(basket[::-1]) #Another way to reverse Data like reverse()
print(list(range(50+1)))
print('\n')
scentence = ' '
avr = scentence.join(['Yo!','How','are','You?']) #Join creates a new item so it should be assigned to a var
print(avr)

a,b,c, *other, d = [1,2,3,4,5,6,7,8,9] #Each var has a value, *other is a list of all the remaining values and d is the last value 

print(a)
print(d)
print(other)

#Dictionaries
dictionary = {
  'Key': True,
  'Key2': ['a','b','c'],
  'Key3': 'String',
  (1,2,3): 'Anything'
} #Boolean keywords can be used as keys

listd = [
  {
    'Key': True,
    'Key2': ['a','b','c'],
    'Key3': 'String'
  },
  {
    'T': False,
    'T2': ['d','e','f'],
    'T3': 'Test',
    (1,2,3): 'Surprise?!'
  }
]

print(dictionary[(1,2,3)]) #When large it can be unordered 

#Dictionary Methods
print(listd[0]['Key2'][1])
print(listd[0:1:2])
print(dictionary.get('tedel', 65)) #Assigned it a default value if it doesn't exist

user = dict(name='Zeplex')

dic = dictionary.copy()

print(dictionary.items())
print('\n')
print(dic)
dictionary.clear()
dic.pop('Key') #returns the deleted key value
print(dic)
dic.popitem() #pops out the last item in the latest python version
print(dic.update({'Key2':'onlyme'}))# None returned as it only update it without memory usage
print(dic.items())

#Tuples (Immutable)
MyTuple = (1,2,3,4,5,5,5,5,5) #Less flexible than List but more performant
print(MyTuple[4])
print(MyTuple[0:3])
print(5 in MyTuple)

a,b,c,*other,d = (1,2,3,4,5,6,7,8,9)

print(MyTuple.count(5)) #Counts the number of occurences of the value
print(MyTuple.index(4)) #Returns the index of the value
print(len(MyTuple)) #Length

#Sets
MySet = {1,2,3,4,5,5,5} #Duplications doesn't get printed 
print(MySet)
MySet.add(100)
print(MySet) #Set are all in one memory location

Listt = [1,2,3,3]
print(set(Listt)) #Sets doesn't support indexing
print(len(MySet)) #Doesn't count duplicates
newset = MySet.copy()

