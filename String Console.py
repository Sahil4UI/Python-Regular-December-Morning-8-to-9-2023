Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#String - single character , word , line,paragraph , more than one paragraph
x = "WElcome to ESS Institute"
type(x)
<class 'str'>
x[0]
'W'
x[1]
'E'
x[2]
'l'
x[-1]
'e'
x[-5]
'i'
#slicing
x[0:6]
'WElcom'
#ending range - n-1
x[0:7]
'WElcome'
x[:12]
'WElcome to E'
x[5:]
'me to ESS Institute'
x[:]
'WElcome to ESS Institute'
x[0:15:1]
'WElcome to ESS '
x[0:15:2]
'Wloet S '
x[::-1]#reverse
'etutitsnI SSE ot emoclEW'
len(x)#length
24
x
'WElcome to ESS Institute'
x.count('e')
2
x.count('E')
2
x
'WElcome to ESS Institute'
x.lower()
'welcome to ess institute'
x.upper()
'WELCOME TO ESS INSTITUTE'
x.capitalize()
'Welcome to ess institute'
x.title()
'Welcome To Ess Institute'
x.swapcase()# caps - small , small - caps
'weLCOME TO ess iNSTITUTE'

x
'WElcome to ESS Institute'
x
'WElcome to ESS Institute'
>>> x.find("W")
0
>>> x.find("e")#first one
6
>>> x.rfind("e")
23
>>> x = "WElcome to Python Programming Class"
>>> x.find('o')
4
>>> x.find('o',5)
9
>>> x.index('o')
4
>>> x.index('X')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    x.index('X')
ValueError: substring not found
>>> x.find("X")
-1
>>> #in find function -1 denotes value not found
