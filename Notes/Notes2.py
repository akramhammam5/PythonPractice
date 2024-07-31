#Truthy and Falsy
bool(5) #Considered truthy as the value is True
bool('') #Considered Falsy as the value is False

#Ternary Operators
Granted = True
Output = "Access Granted!" if Granted else "Access Denied"
#print(Output)

#Short Circuiting
is_Friend = True
is_Blocked = False
if is_Friend or is_Blocked:
  print("Best Friends\n")

#Logical Operators (> | < | == | >= | <= | != | and | or | not)
print(not(True) or True)
print(1<2<3<4)

#Loops
'''for item in [1,2,3,4,5]:
  print(item)'''

#iterables - list, dictionary, tuple, set, string
#iterated -> one by one check each item in the collection
'''user = {
  'name': 'Name',
  'age': 'Age',
  'can_swim': False
}
for key,value in user.items(): #adding .items will print the whole dictionary and adding nothign will print the keys
  print(key,value)
'''

#Range()
'''print(range(50))
for i in range(10,0,-2):
  print(i) #Reverse looping 
'''

#enumrate
for i,char in enumerate(list(range(100))): #It can also be list or tuple
  if (char == 50):
    print(f'The index of 50 is {i}')
  else:
    pass

#While Loops
i = 1
while 51<50+1: #Skipps the loop as the condition is false
  print(i)
  i+=1
else:
  print("Work Done!")

#Break(stops the code in a specific point) , Continue, Pass
i = 1
while i < 10:
  print(i)
  i+=1
  continue #pass does nothing 
  #Anyline Here is skipped as the continue is used

#Functions (A function should do only 1 thing really well)
def say_hello():
  print("Hello")

say_hello()
print(say_hello) #Returns The Memory Location 

#Parameters and Arguments
def Para(name,emoji): #Parameters for definition
  print(f'Hi! {name} {emoji}')

Para('Mike','Laughing') #Passed 2 arguments for calling

#Default Parameters
Para(emoji = 'Laughing', name = 'Mike') #Bad Practice as it makes the code seems complicated 

#Using return
def sum(Num1,Num2):
  '''
  Info: This function returns the sum of the two numbers
  '''
  def another(N1,N2):
    return N1+N2
  return another(Num1,Num2) #Very Confusing Function :(
  #Any line here will not be executed because the function exits after returining the value
total = sum(5,2)
print(total) #Used print as it returns a value

#Methos vs Functions

#Functons are defined using def and coded for a specific task
  #list()
  #dict()

#Methods are defined using . and coded for a specific task (Have to be owned by something)
  #.count()
  #.append()

#Docstrings: Added inside functions when stopping cursor inside the brackets to define its arguments or actions
#help(sum)

# *args and **kwargs
def fun(name, *args, age=0, **kwargs): # *Args store any number of positional arguments as a tuple and **kwargs store any number of key value pairs as a dictionary
  return args

print(fun(1,2,3,4,5, num1 = 5, num2 = 10))

#Rule when using: params --> *args --> Default Params --> **kwargs

#Walrus Operator (From Python 3.8)
a = 'helooooooooo'

if n := (len(a)) > 10:
  print(f'Too long {len(a)} elements') #I just calculated length twice 
  print(f'Too long {n} elements') #Better Version

#Scope - What variables do I have access to?


'''def example():
  total = 100 (Local Scope)
  print(total)
print(total) (Error as total is not defined outside the function)
'''
def parent():
  def example():
    return sum
  return example()
print(parent())

#1 - Start with local
#2 - Parent local?
#3 - Global
#4 - Built in Python Functions
print(10 > 9)
