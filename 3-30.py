Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
type(3)
<class 'int'>
type('DIT')
<class 'str'>
type(3.14)
<class 'float'>
str(3)
'3'
float(3)
3.0
int("365")
365
float(500)
500.0
float(0)
0.0
str(3)
'3'
int("재용")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    int("재용")
ValueError: invalid literal for int() with base 10: '재용'
2>3
False
3>2
True
type(2>3)
<class 'bool'>
type(3>2)
<class 'bool'>
bool(0)
False
bool(1)
True
bool(3)
True
bool(-100)
True
name = """
부산시 부산진구 양지로 54
동의과학대학교
인공지능컴퓨터정보과
박재용"""
name
'\n부산시 부산진구 양지로 54\n동의과학대학교\n인공지능컴퓨터정보과\n박재용'
print(name)

부산시 부산진구 양지로 54
동의과학대학교
인공지능컴퓨터정보과
박재용
