Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
len("what am I doing")
15
my_list= [2,4,5,1,9]
len(my_list)
5
my_list[2:]
[5, 1, 9]
mylist= [4,8,7,9]
my_list + mylist
[2, 4, 5, 1, 9, 4, 8, 7, 9]
new = my_list + mylist
new
[2, 4, 5, 1, 9, 4, 8, 7, 9]
new[1] = 'four'
new
[2, 'four', 5, 1, 9, 4, 8, 7, 9]
my_list.append("ten")
my_list
[2, 4, 5, 1, 9, 'ten']
# this is the basic things you can do with lists.
my_list.pop()
'ten'
my_list
[2, 4, 5, 1, 9]
Popped_item = my_list.pop()
Popped_item
9
# Popping is -1 of list
new
[2, 'four', 5, 1, 9, 4, 8, 7, 9]
new.sort()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    new.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
new[1] = 4
new
[2, 4, 5, 1, 9, 4, 8, 7, 9]
new.sort()
new
[1, 2, 4, 4, 5, 7, 8, 9, 9]
my_list[2:]
[5, 1]


