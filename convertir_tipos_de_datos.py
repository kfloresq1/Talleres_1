Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Convertir tipos de datos#
>>> x=3
>>> print("The value of x is " + x)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print("The value of x is " + x)
TypeError: can only concatenate str (not "int") to str
>>> print("The value of x is " + str(x))
The value of x is 3
>>> type(x)
<class 'int'>
>>> x=str(x)
>>> type(x)
<class 'str'>
>>> 
>>> 
>>> 
>>> 
>>> pi = 22/7
>>> print(pi)
3.142857142857143
>>> print("{:.2f}".format(pi))
3.14
>>> 
