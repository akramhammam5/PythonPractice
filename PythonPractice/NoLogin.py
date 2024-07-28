#Using Dictionary
users = {}

username = input("Enter Your Username: ")
password = input("Enter Your password: ")

secure = len(password) * "*"

users.update({username: secure})



print(users)

#Using Lists
'''
users = [] 
username = input("Enter Your Username: ")
password = input("Enter Your password: ")

secure = len(password) * "*"

users.append(username)
users.append(secure)




print(users)
'''