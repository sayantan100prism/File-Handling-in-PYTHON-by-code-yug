'''file object variables in python, these are the variables that are used to store the file object in python'''
file = open("age.txt", "r+", buffering=10, encoding='utf-8', errors='ignore', newline='\n')
# print(file)
print("file name is :",file.name)
print("file mode is :",file.mode)
print("file encoding is :",file.encoding)
print("file closed is :",file.closed)
print("file newline is :",file.newlines)
print("file error is :",file.errors)
print("file buffer is :",file.buffer)
print("file fileno is :",file.fileno())
print("file isatty is :",file.isatty())
print("file seekable is :",file.seekable())
print("file writable is :",file.writable())
print("file readable is :",file.readable())
print("file tell is :",file.tell())
print("file truncate is :",file.truncate())
'''for "file.truncate()" The error io.UnsupportedOperation: truncate occurs 
because the file is opened in read mode ("r"), and the truncate() method 
is not supported in this mode. To fix this, you need to open the 
file in a mode that allows writing, such as "r+" (read and write).'''
print("file seek is :",file.seek(0))
print("file read is :",file.read())
print("file readline is :",file.readline())
print("file write is :",file.write("Hello"))
print("file flush is :",file.flush())
print("file close is :",file.close())
print("file closed is :",file.closed)