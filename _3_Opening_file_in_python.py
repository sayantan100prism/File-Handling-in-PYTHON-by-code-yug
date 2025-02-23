'''Python provides a built-in open function to open a file.
 This function returns a file object, also called a handle, as it is used to read or modify the file accordingly.
   
   file = open("filename", "mode"='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

   The open function returns a file object, which has methods and attributes for getting information about and manipulating the file. 
The file object is iterable, so you can use it in a for loop to iterate over the lines of the file.
The file object is also a context manager, so you can use it in a with block to ensure that the file is properly closed after its suite finishes,
even if an exception is raised on the way.'''

