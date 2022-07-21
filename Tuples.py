Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t= (2,4,6)
type(t)
<class 'tuple'>
t[0] = "me"
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t[0] = "me"
TypeError: 'tuple' object does not support item assignment
# Tuples are immutable
