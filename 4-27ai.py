Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

====== RESTART: C:/Users/jaeyong/Desktop/클라우드 컴퓨터 실습/AI python/Readline.py =====
단어통계.txt 파일이 생성되었습니다



st = ["Korea", "Japan", "China", "Apple", "Mango"]
st
['Korea', 'Japan', 'China', 'Apple', 'Mango']
st.sort()
st
['Apple', 'China', 'Japan', 'Korea', 'Mango']


d = dict()
for w in st:
    findAdd(d, w)

    

d
{'Apple': 1, 'China': 1, 'Japan': 1, 'Korea': 1, 'Mango': 1}
dir(d)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
d.keys()
dict_keys(['Apple', 'China', 'Japan', 'Korea', 'Mango'])
