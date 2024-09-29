
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

# sorting lists
digits = [100, 40, 20, 90, 80, 50, 30, 60, 70]
digits.sort()
print(digits)
digits.sort(reverse=True)
print(digits)

# customize sort func
def myFunc(n):
    return abs(n - 50)

numb = [40, 30, 50, 10, 20]

numb.sort(key = myFunc)

print(numb)

# copy lists
passwd = ['admin123', 'developer123', 'administrator']
copyPasswd = passwd.copy()[0]
print(copyPasswd)
_copyPassd = list(passwd)
print(_copyPassd)

# lists methods

# copy() - to copy lists
# reverse() - to reverse lists in descending order
# extend() - to add lists to the end of another lists
# append() - to append element to a lists at the end
# clear() - to clear a lists
# del() - to delete lists and element
# count() - to count number of times element in lists
# index() - Returns the index of the first element with the specified value
# insert() - Adds an element at the specified position
# sort() - sort lists
# remove() -Removes the item with the specified value
# pop() - Removes the item with the specified position

# Tuple
files = ('ms1.txt', 'ms2.txt', 'ms3.txt')
print(files)
# change tuples value
ch = list(files)
ch[0] = "f.txt"
cht = tuple(ch)
print(cht)

# add tuple to a tuple
secF = ('auth.txt',)
files += secF
print(files)

# unpacking tuples
dirr =('/tmp', '/etc/passwd', '/etc/nginx')
(tempdir, etcdir, nginxdir) = dirr
print(f'{tempdir}\n{etcdir}\n{nginxdir}')

(tmpDir, *rDir) = dirr
print(f'{tmpDir}\n{rDir}')

# join tuples
file_dir = files + dirr
print(file_dir)
print(dirr * 3)

# tuple methods
# count() - Returns the number of times a specified value occurs in a tuple
# index() - Returns the position of a specified value

# set
myset = {"hello", "world", "python"}
print(myset)
thisset = {"orange", "watermelon", "cherry"}
print(len(thisset))

for x in myset:
    print(x)

print("orange" in thisset)
print("banana" not in thisset)
print(not("banana" not in thisset))

# add sets
thisset.add("guava")
print(thisset)

_p = {"Java", "JavaScript"}
myset.update(_p)
print(myset)

# remove item
myset.remove("Java")
print(myset)

# discard item
myset.discard('world')
print(myset)

# pop item
thisset.pop()
print(thisset)

# clear items
thisset.clear()
print(thisset)

# join sets
dirOne = {"api", "v1", "v2", "v3"}
dirTwo = {"portal", "content", "public", "api"}
dirThree = {"public", "private", "001", "p"}

# union meth
set1 = dirOne.union(dirThree)
print(set1)

# update
digitO = {898, 283, 292, 728}
digitT = {100.10, 374.19, 476.40}
digitO.update(digitT)
print(digitO)

# intersection
digitTh = {123, 738, 328, 928}
digitF = {567, 123, 328, 100}
digitTh.intersection(digitF)
print(digitTh)

# intersection_update
objOnee = {"Car", "Bike", "Motorcycle"}
objTwo = {"Car", "Mouse", "Computer"}
objOnee.intersection_update(objTwo)
print(objOnee)

# difference
objThree = {"Downloading", "test", "test1"}
objFour = {"test", "Artz", "Content"}
dkwdwh = objThree.difference(objFour)
print(dkwdwh)

# difference_update
aie = {"Haymond", "John", "Moss"}
dhsh = {"John", "Moses", "Dani"}
aie.difference_update(dhsh)
print(aie)

# symmetric_difference
sdh = {"cherry", "apple", "berry"}
xsk = {"microsoft", "google", "apple"}
sja = sdh.symmetric_difference(xsk)
print(sja)

# symmetric_difference_update
csn = {"cherry", "apple", "berry"}
cjw = {"microsoft", "google", "apple"}
csn.symmetric_difference_update(cjw)
print(csn)

# isdisjoint
njda = {"NVDA", "OPENAL", "LINUX"}
shs = {"GOOGLE", "MICROSOFT", "YAHOO"}
fjhw = njda.isdisjoint(shs)
print(fjhw)

# issubset
dniw = {"a", "1", "b", "2"}
djhd = {"a", "b", "c", "1", "2", "f"}
dhj = dniw.issubset(djhd)
print(dhj)

# issuperset
bdwj = djhd.issuperset(dniw)
print(bdwj)

# set methods

# add() - add element to the set
# clear() - clear elements in set
# copy() - copy elements in set
# difference() - returns a set containing the difference between two or more sets
# difference_update() - removes the items in sets that are not included in another, specified set
# discard() - remove item
# intersection() - returns set, that is the intersection of two other sets
# intersection_update() - removes items that are not present in other, specified set(s)
# isdisjoint() - return true if items is not present in both sets
# issubset - return true if all items in set is present in specified set
# issuperset - returns true if specified set items contain in original set
# pop() - remove element
# remove() remove specified element
# symmetric-difference() returns a set with symmetric difference of two sets
# symmetric_difference_update() - inserts symmetric difference from this set to another
# union() - return a set containing the union sets
# update() - update set with the union of this set and others

# Dictionary

bcdjsh = {"userId": "1", "username": "david", "password": "david123"}
print(bcdjsh)
print(bcdjsh["userId"])
print(len(bcdjsh))

# the dict constructor
thisdict = dict(name = "Hammond", age = 33, country = "united states of america")
print(thisdict)
print(thisdict.get("age"))
print(thisdict.keys())
print(bcdjsh.keys())

# view of dict
xox = thisdict.keys()
thisdict["height"] = "5'7"
print(xox)
print(thisdict.values())

# value view of dict
hds = thisdict.values()
thisdict["age"] = 32
print(hds)
print(thisdict.items())

# items of view dict
bdiw = thisdict.items()
thisdict["occupation"] = "Cybersecurity"
print(bdiw)

# update dict
thisdict.update({"occupation": "Software Engineer"})
print(thisdict)
thisdict.update({"email": "hammond@fake.com"})
print(thisdict)

# removing items
thisdict.pop("height")
print(thisdict)
thisdict.popitem()
print(thisdict)
del thisdict["occupation"]
print(thisdict)
thisdict.clear()
print(thisdict)

# looping dict
thiscar = dict(brand = "bmw", model = "sport", year = 2020)
for x in thiscar.values():
    print(x)
for y, x in thiscar.items():
    print(y, x)

# copy dict
copiedcar = thiscar.copy()
print(copiedcar)
ccar = dict(thiscar)
print(ccar)

# fromkeys
brand = ("bmw", "ford", "benz")
yr = 2020
cars = dict.fromkeys(brand, yr)
print(cars)

# dict methods

# clear() - remove all elements
# copy() - returns a copy of dict
# fromkeys() - returns a dict with specified keys and value
# get() -  return item with specified key
# items() - returns a tuple containing for each key value pair
# keys() - returns a list containing dict keys
# pop() - remove item with specified key
# popitem() - remove the last item with key value pair
# setdefault() - returns item with specified key, if the does not exist: insert the key, with the specified value
# update() - update the dict with specified key-value pairs
# values() - returns a list of values in dict

# if ... else
ii = 10
iii = 5
if iii < ii:
    pass

# while loop
i = 1
while i < 10:
    print(i)
    i += 1

# the break statement
while i < 20:
    print(i)
    if (i == 10):
        break
    i += 1

# the continue statement
i = 0
while i < 6:
    i += 1
    if (i == 1):
        continue
    print(i)

# the else statement
while i < 5:
    print(i)
    i += 1
else:
    print("done")

# for loops

for r in range(1, 10, 2):
    print(r)
    if (r == 5):
        break
else:
    print("Finished")

# functions
def my_name(f_name):
    print(f_name + "hacker")

my_name("001 ")
my_name("white_")
my_name("black_")
my_name("grey_")

# arbitrary arguments *args
def dns(*names):
    print("Target " + names[0])

dns("google.com")
dns("cloudflare.com")
dns("x.com")

# arbitrary keyword arguments, **kwargs
def files(**file):
    print("/home/hacker/Documents/" + file["file1"])

files(file1="auth.txt", file2="sub.txt")

# recursion
def tri_recursion(k):
  if(k > 0):
    result =k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(2)

# python lambda

lam = lambda o: o + 20
print(lam(20))

lam2 = lambda a, b: a % b
print(lam2(10, 2))

def myF(d):
    return lambda a: a * d

multi = myF(2)
print(multi(5))

# classes and objects
class myClass:
    x = 10
print(myClass)

p1 = myClass()
print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

pp1 = Person("Hacker", 16)
print(pp1.name)
print(pp1.age)

class Data:
    def __init__(self, email, password):
        self.email = email
        self.password = password

uD = Data("hacker@fake.net", "hacker123")
print(uD.email)
print(uD.password)

class Objects:
    def __init__(self, car, phone):
        self.car = car
        self.phone = phone
    def __str__(self):
        return f"{self.car}\n{self.phone}\n"

obbj = Objects("BMW", "Iphone 16")
print(obbj)

class Quote:
    def __init__(self, quote):
        self.quote = quote

    def show(self):
         print(f"Never give {self.quote}")

qqq = Quote("up")
qqq.show()

# Python Inheritance

# create a parent class
class UserOne:
    def __init__(self, fname, lname, email, age, country):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.age = age
        self.country = country

    def showUser(self):
        print(self.fname, self.lname, self.email, self.age, self.country)

# create child class
class userAdd(UserOne):
    def __init__(self, fname, lname, email, age, country, state):
        # UserOne.__init__(self, fname, lname, email, age, country)
        super().__init__(fname, lname, email, age, country)
        self._state_ = state

    def contact(self):
        print("Contact me on " + self.email + ", Have a wonderful day.")

ii = 0
ncnej = ["Apple", "Juice", "Orange"]

while ii < len(ncnej):
    print(ncnej)
    ii += 1

userProfile = userAdd("John", "Doe", "johndoe@fake.net", 38, "United Kingdom", "West London")
userProfile.showUser()
print(userProfile._state_)
userProfile.contact()


class Data:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def user(self):
        print(self.email, self.password)

userData = Data("admin@fake.net", "admin123")
print(userData.user())

# python Iterator

class MyNum:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
      if self.a <= 10:
          x = self.a
          self.a += 1
          return x
      else:
          raise StopIteration
myClass = MyNum()
IterObj = iter(myClass)

print(next(IterObj))

# modules
import platform

pt = platform.system()
frhj = dir(platform)
print(pt)
print(frhj)

# Python Date
import datetime

date = datetime.datetime.now()
print(date.year)
print(date.fold)
print(date.microsecond)
print(date.timestamp())
print(date.tzinfo)

# Python Math
minn = min(10, 12, 30, 0)
maxx = max(1, 10, 22, 9)
abss = abs(-1.29)
poww = pow(2, 5)
print(minn)
print(maxx)
print(abss)
print(poww)

# math built in module
import math

squaroot = math.sqrt(10)
ceill = math.ceil(1.5)
flor = math.floor(1.5)
pie = math.pi
print(squaroot)
print(ceill)
print(flor)
print(pie)

# Python JSON
import json

admin = '{"email": "admin@fake.net", "password": "admin1234", "name": "Philip"}'

user = {"email": "user@fake.net", "password": "user1234", "name": "David"}

par = json.loads(admin)
userD = json.dumps(user, indent=4, sort_keys=True, separators=(".", "=",))
print(par["password"], par)
print(userD)

# Python RegEx
import re

txt = 'This file contains sensitive data'
mach = re.search('^This.*data$', txt)
print(mach)

if mach:
    print(True)
else:
    print(False)


# python try except

try:
    print(abc)

except NameError:
    print("abc is not defined")

except:
    print("something went wrong")

#####
try:
    print("Hello python!")

except NameError:
    print("abc is not defined")

except:
    print("something went wrong")

else:
    print("no errors")

finally:
    print("Finished.")

###
# one = -1
#
# if one < 0:
#     raise Exception("no numbers below zero")


## Python File Handling

f = open("demo.txt", "r")
# print(f.read())
print(f.readline())
f.close()

f = open("demo.txt", "a")
f.write(" Yes!")
f.close()

f = open("demo.txt", "r")
print(f.read())
f.close()

f = open("demo.txt", "w")
f.write("Overwritten")
f.close()

f = open("demo.txt", "r")
print(f.read())
f.close()

f = open("demo2.txt", "x")
f.close()

f = open("demo2.txt", "r")
print(f.read())
f.close()

# delete file
from os import remove

remove("demo2.txt")

ages = [12, 18, 22, 20, 15]

def fil(x):
    if x < 18:
        return False
    else:
        return True

adults = filter(fil, ages)

for x in adults:
    print(x)

print(help())
















print(sys.version)