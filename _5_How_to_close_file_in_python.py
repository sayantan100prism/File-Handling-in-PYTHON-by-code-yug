'''close() method is used to close the file. If we don't close the file,
 the data will not be stored in the file. 
 If we don't close the file, the data will be stored in the buffer memory and
  will be lost if the program crashes.
  
  otherwise python garbage collector will close the file automatically, but only after execution of the program. 
  but it is not recommended to rely on garbage collector.as in the case of large files, 
  it may take time to close the file, which may cause
  1)Data may get corrupted.
  2)memory wastage will happen.'''
