'''
file = open("filename", "mode"='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

buffering: An optional integer used to set the buffering policy. 
Pass 0 to switch buffering off (only allowed in binary mode), 1 to select line buffering 
(only usable in text mode), and an integer > 1 to indicate the size of a fixed-size chunk buffer.
deault size is : 4096 - 8192 bytes

used to divide large files into small chunks, and store them in the buffermemory.

encoding: The name of the encoding used to decode or encode the file.should be used in text mode only.
depends on OS, for windows: cp1252, for linux: utf-8, for mac: utf-8

errors: An optional string that specifies how encoding and decoding errors are to be handled.
The default is 'strict' meaning that encoding errors raise a UnicodeError.
Other possible values are 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 
and any other name registered via codecs.register_error().

newline: Controls how universal newlines mode works (it only applies to text mode).
It can be None, '', '\n', '\r', and '\r\n'. It works as follows:
- None: Read files with any newline convention and write files with your platform's convention.
- '': Read files with any newline convention and write files with '\n'.
- '\n': Read files with '\n' and write files with '\n'.
- '\r': Read files with '\r' and write files with '\n'.
- '\r\n': Read files with '\r\n' and write files with '\n'.

'''

file = open("age.txt", "r", buffering=10, encoding='utf-8', errors='ignore', newline='\n')
if file:
    print("File opened successfully")
else:
    print("File not opened")
print(file)
