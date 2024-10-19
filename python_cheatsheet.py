
'''msg='Hello, world!'
print(msg[2:6])'''

'''myList=[]
myList.append(1)
myList.append(2)

for item in myList:
    print(item)'''
  
 #if else   
'''num=200
if num>100:
    print("num is greater than 0")
else:
    print("num is not greater than 0")'''
    

#loop            
'''for item in range(6):
    if item == 6: break
    print(item)
else:
    print("finally finished!")'''
    
#function
'''def my_function():
    print("Hello from a function")
   
my_function()'''

#arithmetic
'''result1=10+30                
result2=40-10                
result3=50*5                
result4=16/4                
result5=16//4                
result6=25%2                
result7=5**3
print(result1)                
print(result2)                
print(result3)                
print(result4)                
print(result5)                
print(result6)                
print(result7)'''

#plus-Equal
'''counter = 0
counter += 10
counter = 0
counter = counter + 10

message="part 1."  
message+= "part 2." 

print(message)'''

#f-strings
'''name="Danish Iqbal"
print(f"Hello,{name}")

num=10
print(f"{num}+10={num+10}")'''

#python Built-in Data

#string
'''name="Danish "
name+='iqbal'

multi_string="""Essay topics in English can be difficult to come up with. While writing essays, 
many college and high school students face writer’s block and have a hard time to think about topics
and ideas for an essay. In this article, we will list out many good essay topics from different categories
like argumentative essays, essays on technology, environment essays for students from 5th, 6th, 7th, 8th grades."""

print(name) 
print(multi_string)'''

#numbers
'''x=1
y=2.8
z=1j
s='cat'
print(type(s))'''

#Boolean
'''my_bool = True
my_bool1 = False
print(my_bool)'''

#list
'''list1=["apple","banana","cherry"]
list2=[True,False,False]
list3=[1,5,7,9,3]
list4=list((1,5,7,9,3))

print(list1)
print(list2)
print(list3)
print(list4)'''

#Tuple
'''my_tuple=(1,2,3)
my_tuple=tuple((1,2,3))
print(my_tuple)'''

#set
'''set1={"a","b","c"}
set2=set(("a","b","c"))
print(set1)
print(set2)'''

#Heaps
'''import heapq
myList=[9,5,4,1,3,2]
heapq.heapify(myList)
print(myList)
print(myList[0])

heapq.heappush(myList,10)
x = heapq.heappop(myList)
print(x)'''

'''import heapq
myList=[9,5,4,1,3,2]
myList=[-val for val in myList]
heapq.heapify(myList)
x=heapq.heappop(myList)
print(-x)'''

#Stack and Queues
'''from collections import deque
q=deque()
q=deque([1,2,3])

q.append(4)
q.appendleft(0)
print(q)

x=q.pop()
y=q.popleft()
print(x)
print(y)
print(q)

q.rotate(1)
print(q)'''

#---------python string --------->
#Array like->
'''hello='hello world'
print(hello[0])
print(hello[-1])'''

#looping->
'''for char in "foo":
    print(char)'''
    
#slicing
'''s='Danish'
print(s[2:6])
print(s[0:2])
print(s[:2])
print(s[2:])
print(s[:2]+s[2:])
print(s[:])
print(s[-6:-2])'''

#with a stride
'''s='12345'*5
print(s)    
print(s[::5])    
print(s[2::5])    
print(s[::-5])
print(s[::-1])'''

#string length
'''hello="hello, world!"
print(len(hello))'''

#multiple copies
'''s='===+'
n=8
print(s*n)'''

#check string
'''s='spam'
print(s in 'i saw a spam a lot!')
print(s not in 'i saw the holy grail!')'''

#concatenates
'''s='Danish '
t="Iqbal"
print(s+t)

n='2'
m='5'
print(m+n)'''

#formatting
'''name='world'
print('hello. %s!'%name)

name='Danish'
age='12'
print('%s is %s year old.'%(name,age))'''

#format() method
'''print('my name is {fname}, I am {age}'.format(fname='danish',age=20) )
print('my name is {0}, I am {1}'.format('danish',20) )
print('my name is {}, I am {}'.format('danish',20) )'''

#input
'''name=input('enter any name:')
print(name)'''

#join
'''print('#'.join(['danish','peter','vicky']))'''

#endswith
'''print("hello, world!".endswith("!"))'''

#F-strings
'''website='World'
print(f"Hello,{website}")

num=10
print(f"{num} + 10 = {num+10}")

print(f"""He said {"I'm good boy"}""") 

print(f'5{"{stars}"}')
print(f'{{5}} {"stars"}')   

name='danish'
age=21
print(f"""Hello! 
      i'm {name},
      i'm {age} years old""")

print("hello\n  I'm Danish.\n  I'm 21.")'''

# f-string fill align
'''
print(f'{"text":10}')
print(f'{"test":*>10}')
print(f'{"test":*<10}')
print(f'{"test":*^10}')
print(f'{12345:0>10}')'''

# f-string Type
'''
print(f'{10:b}') #binary type
print(f'{10:0}') #octal type
print(f'{200:x}') #hexadecimal type
print(f'{200:X}')
print(f'{345600000000:e}')  #scientific notation
print(f'{65:c}')  #character type
print(f'{10:#b}')  #[type] with notation (base)
print(f'{10:#o}')
print(f'{10:#x}')'''

#F-string others
'''
print(f'{-12345:0=10}')  #negative number
print(f'{12345:010}')  #[0] shortcut (not align)
print(f'{-12345:010}')
import math   #[.precision]
print(math.pi)
print(f'{math.pi:.2f}')

print(f'{1000000:,.2f}')  #[grouping_option]
print(f'{1000000:_.2f}')  #[grouping_option]

print(f'{0.25:0%}') #percentage
print(f'{0.25:.0%}')'''

# F-String sign
'''
print(f'{12345:+}')
print(f'{-12345:+}')
print(f'{-12345:+10}')
print(f'{-12345:+010}')'''

#------ python List ------->

#defining
'''
li1=[]
print(li1)

li2=[4, 5, 6]
print(li2)

li3= list((1, 2, 3))
print(li3)

li4 = list(range(1,11))
print(li4)'''

#Generate
'''
print(list(filter(lambda x : x%2==1, range(1,20))))
print([x ** 2 for x in range (1,11) if x % 2==1])
print([x for x in [3,4,5,6,7] if x >5])
print(list(filter(lambda x: x>5, [3,4,5,6,7])))'''

#Append
'''
li=[]
li.append(1)
print(li)

li.append(2)
print(li)

li.append(4)
print(li)

li.append(3)
print(li)'''

#-----------------------*----------------*------------------->
#-------List Slicing--------->
#syntax of list slicing:

#---> a_list[start:end]
#---> a_list[start:end:step]

#                 Slicing
'''
a=['spam','egg','tomato','Hello']
print(a[2:5])

a=['span','tomato','egg']
print(a[-3:-2])

a=['egg','world','tomato']
print(a[1:3])'''

#       Omitting index
'''
a=['spam','egg','tomato','Hello']
print(a[:4])

a=['spam','egg','tomato','Hello']
print(a[0:4])

a=['spam','egg','tomato','Hello']
print(a[2:])

a=['spam','egg','tomato','Hello']
print(a[3:len(a)])

a=['spam','egg','tomato','Hello']
print(a[:])'''


#         With a Stride
'''
a=['spam','egg','hello','world!','tomato','mouse']
print(a)

a=['spam','egg','hello','world!','tomato','mouse']
print(a[0:6:2])

a=['spam','egg','hello','world!','tomato','mouse']
print(a[1:6:2])

a=['spam','egg','hello','world!','tomato','mouse']
print(a[6:0:-2])

a=['spam','egg','hello','world!','tomato','mouse']
print(a[::-1])'''


#--------      Remove       ------->
'''
li=['bread','butter','milk']
print(li.pop())

li=['bread','butter','milk']
del( li[0])
print(li)'''

#       Access
'''
li=['a','b','c','d']
print(li[0])
print(li[-1])
print(li[4])'''

#   Concatenating
'''
odd=[1,3,5]
odd.extend([9,11,13])
print(odd)

odd=[1,3,5]
print(odd+[9,11,13])'''


#        Sort & Reverse
'''
li=[3,1,3,2,5]
li.sort()
print(li)

li.reverse()
print(li)'''

#     Count
'''
li=[3,1,3,2,5,2,2,2]
print(li.count(2))'''

#Repeating
'''
li = ["re"]*3
print(li)'''

#--------Python Flow  Control------->

#        Basic
'''
num=11
if num>10:
    print("num is totally bigger than 10.")
elif num<10:
    print("num is smaller than 10")
else:
    print("num is indeed 10.")'''
    
#               One Line
'''
a=350
b=200
r="a" if a>b else "b"
print(r)'''

#        Else If
'''
Value = False
if not Value:
    print("value is false")
elif Value is None:
    print("value is none")
else:
    print("value is true")'''
    
#------- Python Loops --------->

#     Basic
'''
primes = [2,3,5,6]
for prime in primes:
    print(prime)'''
    
#    With Index
'''
animals= ['dog','cat','mouse','fox']
for i, value in enumerate(animals):
    print(i,value)'''
    
#    while
'''
x = 0
while x<4:
    print(x)
    x+=1'''
    
#         Break
'''
x=0
for index in range(10):
    x = index*10
    if index == 10:
        break
    print(x)'''
    
#   Continue
'''
for index in range(3, 8):
    x = index*10
    if index == 5:
        continue
    print(x)'''
    
#     Range
'''
for i in range(4):
    print(i) #prints: 0 1 2 3
    
for i in range(4,8):
    print(i) #prints: 4 5 6 7
    
for i in range(4, 10, 2):
    print(i) # prints: 4 6 8 '''
    

#      With Zip()
'''
Words = ['mon','tue','wed']
nums = [1,2,3]
for w, n in zip(Words, nums):
    print('%d.%s, '%(n, w))'''
    
                                                              
#     for/else
'''
nums = [60, 70, 30, 110, 90]
for n in nums:
    if n > 100:
        print(f"{n} is bigger than 100")
        break
    else:
        print("not found")'''
        

#---------------Python Function------------->

#          Basic
'''
def hello_world():
    print('Hello World!')
hello_world()'''

#     Return
'''
def add(x,y):
    print("x is %s, y is %s" %(x,y))
    return x+y
add(5,6)'''

#    Positional Arguments
'''
def varargs(*args):
    return args

print(varargs(1,2,3))'''

#    Keyword Arguments
'''
def keyword_args(**kwargs):
    return kwargs

print(keyword_args(big="foot",loch="ness"))'''

#    Returning Multiple
'''
def swap(x,y):
    return y,x
x="Iqbal"
y="Danish"
x,y = swap(x,y)
print(x,y)'''

#  Default Value
'''
def add(x,y=10):
    return x+y
print(add(5))
print(add(5,20))'''

#    Anonymous Function
'''
print((lambda x: x>2)(3))

print((lambda x, y: x**2+y**2)(3,1))'''

# -----------Python Modules--------------->
#  import modules
'''
import math
print(math.sqrt(16))'''

#from a module
'''
from math import ceil, floor
print(ceil(3.7))
print(floor(3.7))'''

# import all->
#from math import * 

#  shorten module
'''
import math as m
print(m.sqrt(16))'''

# Function and attributes
'''
import math
print(dir(math))'''

# ---------Python class & inheritance------------->
#Defining
'''
class MyNewClass:
    pass
print("hello world!")
my=MyNewClass()'''

# Constructor
'''
class Animal:
    def  __init__(self,voice):
        self.voice=voice
        
cat = Animal('Meow')
print(cat.voice)

dog = Animal('Woof')
print(dog.voice) '''

#   Method
'''
class Dog :
    def bark(self):
        print("Ham-Ham")
        
charlie = Dog()
charlie.bark()'''

#  Class Variable
'''
class MyClass:
    class_variable = "A class Variable!"
    
print(MyClass.class_variable)
x= MyClass()
print(x.class_variable)'''

#      super() function
'''
class ParentsClass:
    def print_test(self):
        print("Parents method")
        
class ChildClass(ParentsClass):
    def print_test(self):
        print("child method")
        return super().print_test()   
        
child_instance = ChildClass()
child_instance.print_test()'''

#         repr() method
'''
class employee:
    def __init__(self,name):
        self.name = name
        
    def __repr__(self):
        return self.name
    
john = employee('john')
print(john)   '''


#     User-defined exceptions
'''
class CustomError(Exception):
    pass'''
    
#      Polymorphism
'''
class ParentsClass:
    def print_self(self):
        print('A')
        
class ChildClass(ParentsClass):
    def print_self(self):
        print('B') 
        
obj_A = ParentsClass()
obj_B = ChildClass()

obj_A.print_self()
obj_B.print_self()'''

#       overriding
'''
class ParentsClass:
    def print_self(self):
        print("parents")
        
class ChildClass(ParentsClass):
    def print_self(self):
        print("child")
        
child_instance = ChildClass()
child_instance.print_self()'''

#     inheritance
'''
class Animal:
    def __init__(self,name, legs):
        self.name = name
        self.legs = legs
        
class Dog(Animal):
    def sound(self):
        print("Woof!")
        
pluto =Dog("pluto", 4)
print(pluto.name)
print(pluto.legs)
pluto.sound()'''

# --------------Miscellaneous------------>
#  Generators
'''
def double_numbers(iterable):
    for i in iterable:
        yield i+i

#--------------x--------------
nums = [1, 2, 3, 4]
doubled = double_numbers(nums)

# Since it's a generator, we can loop through it
for num in doubled:
    print(num)'''
    
    
#    Generator to list 
'''
values= (-x for x in [1,2,3,4,5])
gen_to_list = list(values)

print(gen_to_list)'''


#         Handle Exception

try:
    
    raise IndexError("This is an index error")
except IndexError as e:
    pass
else:
    print("all good!")
finally:
    print("We clean up resource here")                 

