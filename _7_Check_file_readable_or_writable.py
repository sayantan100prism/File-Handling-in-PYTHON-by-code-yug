'''file class in python, these are the variables that are used to store the file object in python.
readable() method is used to check whether the file is readable or not. true if the file is readable, false otherwise.
writable() method is used to check whether the file is writable or not. true if the file is writable, false otherwise.'''

file = open("age.txt", "r+")
print("file writable is :",file.writable())
print("file readable is :",file.readable())
file.close()
