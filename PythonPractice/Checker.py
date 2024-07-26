username = input('Username: ')
password = input('Password: ')


length = len(password)

Hidden_Pass = '*' * length

print("\n")
print(f"Hi! {username} Your password {Hidden_Pass} is {length} characters long")
