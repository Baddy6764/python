
import sys, random
from random import randrange
from ssl import PROTOCOL_SSLv23

# indentation in python
if 10 > 2:
    print("10 is greater than 2!!!")

# python variables
x = 10
y = 'Hello world!!!'
print(x)
print(y)

# casting in python
i = str(25)
j = int(25)
k = float(25.0)
print(i, type(i))
print(j, type(j))
print(k, type(k))

# multiple values to multiple variables
o, b, c = "Orange", "Banana", "Cherry"
print(o)
print(b)
print(c)

# Unpack a collection
items = ['Book', 'Table', 'Chair']
x, y, z = items
print(x)
print(y)
print(z)

# Global variables
x = 'cool'
def myFunc():
    print('Python is ' + x)
    global y
    y = 'fantastic'
myFunc()
print('Python is ' + y)

# Data types
# string
p = str("Hello World")
print(p, type(p))
# int
one = int(1)
print(one, type(one))
# float
oneDec = float(1.10)
print(oneDec, type(oneDec))
# complex
c = complex(9j)
print(c, type(c))
# list
shop = list(('Watch', 'Phone', 'Computer'))
print(shop, type(shop))
# tuple
tup = tuple(("Curtin", "Pen", "Book"))
# range
r = range(0, 5)
print(r, type(r))
# dict
person = dict(name="John", age= "22")
print(person, type(person))
# set
fruits = set(("Mango", "Apple", "Guava"))
print(fruits, type(fruits))
#frozenset
fruts = frozenset(("banana", "maize", "berry"))
print(fruts, type(fruts))
# boolean
boo = bool(1)
print(boo, type(boo))
# bytes
byt = bytes(10)
print(byt, type(byt))
# bytearray
byt_array = bytearray(10)
print(byt_array, type(byt_array))
# memoryview
memo = memoryview(bytes(10))
print(memo,  type(memo))
# NoneType
non = None
print(non, type)

# python numbers
intt = 10
flooat = 10.5
compleex = 3j
floPower = 10e5
ranNum = random.randrange(1, 30)
print(floPower)
print(ranNum)

# multiline string
a = """
Hello,
     How are you doing today? I hope you are having a good day. 
"""
print(a)

# strings are arrays
mr = "Mr David"
print(mr[0])

# looping through strings
for s in "Cassava":
    print(s)

# strings length
print(len(mr))

# check string
_txt = "The best things in life are free"
print("are" in _txt)

# check if Not
print("expensive" not in _txt)

# slicing
print(mr[3:])

# negative indexing
print(mr[-5:-2])

# upper case
print(mr.upper())

# lower case
print(mr.lower())

# remove whitespace
striip = " Mr. V "
print(striip.strip())

# replace strings
print(striip.replace('V', 'VV').strip())

# split strings
print(mr.split(" "))

# F-Strings
age = 100
q = f"How old are you? I'm {age} years old."
print(q)

# placeholders and modifiers
_price = 340
itemP = f"Total price is {_price:.1f}"
print(itemP)

# escape characters
charac = "Don't learn to hack, \"Hack to learn\""
print(charac)
__txt = 'Don\'t give up'
print(__txt)
blacksl = "Say my name. \\ (hacker)"
print(blacksl)
caReturn = "I\tLove\tPython!"
print(caReturn)
back_space = "Kiss \bPython"
print(back_space)
formF = "Dude\f\f\f"
print(formF)

# strings method
# capitalize method
f_n = "cole Palmer"
print(f_n.capitalize())

# casefold method
word = "Allah is Great"
print(word.casefold())

# center method
cen = "TOOLS"
print(cen.center(10, "-"))

# count method
exp = "I love Python, Python is great, Python for live."
print(exp.count('Python'))

# encode method
_name = "Dåvid"
print(_name.encode())

# endswith method
_cs = 'Bug Hunter.'
print(_cs.endswith('er.'))

# expandtabs method
obj = 'C\to\tm\tp\tu\tt\te\tr'
print(obj.expandtabs(2))

# find method
print(exp.find('P'))

# format method
formatt  = "item: {word} price: {num}".format(word='T-shirt', num=10).center(25)
__formatt = "item: {0} price: {1}".format("Bags", 22)
___formatt = "item: {} price: {}".format("Shoes", 55)
print(f"{formatt}\n {___formatt}\n {___formatt}\n")

# data
data =  {"name": "David Luis", "age": 33, "email": "luis0@fake.net"}

# format_map method
intro = "My name is {name}, I'm {age}. You can contact me on {email} if you want to know more about me".format_map(data)
print(intro)

# index method
print(intro.index('me'))

# isalnum method
alpha_numeric = "Position1"
print(alpha_numeric.isalnum())

# isalpha method
alpa = "PythonJ"
print(alpa.isalpha())

# isascii method
ani = 'Lion10'
print(ani.isascii())

# isdecimal method
__nums = '12345'
print(__nums.isdecimal())

# isdigit method
_digit = '73862'
print(_digit.isdigit())

# isidentifier method
identi = "python_is_great_1"
print(identi.isidentifier())

# islower method
lower_str = 'strings method'
print(lower_str.islower())

# isnumeric method
num_eric = '8374203'
print(num_eric.isnumeric())

# isprintable method
prin_table = 'Hello! Do you like python?'
print(prin_table.isprintable())

# isspace method
s_pace = '  '
print(s_pace.isspace())

# istitle method
ti_tile = 'Python Or Javascript?'
print(ti_tile.istitle())

# isupper method
up_per = 'PYTHON'
print(up_per.isupper())

# join method
_tuple = ('Python', 'JavaScript', 'Go', 'Bash')
print("Or".join(_tuple))

# ljust method
_fru = 'banana'
print(_fru.ljust(10, "_"))

# lower method
_words = 'python Project Version Control'
print(_words.lower())

# lstrip method
charc, _white = '_______Python______', '         ICE         '
print(f'{charc.lstrip('_')}\n' f'{_white.lstrip()}')

# maketrans method
t_xt = 'Wood, Bash'
_y = 'hBas'
_x = 'eRud'
_z = 'Book'
_mytrans = t_xt.maketrans(_y, _x)
print(t_xt.translate(_mytrans))

# partition
expression = 'I only love programming languages others languages I like them'
print(expression.partition("only"))

# replace
print(t_xt.replace("Wood", "Java"))

# rfind method
occu = "Hello friend, Hope you are doing good?"
print(occu.rfind('o'))

# rindex method
_occu = "Hello friend, Hope you are doing good?"
print(_occu.rindex("d"))

# rjust method
__occu = "Hello friend, Hope you are doing good?"
print(__occu.rjust(50))

# rpartition method
_health = 'Drink water not minerals, water is free and great'
print(_health.rpartition('water'))

# rsplit method
f_ruits = 'Apple, Orange, Watermelon'
print(f_ruits.rsplit(",", 1))

# rstrip method
_f = '    Cherry______'
print(_f.rstrip('_'))

# split method
_h = 'David, Joe, Smith'
print(_h.split())

# splitlines method
_hn = 'David, Joe\n Smith, Louis'
print(_hn.splitlines())

# swapcase method
_hc = 'David Joe Smith PETER'
print(_hc.swapcase())

# title method
_hu = '3gig 4gig data'
print(_hu.title())

# zfill method
_hp = 'Python'
print(_hp.zfill(10))


# Boolean

print(1 == 1)
print(1 > 0)
print(-1 > 0)

# evaluate values and variables
print(bool('Python'))
print(bool(-1))

_ey = 'JavaScript Python'
_ex = 10
_ez = None
print(bool(_ey), bool(_ex), bool(_ez))

# isinstance
_xxy = '123'
print(isinstance(_xxy, str))

# python operator

# logical operator
# or
print( 1 == 1 or 1 > 2)

# and
print(0 > -1 and 0 < 1)

# not
print(not(1==1 and 2==2))

# identity operator

# is
hsd = 'Allah'
shj = 'God'
bja = hsd
print(hsd is bja)
print(hsd is shj)

# is not
print(hsd is not bja)
print(hsd is not shj)

# membership operator
dhui = ['water', 'mineral']
print('water' in dhui)
print('minera' not in dhui)

# Python Lists

# lists
this_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(len(this_list))
print(this_list[3])
print(this_list[-1])
print(this_list[0:4])
print(this_list[:2])
print(this_list[1:])
print(this_list[-3:-1])
this_list[0] = 'Saturday'
print(this_list)
this_list[0] = 'Sunday'
print(this_list)
this_list.insert(6, 'Saturday')
print(this_list)
this_list.append('Saturday and Sunday is weekend')
print(this_list)
loop_life = ['Code', 'Eat', 'Sleep', 'Repeat']
this_list.extend(loop_life)
print(this_list)
this_list.remove('Saturday and Sunday is weekend')
print(this_list)
this_list.append('Lazy')
print(this_list)
this_list.pop()
print(this_list)
this_list.append('Consistency')
print(this_list)
del this_list[-1]
print(this_list)
this_list.clear()
print(this_list)

# loop lists
_names = ['John', 'Simon', 'David', 'James', 'Kingsley']

for name in _names:
    print(name)

# loop through the index numbers
years = ['2000', '2010', '2020']
for y in range(len(years)):
    print(years[y])

# using while loop
emails = ['david@fake.net', 'james@fake.com', 'samuel@fake.net', 'sarah@fake.com']
i = 0
while i < len(emails):
    print(emails[i])
    i = i + 1

# looping using lists comprehension
pLan = ['Python', 'JavaScript', 'PHP', 'Java']
[print(pl) for pl in pLan]

# lists comprehension
countries = ['Nigeria', 'United Kingdom', 'United State', 'Russia', 'Canada', 'Chile', 'China']

for c in range(len(countries)):
    if "C" in countries[c]:
        print(countries[c])
    else:
        print("N" in countries[c])

dest = [des for des in countries if "U" in des]
print(dest)







print(sys.version)