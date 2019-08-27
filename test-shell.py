#!/usr/bin/python3

import os
myCmd = 'sudo ls -la'

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Shell script - list the contents of the curren folder</title>")
print("</head>")
print("<body>")
print("<div>")
os.system(myCmd)
print("test") 
print("</div>")
print("</body>")
print("</html>")
