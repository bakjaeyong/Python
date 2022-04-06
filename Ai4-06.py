Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 3
a =[1,2,3]
a
[1, 2, 3]
a[0]
1
a[1]
2
a[2]
3
a[3]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a[3]
IndexError: list index out of range
a[-1]
3
a[-2]
2
a[-3]
1
a[1:]
[2, 3]
a[2:]
[3]
a[1,2,3]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a[1,2,3]
TypeError: list indices must be integers or slices, not tuple
a
[1, 2, 3]
a[1]
2
a[1] = 5
a[1]
5
a[2] = 'DIT'
a[2]
'DIT'
a[1]
5
a
[1, 5, 'DIT']
a[-1]
'DIT'
a.aappend('KOREA')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.aappend('KOREA')
AttributeError: 'list' object has no attribute 'aappend'. Did you mean: 'append'?
a.append('KOREA')
a
[1, 5, 'DIT', 'KOREA']
a.append('JAPEN')
a
[1, 5, 'DIT', 'KOREA', 'JAPEN']
a.append('CHINA')
a
[1, 5, 'DIT', 'KOREA', 'JAPEN', 'CHINA']
b = 100
b
100
c = b
c
100
c +=50
c
150
b
100
a
[1, 5, 'DIT', 'KOREA', 'JAPEN', 'CHINA']
b = a
b
[1, 5, 'DIT', 'KOREA', 'JAPEN', 'CHINA']
a
[1, 5, 'DIT', 'KOREA', 'JAPEN', 'CHINA']
b.append = 'USA'
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    b.append = 'USA'
AttributeError: 'list' object attribute 'append' is read-only
bb.append('USA')
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    bb.append('USA')
NameError: name 'bb' is not defined. Did you mean: 'b'?
b.append('USA')
b
[1, 5, 'DIT', 'KOREA', 'JAPEN', 'CHINA', 'USA']
a
[1, 5, 'DIT', 'KOREA', 'JAPEN', 'CHINA', 'USA']
a.append('ROSSIA')
a
[1, 5, 'DIT', 'KOREA', 'JAPEN', 'CHINA', 'USA', 'ROSSIA']
a[4] = 'JAPAN'
a
[1, 5, 'DIT', 'KOREA', 'JAPAN', 'CHINA', 'USA', 'ROSSIA']
b.append('UKRAINE')
b
[1, 5, 'DIT', 'KOREA', 'JAPAN', 'CHINA', 'USA', 'ROSSIA', 'UKRAINE']
a.append('KOREA')
b
[1, 5, 'DIT', 'KOREA', 'JAPAN', 'CHINA', 'USA', 'ROSSIA', 'UKRAINE', 'KOREA']
b = a.copy()
b
[1, 5, 'DIT', 'KOREA', 'JAPAN', 'CHINA', 'USA', 'ROSSIA', 'UKRAINE', 'KOREA']
b.clear()
b
[]
a.count('KOREA')
2
a
[1, 5, 'DIT', 'KOREA', 'JAPAN', 'CHINA', 'USA', 'ROSSIA', 'UKRAINE', 'KOREA']
a.count('USA')
1
a.count(100)
0
a.index('DIT')
2
a[2]
'DIT'
a[3]
'KOREA'
a.insert(2, 'Computer')
a
[1, 5, 'Computer', 'DIT', 'KOREA', 'JAPAN', 'CHINA', 'USA', 'ROSSIA', 'UKRAINE', 'KOREA']
a.index('JAPAN')
5
a.insert(5, 'apple')
a
[1, 5, 'Computer', 'DIT', 'KOREA', 'apple', 'JAPAN', 'CHINA', 'USA', 'ROSSIA', 'UKRAINE', 'KOREA']
a.insert(6, 'mango')
a
[1, 5, 'Computer', 'DIT', 'KOREA', 'apple', 'mango', 'JAPAN', 'CHINA', 'USA', 'ROSSIA', 'UKRAINE', 'KOREA']
a.(insert(a.index('China'),'Mango')
   
SyntaxError: invalid syntax
for item in a:
   print(item)

   
1
5
Computer
DIT
KOREA
apple
mango
JAPAN
CHINA
USA
ROSSIA
UKRAINE
KOREA
a
   
[1, 5, 'Computer', 'DIT', 'KOREA', 'apple', 'mango', 'JAPAN', 'CHINA', 'USA', 'ROSSIA', 'UKRAINE', 'KOREA']
a.pop()
   
'KOREA'
a
   
[1, 5, 'Computer', 'DIT', 'KOREA', 'apple', 'mango', 'JAPAN', 'CHINA', 'USA', 'ROSSIA', 'UKRAINE']
a.pop()
   
'UKRAINE'
a
   
[1, 5, 'Computer', 'DIT', 'KOREA', 'apple', 'mango', 'JAPAN', 'CHINA', 'USA', 'ROSSIA']
a.remove('apple')
   
a
   
[1, 5, 'Computer', 'DIT', 'KOREA', 'mango', 'JAPAN', 'CHINA', 'USA', 'ROSSIA']
a.insert(a.index('JAPAN'),'KOREA')
   
a
   
[1, 5, 'Computer', 'DIT', 'KOREA', 'mango', 'KOREA', 'JAPAN', 'CHINA', 'USA', 'ROSSIA']
a.remove('KOREA')
   
a
   
[1, 5, 'Computer', 'DIT', 'mango', 'KOREA', 'JAPAN', 'CHINA', 'USA', 'ROSSIA']
a.insert(a.index('CHINA'),'KOREA')
   
a
   
[1, 5, 'Computer', 'DIT', 'mango', 'KOREA', 'JAPAN', 'KOREA', 'CHINA', 'USA', 'ROSSIA']
a.reverse()
   
a
   
['ROSSIA', 'USA', 'CHINA', 'KOREA', 'JAPAN', 'KOREA', 'mango', 'DIT', 'Computer', 5, 1]
a.reverse()
   
a
   
[1, 5, 'Computer', 'DIT', 'mango', 'KOREA', 'JAPAN', 'KOREA', 'CHINA', 'USA', 'ROSSIA']
a
   
[1, 5, 'Computer', 'DIT', 'mango', 'KOREA', 'JAPAN', 'KOREA', 'CHINA', 'USA', 'ROSSIA']
a.remove(1)
   
a.remove(5)
   
a
   
['Computer', 'DIT', 'mango', 'KOREA', 'JAPAN', 'KOREA', 'CHINA', 'USA', 'ROSSIA']
a.sort()
   
a
   
['CHINA', 'Computer', 'DIT', 'JAPAN', 'KOREA', 'KOREA', 'ROSSIA', 'USA', 'mango']
a.reverse()
   
a
   
['mango', 'USA', 'ROSSIA', 'KOREA', 'KOREA', 'JAPAN', 'DIT', 'Computer', 'CHINA']
a.sort()
   
a
   
['CHINA', 'Computer', 'DIT', 'JAPAN', 'KOREA', 'KOREA', 'ROSSIA', 'USA', 'mango']
b.extend(c)
   
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    b.extend(c)
TypeError: 'int' object is not iterable
b = [1,2,3]
   
c=[4,5,6]
   
b.extend(c)
   
c
   
[4, 5, 6]
b
   
[1, 2, 3, 4, 5, 6]
c.extend(b)
   
c
   
[4, 5, 6, 1, 2, 3, 4, 5, 6]
t = (1,2,3)
   
t
   
(1, 2, 3)
t
   
(1, 2, 3)
t[0]
   
1
t[1]
   
2
t[2]
   
3
t.count(2)
   
1
t.index(3)
   
2
t = list(t)
   
t
   
[1, 2, 3]
t.append(4)
   
t
   
[1, 2, 3, 4]
t[1]=100
   
t
   
[1, 100, 3, 4]
t.append(100)
   
t
   
[1, 100, 3, 4, 100]
t = tuple(t)
   
t
   
(1, 100, 3, 4, 100)
t
   
(1, 100, 3, 4, 100)
t = list(t)
   
t
   
[1, 100, 3, 4, 100]
t = tuple(t)
   
t
   
(1, 100, 3, 4, 100)
s = {1,2,3}
   
s
   
{1, 2, 3}
s = {1,2,3,3,3}
   
s
   
{1, 2, 3}
s
   
{1, 2, 3}
s.add(4)
   
s
   
{1, 2, 3, 4}
s.add('DIT')
   
s
   
{1, 2, 3, 4, 'DIT'}
s.clear()
   
s
   
set()
s
   
set()
s.add(1)
   
s
   
{1}
s = {1,2,3,4}
   
s
   
{1, 2, 3, 4}
s1 = s
   
s1
   
{1, 2, 3, 4}
s1.add(5)
   
s
   
{1, 2, 3, 4, 5}
s1
   
{1, 2, 3, 4, 5}
s.pop()
   
1
s.pop()
   
2
s1
   
{3, 4, 5}
s
   
{3, 4, 5}
s.pop(5)
   
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    s.pop(5)
TypeError: set.pop() takes no arguments (1 given)
s.pop(1)
   
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    s.pop(1)
TypeError: set.pop() takes no arguments (1 given)
s.pop()
   
3
s.remove(4)
   
s
   
{5}
a = {1,2,3,4,5}
   
a
   
{1, 2, 3, 4, 5}
b = {3,4,5,6,7}
   
b
   
{3, 4, 5, 6, 7}
a
   
{1, 2, 3, 4, 5}
b
   
{3, 4, 5, 6, 7}
a.difference(b)
   
{1, 2}
a
   
{1, 2, 3, 4, 5}
c = a.difference(b)
   
c
   
{1, 2}
a
   
{1, 2, 3, 4, 5}
b
   
{3, 4, 5, 6, 7}
c
   
{1, 2}
a
   
{1, 2, 3, 4, 5}
b
   
{3, 4, 5, 6, 7}
a.intersection_update(b)
   
a
   
{3, 4, 5}
a = list(a)
   
a
   
[3, 4, 5]
a[1]=8
   
a
   
[3, 8, 5]
b
   
{3, 4, 5, 6, 7}
a=set(a)
   
a
   
{8, 3, 5}
a=set(a)
   
a
   
{8, 3, 5}
a
   
{8, 3, 5}
a

b
   
{3, 4, 5, 6, 7}
a.union(b)
   
{3, 4, 5, 6, 7, 8}
a
   
{8, 3, 5}
b
   
{3, 4, 5, 6, 7}
a
   
{8, 3, 5}
a = list(a)
   
a.append(5)
   
a
   
[8, 3, 5, 5]
a=set(a)
   
a
   
{8, 3, 5}
a.update(b)
   
a
   
{3, 4, 5, 6, 7, 8}
a
   
{3, 4, 5, 6, 7, 8}
b
   
{3, 4, 5, 6, 7}
b.issubset(a)
   
True
a.issubset(b)
   
False
d = {'a':100, 'b':200}
   
d
   
{'a': 100, 'b': 200}
d['a']
   
100
d['b']
   
200
d['Korea']='Visit Korea'
   
d
   
{'a': 100, 'b': 200, 'Korea': 'Visit Korea'}
d
   
{'a': 100, 'b': 200, 'Korea': 'Visit Korea'}
d['AICC Member'] = ['홍서현','오유경']
   
ㅇ
   
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    ㅇ
NameError: name 'ᄋ' is not defined
d
   
{'a': 100, 'b': 200, 'Korea': 'Visit Korea', 'AICC Member': ['홍서현', '오유경']}
d.keys()
   
dict_keys(['a', 'b', 'Korea', 'AICC Member'])
