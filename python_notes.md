# Functions

* start with def
* no return type - either what return statement returns or None. (not last statement stuff)
* args have  no type either.
* function are objects too..
* invoked with fnName(args) [dont forget parenthesis for empty-arg fns]

eg:

```python
def add(a,b):
  c=a+b
  return c

add(5,10)
```

# comments

* '''...''' right after the function defintion
* function.__doc__ is the way to get the doc-string of a function
* Simple comments begin with #

# Data-types

* booleans
* numbers
* strings
* bytes and bytearray
* lists
* tuples
* sets
* dictionaries

Working with data-types

* use type(variable) to check the type of a variable.

## casting

```python
str(anything)       # for class-types, it invokes __repr__ of the class
int(string_var,base=10)
float(strint_var)   # yes. it coverts to double precision
```

## List

* list is [ .. ] separated by comma
* list elements are indexed from 0 and name[0] is the way to get one element
* -1 is the last element.
* slicing is first index to *one before* the second index.
* slicing generally creates a reference to a list. However, in the a[:] form,
  Slicing creates a copy, so a[:] is a shorthand for getting a copy of a list
* l[:size] -> will give u first size elements
* l[size:] -> will give u from size'th index (i.e size+1th element) till end
* lists never have gaps

operations on lists:

* `len(a)`
* `a.append(one_value)`
* `a.extend([list])`
* `a.insert(index,value)` # Use this for inserting at head/index-0 !
* `del a[index]`          # list size reduced by one. and all indices `index+1:<end>` become `index:<end>`
* `a.pop()`               # pops the last index, gets a IndexError when we pop a empty list. List reduces after pop.
* `a.pop(index)`          # pops given index
* `a.remove(value)`       # pops vlaue. raises ValueError if value is not found
* `a.index(value)`        # gives index of the value.
* `sorted(a)`             # Gives a new list which is sorted a.
* `str.join(list_x)`      # joins each element in list_x with str as the joining character. eg: `' '.join(['hello','world'])`

To use list as:

* LIFO (stack)
    * append/pop() is equialent of push/pop
* FIFO (queue)
    * append/pop(0) is equialent of insert_tail/pop_head
    * insert(0,val)/pop() is equialent of insert_head/pop_tail

Quickly check if a value is in list:

```python
elem in lst # WORKS FOR STRING AS WELL
```
Iterate in list

```python
for value in a:
  # .. use value
```

* `+` operator concatenates lists

Sorting a list
* list.sort()
    * sorts the list in place. So better than sorted(list) if u dont need orig-list.
    * sorted() takes any iterable, but list.sort() is available only for lists.
* Both sorted and list.sort() take a named key arg. This is a function with one-arg and returns
  a value, which is used as the value to be sorted. (Efficient as this func is called
  only once for each member). Lambda's are typically used here..

### List comprehesion

```python
[ expression-having-variable for variable in origList ]
[ expression-having-variable for variable in origList if condition ]
```

* so is it with dictionary and set comprehesion

```python
{ expression_with_i:another_expression_with_i for i in a_list if condition }
```


## Tuples

* Use `( , .. , )` for types instead of squarebracket.
* (tuple1) = (tuple2)
    * eg: (x,y,z) = (1,2,3) is a conveneient way to assign multiple variables respectively

## Sets

* Use `{ , .. , }` for sets
    * Python is intelligent to figure out if its set or dict based on
      the presence of `:` in the individual elements.
    * Note: Empty `{}` creates a dict
      ```
      a={}     # creates a dict
      a=set()  # to create empty set
      ```
* sets dont remember order of their elements. It actually unordered_set()
* values in the sets are unique.

* Operations on set:
```python
# access
## regular iteration over set works
for i in set_a:
    do_whatever(i)

# if used for checking
if i in set_a:
    do_something(i)

# add to set
a.add (value)               # adds if doesn't exist. Nothing if it already exists
                            # no native operation for check_and_add
                            #     if value in set_a:
                            #           add
                            #     else:
                            #           do_what_you_want()
# extend from other iterables
a.update(any_iterable)      # update take any number of iterables and add them to set
a.update(any_iterable, one_more_such)

# remove
a.discard(value)            # remove value from set. No error if not found
a.remove(value)             # remove value from set. KeyError raised if not found
a.pop()                     # removes some arbitrary member from set. KeyError on empty set
                            #   but DONT expect randomness. Based on impl.
                            #   you will see the same element coming out
                            #   from a same set over and over.
a.clear()                   # clears the set. same as a=set()

# cool stuff with set
a.union(b)                  # returns new set - union of a & b
a.intersection(b)           # returns new set - both in a & b
a.difference(b)             # returns new set - in a, but not in b
a.symmetric_difference(b)   # returns new set - in strictly only of a and b
```

## Dictionary

* user { key:value } for dictionary

```python

value = a[key]              # get a value. Throws KeyError if not found
value = a.get(key)          # None if key is not found
value = a.get(key, def_val) # get a value and supply default if it doesn't exist

a[key] = value  # for assignment or referenence. Note they key is indexed using square bracket

a.keys()    # gives a list of keys of dictionary a, not necesarily in sorted order .. probably iterable in py-3
a.vaues()   # gives a list of values
a.items()   # gives a list of tuple of (key, value) from a dictionary

del a[key]  # remove the key off the dict. KeyError thrown if not found
a.pop(key [, default])   # dels the key and returns its value. If key isn't present default is given. If default isn't supplied KeyError is generated

# dict literal, last comma allowed!
a={
"key1":"value1",
"key2":"value2",
"key3":"value3",
}

# when iterating over dict, u typically iterate over keys
for key in a_dict:

# py2: if u need both key and value, then use iteritems
for key,value in a_dict.iteritems()
# py3: its just items()
for key,value in a_dict.items()

# merge a diction in another one.
#  if the same key exists in both, the new one's value will win!
orig_dict.update(another_dict)
```

### Use collections.defaultdict for handy defaulting

* first arg is a factory-method.
    * what this means is an existing object wont work if you
      want that as a template! Use a lambda if you can here.

```python
>>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
>>> d = defaultdict(list)
>>> for k, v in s:
...     d[k].append(v)
...
>>> d.items()
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

#arbitrary level of nested default-dicts!
#Note the last leve will also be a default-dict, but this is okay and can be ignored - just handle keys
tree = lambda: defaultdict(tree)
my_holder = tree()
```

### Comparison

* simple == does work. BUt will give False at the slightest difference.
* It might raise ValueError if there are say numpy arrays.
* Use `DeepDiff`
```python
from deepdiff import DeepDiff

diff = DeepDiff(a, b)
## diff is a dict with differences.
## diff is empty-{} if there are no diffs.
```


## strings

### Literals

```python
# simple strings
'single quoted',  'single quote can have double " "inside it'
"doubled quoted", "double quote can have single ' ' inside it"

#multiline
a = '''This is a multiline
       preserving line-breaks and initial spaces'''

# multiline just in code
# Note there is N-O comma between them
a = ("this is a convenient"
     " way to code a lengthy string"
     " without newlines or initial spaces")
```


### notes

* Every string is a UTF-8 encoded sequence of characters in python-3.
* strings can be single or double-quoted(abs no diff. This helps to avoid escaping either). Triple single quotes is for long strings. r'raw \.string' is a raw strings
* `+` is a way to concatenate strings

a.splitlines()       # list of lines. The restult wont have carriage returns.
a.lower()            # returns a new string that has all lower caps
a.upper()
a.count('f')         # counts no of substrings
a.split(delimiter,times)   # splits a string based on delimiter. THe second is optional and gives number of times the slice should be done.
                           # use re.split(regex, string) will give a list.

a.encode('utf-8')    # gives a bytes object

a.index()
haystack.find(needle [,start [,end]])  # give index in haystack where needle is found, -1 on failure, start:end as in slicing
a.replace(old_substr, new_substr[, max]) # repl all/max occurences of old_substr with new_substr

a.rfind()  # find from end.

a.strip()            # trim whitespaces (for other chars use replace)
a.rstrip()
a.lstrip()
a.replace(what_to_replace,to_replace_with,[,max])   #bbbbbb

ord(a)    # gives the ordinal value of a, give just one char as input. I.e get the int-value of a char.
chr(num)  # inverse of ord

a.startswith()  # boht accept single str or tuple of strings
a.endswith()

### UnicodeEncodeError


Good video at : https://www.youtube.com/watch?v=sgHbC6udIqc

* if you want to convert to ascii

ascii_form = unicode_data.encode('ascii','ignore')
ascii_form = unicode_data.encode('ascii','replace')  # you get '?' for every non-ascii
ascii_form = unicode_data.encode('ascii','xmlcharrefreplace')  # you get &#<num>; for every non-ascii

* if u want to retain unicode (while file writing)

```python
with open('file','w') as fd:

    fd.write(unicode_string.encode('utf-8'))
```

```
in python2,
   str is actually a byte-string.
   unicode is an array of unicode-points.
    so we use .encode() .decode()
    python2 automatically tries to decode/encode by def to ascii - so you get all those errors
in python3,
   str is an array of unicode-points
   bytes is a array of bytes.
```


## bytes

```
defined as b'\xfe' or b'abc'

a=b'\x65\x48'        # a bytes object
a.decode('ascii')    # gives a string object.
                     # encode/decode complement bytes/str conversion
```

bytes like string is immutable
bytearray is mutuable

## Extra Extended Datatypes from Collections

* collections.deque
   * like list, but has front and back at O(1)
* collections.orderedDict
   * A bit useless. Order is maintained on insertion order of keys.
   * This is more standard than the SortedContainers below. So use this if it solves the purpose
* SortedContainers.sortedDict
   * A proper dict based on key.
   * Looks like there is getNextAfterKey()/..Before.. [use bisect() and peekItem()]
   * python3 use - sortedcontainers.SortedDict
* llist.dllist
   * A doubly linked list in python. If you really wanted a linked list.

## General Summary on sequence types

* list, tuple and collections.deque can hold items of different types.
    * hold reference to items they contain
* str, bytes, bytearray, memoryview and array.array hold items of one type.
    * physically store the objects they contain

Mutable:
* list, bytearray, array.array, collections.deque, memoryview
* tuple, str, bytes

# control structures

```python
if condition:
  ...
elif next_condition:         #python's else if style
  ..
else
  ..

with lists.
  Use range function to run over a range.
  range(start-value, end-value+1, increment)

#loops
for i in list:
  ..use i..

for i in range(1,10):
  ..use i..

break
continue

# use this to get a convenient index as well
# you can override start value as well.
for n,i in enumerate(iterable,start_value=0):
    do_whatever(n,i)

#limit for loop to a number
for i in itertools.slice(iter,0,limit):
    use(i)
```

* Want to iterate over 2(or more) lists of the same length simulataneously?
  *  Keep them as one list of tuples!
    ```python
    student=['s1','s2','s3']
    mentor=['m1',m2','m3]
    count = 0
    for s in student:
      print s,m[0]

    can instead be:

    student_mentors=[('s1','m1'),('s2','m2'),('s3','m3')]
    for (s,m) in student_mentors:
      print s,m
    ```


## logical operators

and
or
not


## variable args to function

```python
def manyArgs(arg1, arg2, *args, **kwargs):
  #arg1, arg2 are std args
  #args is a tuple of all unnamed args
  #kwargs is a dict of all named args
```

* Its also possible to use this other way around
  Search: expand arg list function

```python
def fun(arg1, arg2)
    #regular fun using arg1, arg2
    pass

a=[1,2]
dict_b={'arg1':1, 'arg2':2}
func(*a)
func(**b)
```

## swap 2 variables

```python
a,b = b,a
```

# More pythonic constructs

## source-code has utf-8 chars

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
```


## class

```python
class Name:
  #There is no explicity declaring of members

  count = 0                     # Can be used like static in c++, but see notes below

  def __init__(self,arg1,arg2):
    self.member1=arg1           #automaticaly adds member1 as a field to the class objects.
    self._convention_priv_member = 2
                                #use _beginning names to mean its private. Only convention.

  def function(self,arg1):
    pass                        #all member function's first arg is self.
    self.anotherMember(arg2)    #remember to put the self before calling another member from member
    Name.count++;               #refering a Name.member brings in a c++-style static member of the class.

  @staticmethod
  def function(arg1):
    pass                        # note the absence of self for static member functions. Invoked as ClassName.function()
    Name.count++;               #refering a Name.member brings in a c++-style static member of the class.

  @classmethod
  def function(cls, arg1):
    pass                        # here the first arg is the Class itself. To illustrate, this is like doing type(self).access
    cls.count++;                # from a regular class. The cls is a convenient first arg. Has the adv of not having to edit
                                # the function text if the classname (Name in this case) changes.

  @property                     # kind of automatically makes this a getter fn
  def member_name(self):            # for the member.
    return self._member_name    # Mind you users now do obj.member_name
                                # instead of obj.member_name()

  @member_name.setter           # similarly for setter.
  def member_name(self, value):
    self._member_name = value

#Later..
n = Name(10,12)
```

* The attributes of a class are kind of public. No data-encapsulation.
* In fact, attributes of a class can be added at will anytime. There is really no
  fixed-set of attributes for a class
  n.newAttribute = "abc"   # is perfectly valid anywhere!
* ClassName.var_name
    * when used with ClassName refers to a var_name in class-scope(static like)
    * DONT FORGET the ClassName - otherwise, it just uses/refers to a local var.
* methods in the class can work on static members as long as they use ClassName to scope it.
* But instance_var.var_name  # when assigned to, will create a instance level attribute!

```python
class Derived(Base):
  def __init__(self, derived_args):
    Base.__init__(self, base_args)
    self.derived_member = derived_args

  def overriddenMethod(self, args):
    super(Base, self).overriddenMethod(args)
    moreWorkHere()
```

### Magic attributes of a class

```python
n.__class__    # reference to a object of type class, which represents the class-definition.
               #  this is how you do typeof() in python
n.__doc__      # reference to the doc-string
n.__repr__     # is a function, that will used to stringize the class.
               # Tip, it takes mandorty self, u can actaully pass more args
               # as long as u have default-args.

#search attribute set attr set_attr has_attr
hasattr(object, "member")  # check if object.member exists
getattr(object, "member")
setattr(object, "member", "value")
```

* object id
```
id(anyobject)  # gives a unique id for th object

```


## Global scope

```python
var  = 5;     #global scope - outside of any function

def func():
  global var
  var = 6        #updates global var as it explicity mentiond

def func2()
  var = 6        #silently creates a local var and uses that. Doesn't reflect glboal var.
```

## lambda

```python
lambda arg1 [, arg2,..]: manipulate(args)
```

## map

Gives a generator, where the given fn is applied on the list provided.

```python
map (fn_to_apply, list_of_inputs)
```

useful example:

```python
#convert a list of hex string into int numbers
data = map(lambda x: int(x,16), data)
```

## Iterators

* A class that implements __iter__ , which returns a object that implements __next__
* Typically its customary to return self in __iter__ and implemen __next__
* User calls next() and gets StopIteration error at end.


## generator

* Is a function (defined with def Name():)
* But has a yield statement in it.
* You have to first create a object by calling generate_name() [read, generate_name param param]
    * Note, calling a normal funciton returns whatever the function gives.
    * Calling a generator function, returns, well a generator.
        * You have to use the .next() on it to make sennse.
* Later you call gentr.next() to start getting values out of it.
* When its done, you get StopIteration thrown (This happens when generator code falls off its def block)
* On actual invocation (creation of object), no code gets executed.
* On first next, code gets executed till yield which is returned outside
* On susequent next()'s, code continues from yield till yield is hit again. Note taht all vars in
  the def block remember their values
* When code falls off the def-block, we get StopIteration thrown to the next() caller.

```python
# a generator that yields items instead of returning a list
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(1000000))
```

## Generator expressions

* syntactically different form Comprehension with a parenthesis!
* Generators are cheaper than comprehension as the list isn't created right away

(expression for i in origList)

## closures

* A (typically anonymous) function that takes arguments (like normal function) and has a state inside it.
* The state is set up in the closure at the time of its creation.
* The closure can mutate its state during every invocation
* Multiple instances of the same closure function can have different states.
* At the outset, you will see a function having a inner function, and returning the inner function

A closure is typically created like this

```python
def create_a_closure(state1_for_closure):
  state2_for_closure = "some_initial_value"
  def my_closure(closure_arg1, closure_arg2):
    result = work_on(state1_for_closure, state2_for_closure, closure_arg1, closure_arg2)
    state1_for_closure = "new_values"  # Note this state was setup at closure create time (call of create_a_closure)
    state2_for_closure = "new_values"  # Note this state was setup at coding time
    return result
  return my_closure

#Later
a_closure = create_a_closure("intial_value_for_state1")
```

## decorators

* The intent of a decorator is to wrap around any function with added behavior
* You write a closure like situation, where a function takes one function as arg, which defines a inner funciton and returns it.
* The inner funciton does fancy stuff (and calling the actual supplied function)
* Later you can just use the decorator syntax
    ```python
    def decorator_name(original_func):
        def some_inner_non_exposed_meaningful_name(*args, **kwargs):
            optional_items = do_fancy_stuff()
            result = original_func(optional_items, *args, **kwargs)
            result += more_fancy_stuff_if_be()
            return result
        #note you return the fn-object - not call it!
        return some_inner_non_exposed_meaningful_name

    # now call it as:
    @decorator_name
    def function_that_will_be_wrapped(...):
      ...

    #users later call just, but fancy works happen!
    a = function_that_will_be_wrapped(..)
    ```
* Users just invoke normally with function_that_will_be_wrapped() and that gets wrapped by the decorator

## itertools

```python
itertools.permutations(iterable, size_to_work)
itertools.combinations(iterable, size_to_work)
itertools.product(iterable, iterable)           -> (1,a), (1,b), (1,c), (2,a), (2,b), (2,c)
itertools.groupby(iterable,keyfunc)             -> listof (keyvalue, sub-iterators) Note: given iterable Must be already sorted/sub-sorted.
itertools.chain(it1,it2,..itn)                  -> single iterator that goes over all
itertools.zip(it1,it2,..itn)                    -> gets a list of tuples that goes over all iterables. Stops at shorted.
itertools.zip_longest(it1,it2,..itn)            -> ..zip till longest, filling None for thse that are over.
itertools.izip(it1,it2,..itn)                   -> single iterator(instead of a list) that goes over tuples of members of all iterables. Stops at shorted.
itertools.izip_longest(it1,it2,..itn)           -> ..zip till longes, filling None for thse that are over.

#infinte iterators
itertools.cycle(iterable)                       -> keeps cycling on the iterable endlessly

reversed(iterable)                              -> native way to reverse any interable
```

# asyncio

## common asyncio statements

```py
await asyncio.sleep(1)

```


## subprocess

https://docs.python.org/3/library/asyncio-subprocess.html

```python
import subprocess

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
                        cmd,
                        stdout=asyncio.subprocess.PIPE,
                        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')

asyncio.run(run('ls /zzz'))


## regular subprocess
#### Most quick and useful
completedProcess=subprocess.run("ls -l /var/log", shell=True, capture_output=True)
print ("stdout was:%s"%completedProcess.stdout)
print ("stderr was:%s"%completedProcess.stderr)
print ("exit code was:%s"%completedProcess.returncode)

# run it natively w/o shell.
cmd_in_list=['ls', '-l', '/var/log']
completedProcess=subprocess.run(cmd_in_list, capture_output=True)

# each command is one invocation to Popen, with its stdout/stderr set to the previous commands pipe.
# You can use subprocess.PIPE to ask popen to give you a pipe. THis is obtained by a call to communicate.
# the wait will wait till the command is done. errcode is the process return code. 0 if success, non-0 iff ailure
# The result of communicate is like a string, ready for processing.
# You can stack as many commands with a pipe arrangement.

# To do this following
#   ls *.mp3 | grep MS
from subprocess import Popen, PIPE
ls_process = Popen(['ls', '*.mp3'], stdout=PIPE)
grep_process = Popen(['grep', 'ms'],stdin=ls_process.stdout, stdout=PIPE)
ls_process.stdout.close() # enable write error in ls if grep dies
out, err = grep_process.communicate()

#if you dont want to pass to stdin
a=subprocess.Popen(["ls","-l"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output,err=a.communicate()
errcode = a.wait()
print output

#if you have a  stdin to poass
a=subprocess.Popen(["ls","-l"],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output,err=a.communicate(input="Whatever you want to pass")
errcode = a.wait()
print output



# older versions for py2
subprocess.call(["ls","-l"])   # Just run it clobbering ur stdout with the cmd's stdout.
output = subprocess.check_output(["ls","-1"])  # Run and get the o/p as return value
                                               # But stderr will still clobber your stderr

finished_result=subprocess.run(["ls","-l","file"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
finished_result=subprocess.run(["ls","-l","file"],...,stdin="some-string")
finished_result.returncode
finished_result.stdout
finished_result.stderr
```



# Python Internals

Every name you see is a reference/pointer to an object.
The underlying object is either an immutable object or a mutable object.

## Import path

sys.path is the list of locations looked for imported modules

## Python library mgmt

Typically python stores all its libraries in

/usr/local/lib/python<ver>/site-packages
/usr/local/python<ver>/dist-packages

sudo apt-get install python-pip

and then

```sh
pip install <blah-blah>
```

or if u get the source

```sh
cd the-new-stuff
python ./setup.py install   # use the right python-version to install in its location

#List all installed libraries.
pip freeze

#list all files installed in a package
pip show -f <package>
```

## Python Interpreter notes

Use underscore to capture last value

```python
>>> 5 + 6
>>> a = _
```

### Get interpreter in between

```python
import code
code.interact(local=locals())
```

### reload a module in interpreter

```python
#import again / re import / reimport
reload(module_name)

#python3
import importlib
importlib.relaod(module_name)
```


# Simple commands

```python
print()   # also prints a "\n" at end of string

print "happy arg:%d"%arg,  # the trailing comman skips the newline

print('.',end="",flush=True)   # to control "\n" and flushing  .. only in python 3
sys.stdout.flush()  # in python 2

print('string',file=sys.stdout)  # to a file
```

## formating

https://pyformat.info/

```python
string.format(args)
'{0} {1:2d}'.format(s,i)
'{0:b}'.format(i)               # is a quick way to print a number in binary
```

* By default format calls __format__ of the object.
* Use !r !s or !a to call __repr__, __str__, ascii()
* {0!r:}
* align right/left/center : `> , -, ^`

```python
{<arg-position><convertion-flag>:<padding-char><align><width>.<trunc-width><type>}  # default type is string
```

## print function for v2

```python
# use this and use print statement.
from __future__ import print_function

print "format string %d, %s, %s"%(int_var,str_var,"string literal")
```


## Error handling/Exception

```python
# usual copy paste for your error
# replace the Exception wth your choice of error

def your_fn():
    ...
    try:
        whatever()

    #copy paste from here:
    except Exception as e:
        logging.error("Got error: %s", e)
        resp = None
    finally:
        #always gets executed


#printing stack-trace at exception
import traceback

    except Exception as e:
        e.whatever..
        e.errno
        e.strerror
        var = traceback.format_exc()

```

* Typical Types of Error


```python
except IOError:
except FileNotFoundError:
```

### note

* Note its except and not expect
* No one defines what exceptions will be raised. We handle every possible exception
* keyword to throw in python is raise
    ```python
    def function():
      ...;
      if problem:
        raise IOError;
      ...;
    ```
* Exception is a grant root of all excetions. So it Capture all Exceptions!
    ```python
    except Exception,e:
        print str(e)
    ```
    * As a fallout - if you write a Exception class inherit from Exception

## Reading file line by line


```python
with open("file","r") as fp:
  for i in fp:                  # This is efficient on large files. so *ok for big files*
    print(i)

with open("file","r") as fp, open("second-file","r") as fp2:   # for multiple files

f.readlines()   # gives each line of file in a list.. Note: Entire file is gobbled in one-go. Useful *only for small files.*
f.read()        # gets entire file as one big string. Again, use for small files only.

Reading line by line from stdin:

import fileinput
for line in fileinput.input():   #this one will pick stdin or if some arg(s) is/are given, it will open that as a file!
  pass

fls=('a.txt','b.txt','-')
for line in fileinput.input(files=fls):
  pass

import sys
for line in sys.stdin:
  print line

for line_number, line in enumerate(fd):   # will also get line-number along
```

* Possible exceptions
    * FileNotFoundError

### Reading N lines

```
with open(filename, 'r') as infile:
    lines = [line for line in infile][:N]

from itertools import izip_longest

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)

with open(filename) as f:
     for lines in grouper(f, N, ''):
         assert len(lines) == N
         # process N lines here
```


## To find if a variable is a list/scalar

```python
if isinstance(var_name, list):
```

## User input (from stdin, keyboard)

```python
#what you probably need most of the time
variable=raw_input("Prompt string w/o newline:") # Gets whatever is given and assigns to variable which is now a str. You then cast this string into whatever you want.

# in python3, raw_input is input

#also know:
variable=input("Prompt string w/o newline:")     # Gets user-input and interprets it as a python-expression! Thus unquoted string-literals are interpreted as var-names
                                                 # Most likely not what you want. But if you type in a int, your variable also holds a int-object directly.

# if you need from a choice:
def askUser(choices=(1,2,3),max_attempts=5):
    attempt = 0
    while True:
        try:
            choice = int(raw_input("Do you want: \n(1) Bread \n(2) Butter \n(3) Jam \n:"))
            if choice not in choices:
                print("That is not a valid choice. your choices are %s"%choices)
            else:
                return choice
        except ValueError:
            print("Please input a number")
        attempt += 1
        if attempt >= max_attempts:
            raise Exception
```

### password input

```python
from getpass import getpass
password = getpass('Optional Prompt:')
```


### Use readline library

```python
import readline
import atexit

def rlinput(prompt, prefill=''):
  readline.set_startup_hook(lambda: readline.insert_text(prefill))
  try:
    return raw_input(prompt)
  finally:
    readline.set_startup_hook()

historyPath = os.path.expanduser("~/.pyhistory")

def save_history(historyPath=historyPath):
    import readline
    readline.write_history_file(historyPath)

if os.path.exists(historyPath):
    readline.read_history_file(historyPath)

atexit.register(save_history)
```

## Find python version

python -v

## To make a script run if its main

```python
if __name__ == "__main__":
    main()
```

## Simple TCP client to send binary info


```python
import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("169.254.69.1",6005))
f="testfile"
m="aaa"
hdr=struct.pack("II128s33sBBBI",32,16,f,m,1,0,0,0)
s.send(hdr)
```

### send data in f-ack

```python
import socket
s = socket.socket()
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_QUICKACK, False)
s.connect(("10.1.1.2",80))
s.send(b"GET / HTTP/1.1\r\nHost: 10.1.1.2\r\n\r\n")
print(s.recv(1024))
```

## Simple UDP server in python

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host="127.0.0.1"
port=19999
s.bind((host, port))

#block till a pkt
(data, addr) = s.recvfrom(128*1024)

```

## signal handler

```python
import signal, os

def handler(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
```


# Various Python Libraries

## Arg parse

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v","--verbose", help="increase output verbosity", action="store_true")       # captures if --verbosity present or not in arg-list. No arg per-se for this option.
parser.add_argument("-v","--verbose", help="increase output verbosity", action="count")            # captures how many times --verbosity was present in arg-list. No arg per-se for this option.
parser.add_argument("-v","--verbose", help="increase output verbosity", type=int)                  # --verbosity <int>
parser.add_argument("-v","--verbose", help="increase output verbosity", type=float)                  # --verbosity <int>
parser.add_argument("-v","--verbose", help="increase output verbosity", type=int, choices=[0,1,2]) # --verbosity <0|1|2>
parser.add_argument("-l","--long-arg", help="repeats", nargs="+", required=True)                   # -l arg1 arg2 arg3  .. flipside: cant distinguish positional args from args to this option
parser.add_argument("-L","--long-arg2", help="repeats", type="append")                             # -l arg1 -l arg2 -l arg3 .. better.
parser.add_argument("str_arg",   help="give a string argument (this is a mandatory argment)")
parser.add_argument("int_arg",   help="give a int arg (this is a mandatory argment)", type=int)
parser.add_argument("optional",  help="User may skip this", nargs="?", default="abc")
parser.add_argument("many_optional", help="User may give zero or  more of this and this will be a list", nargs="*", default=["a","b"])
if cmd_options.verbose:
    print("verbosity turned on")

# dash- is converted to underscore

# COPY THIS for fresh scripts!!
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("server", help="server")
    cmd_options = parser.parse_args()
    return cmd_options

also:
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")

#to explicitly print help
parser.print_help()
```

### argc/argv example

```python
if len(sys.argv) < 2:
    sys.exit('Usage: %s database-name' % sys.argv[0])

if not os.path.exists(sys.argv[1]):
    sys.exit('ERROR: Database %s was not found!' % sys.argv[1])
```

### nifty use of argparse.Namespace

* Convert dictionary to a object which can access its
  keys as member-names
* It wont convert nested dictionaries. Just top-level.

```python
from argparse import Namespace
ns = Namespace(**mydict)

#and reverse (this is just pythonic):
mydict = vars(ns)
```


## exiting from python

sys.exit(0)

## environment variables

os.environ['HOME']

## regular expression  regexp regex

```python
import re
m =  re.search (pat, haystack)   # m is a match object or a None

m.group()  # gets the matched string
m.group(1)  # gets the 1st left paren group.

a = re.findall (pat, haystack)  # gets the list of all matches.. if he pat has (), then it gets back a list of tuples

a = re.sub(pat,replacement,src_string,count=0,flags=0)  # replace can use \1 to backref.

#remove invalid filename chars for windows
valid_filename = re.sub(r'[\\/:"*?<>|]+', "_", var_having_junk_chars)

# if u are using a regex a lot, pre-compile it

flags:
re.IGNORECASE

pat_object = re.compile(pattern,flags)
pat_object.search(haystack)
pat_object.match(check_exact_match_input)
```

### character classes

use r'...' to represet a regex for python to preserve the back-slashes

\s   - space
\S   - non-space
()   - imply group. Use \( if u want to match a literal (


## os-package (file manipulation stuff)

```python
os.path.join(dir,filename)
(dirname,filename) = os.path.split("abc/efg/file")       # dirname basename
(filename,extension) = os.path.splitext("filename.ext")  # note the spelling split-ext
os.path.abspath(path)
os.path.realpath(path)  # resolves sym-links!
os.path.exists('path/to/file')      #file check present
os.makedirs(path)   # it will create all dirs in path if needed.
                    # But the last dir MUST be non-existant.
                    # You can either check isdir() before, or catch FileExistsError
os.getcwd()         # get cwd pwd
os.chdir(path)      # cd to a working-dir
os.path.dirname(os.path.realpath(__file__))   # get dir of current file

os.path.isfile('path')  # true if its regular file or sym-link to regular file, if [ -f file ] check in sh
os.path.islink('path')  # true if its a sym link
os.path.isdir('path')   # true if its a dir or a sym link to a dir, -d

#get home folder
homefolder = os.path.expanduser("~")
anyfolderunderhome = os.path.expanduser("~/.pyhistory")

# create/make a new dir , mkdir -p
if not os.path.exists(directory):
    os.makedirs(directory)

os.rename(src,dst)   # mv in python

os.unlink(dst)  # rm a file , delete
os.remove(dst)  # unlink/remove are the same

shutil.rmtree(dir_with_contents)  # just delete a dir / folder with contents
shutil.copyfile(src,dst)          # file copy / cp

#if you just want contents copy
def copycontents(src,dst):
    with open(dst, 'wb') as output, open(src, 'rb') as input:
        shutil.copyfileobj(input, output)

# for quick and directy commands. Command o/p comes to stdout.
# search : subprocess
os.system("your command with all args in a single string")

boolean_variable=os.access("/path/to/file",os.F_OK)  # does file exist at all
boolean_variable=os.access("/path/to/file",os.R_OK)
boolean_variable=os.access("/path/to/file",os.W_OK)
boolean_variable=os.access("/path/to/file",os.X_OK)
```

### To recursively walk a dir

```python
# os.walk gives a generator that recurses into dirs.
# So our code looks nice and iterative!
for subdir, dirs, files in os.walk(a_given_dir):
  print "files in %s"%subdir
  for f in files:
    fname = os.path.join(subdir, f)
    print(fname)
  print "dirs in %s"%subdir
  for f in dirs:
    fname = os.path.join(subdir, f)
    print(fname)
```

* To just list one level

```python
os.listdir(given_dir)

#To filter only dirs:
[ name for name in os.listdir(given_dir) if os.path.isdir(os.path.join(given_dir, name)) ]

#using fnmatch to match glob expressions
import fnmatch
[ name for name in os.listdir(given_dir) if fnmatch.fnmatch(name, '*.txt') ]

or

import glob
list_of_filenames=glob.glob("*.py")

import sh
a=sh.ls('-1','.')

# to recursively match filenaes

import fnmatch
import os

matches = []
for root, dirnames, filenames in os.walk('src'):
    for filename in fnmatch.filter(filenames, '*.c'):
        matches.append(os.path.join(root, filename))
```

* Curated external-command execute  -- see my_python_util.py

### File locking


```python
import fcntl
x = open('foo', 'w+')
fcntl.flock(x, fcntl.LOCK_EX | fcntl.LOCK_NB)
Unlocking is just as easy:

fcntl.flock(x, fcntl.LOCK_UN)
```

### Temp file

```python
import os
import tempfile

fd, path = tempfile.mkstemp()
try:
with os.fdopen(fd, 'w') as tmp:
# do stuff with temp file
tmp.write('stuff')
finally:
os.remove(path)
```

## random

```python
random.seed([x])    # x is any hashanble object. if none is passed, sys-time is used.
random.shuffle(x)   # shuffles list x in place.
random.randint(a,b) # get a random int from [a,b], both included
random.sample(iterable,k=1)  # gets a k-sized tuple of items from iterable.
```


## time

```python
>>> import time
>>> st_mtime=1247520344.9537716
>>> time.localtime(st_mtime)
time.struct_time(tm_year=2009, tm_mon=7, tm_mday=13, tm_hour=14, tm_min=25, tm_sec=44, tm_wday=0, tm_yday=194, tm_isdst=1)
>>>

#sleeping in python
from time import sleep
sleep(0.1) # Time in seconds.
```

### datetime

https://stackabuse.com/how-to-format-dates-in-python/

```python
#Note: datetime module has 2 objects - date  and datetime. (And a timedelta)

datetime.date.today()
datetime.datetime.now()    # same as today, but can accept a tz as optional name arg

datetime.datetime.strptime('time-in-string','format')   # read a time in a string in.
datetime.datetime.strftime('format')                    # print a time in a string

%d - 0 padded 2 digit date
%m - 0 padded 2 digit mth
%Y - 4 digit year
%H,%M,%S - 24-hr,min,sec as 0-padded-2-digit-numbers
%I - 12hr, %p - "AM"/"PM"
%a - 3 alpha weekday
%b - 3 alpha month
%Z - time-zone

%s - get seconds since epcoh #Undocumented. Might work or not.

## initialize from epoch
datetime.datetime.fromtimestamp(123132112)
datetime.datetime.fromtimestamp(0)           # initialize from 0-epoch.

datetime.timedelta is returned when you subtract 2 datetime.datetime objects

date = datetime_obj + datetime.timedelta(days=30)

#create a datetime - yr,mth,date are mand. hr, min, sec, micro-sec, tz are opt.
datetime.datetime(2019, 1, 19)

#convert datetime to date
datetime_object.date()

#to get time in seconds since epoch
time.mktime(datetime.datetime.now().timetuple())

 eg: linux date o/p , and its string format
     a=datetime.datetime.strptime("Mon Dec 11 20:08:01 UTC 2017","%a %b %d %H:%M:%S %Z %Y")

##timedetla in days, hours, minutes, seconds
def days_hours_minutes(td):
    return td.days, td.seconds//3600, (td.seconds//60)%60, td.seconds%60
## initialize timedelta
datetime.timedelta(days=10)
datetime.timedelta(seconds=3600)
datetime.timedelta(minutes=15)
datetime.timedelta(hours=3)

```

## Enums /enum

```python
from enum import Enum

class Color(Enum):
  Red = 1
  Yellow = 2

#Iterate over all enums
for c in Color:
  print (c)         # will print Color.Red, Color.Yellow

#To get string/number against a enum
Color.Red.name
Color.Red.value

#if u have number, to get enum object
Color(1)

#if u have string, to get enum object
Color['Red']
```


## urllib

```python
import urllib

uf = urllib.urlopen('http://google.com')
file_page = uf.read()

urllib.urlretrive('http://google.com/intl/en_ALL/images/logo.gif', 'blah.gif')

import urllib2, base64

request = urllib2.Request("http://api.foursquare.com/v1/user")
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)
result = urllib2.urlopen(request)
```

## requests

```python
url='https://api.github.com/user'
user='username'
pass='password'
r = requests.get(url, auth=(user, pass))

dictvar = requests.utils.dict_from_cookiejar(cookiejar)
cookies = requests.utils.cookiejar_from_dict(dictvar)
```

### Post a json object

```python
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}

response = requests.post(url, data=json.dumps(payload), headers=headers)
```

### To supress warnings

```python
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
```

## beautiful soup

```python
#pip install beautifulsoup4
import bs4

soup = bs4.BeautifulSoup(html_data,'html.parser')
#or
with open("local_file","r") as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')

# Look at the parts of a tag
tags = soup('a')
first_tag = tags[0]
print 'TAG:',first_tag
print 'URL:',first_tag.get('href', None)
print 'Contents:',first_tag.contents[0]
print 'Attrs:',first_tag.attrs

#find by id
elem = soup.find("div", {"id": "articlebody"})

#find by class
mydivs = soup.findAll("div", {"class": "stylelistrow"})
#find ANY matching class
mydivs = soup.findAll("div", {"class": ["classVal1", "classVal2"]})
#find ALL matching classes. This works only for classes. The above
#work for any attribute of the element-type
mydivs = soup.select("div.classVal1.classVal2")

#find only one level
li_items = ol_item.findAll("li", recursive=False)

#check if a element has an attribute
# all attrbutes are in dict attrs
if 'some_attribute' in div_elem.attrs
# .. check if is some value is present in a attribute
if 'className' in div_elem.attrs['class']

#walk over a table
rows = soup.find("table", border=1).find("tbody").find_all("tr")
for row in rows:
    cells = row.find_all("td")
    rn = cells[0].get_text()         # textContent

#pretty
soup.prettify()
```

4 types of objects

Tag, NavigableString, BeautifulSoup, and Comment.

## XML/xml

Element:
    * tag - name
    * attribue - name/value paris
    * context - text
    * can have subelements to any depth
    * xml can have only one root.

```python
import xml.etree.ElementTree as etree
tree = etree.parse('file_having_xml.xml')
root = tree.get_root()  # root if of type Element
```

* element.tag is its tag
* children are lists. This way element is an iterable
* element.attrib is a dict
* element.txt is its content

```python
import lxml.etree
parser = lxml.etree.XMLParser(recover=True)
mytree = etree.parse('pg_src', parser)
parser.error_log

all_a = mytree.findall("//{http://www.w3.org/1999/xhtml}a")
for i in all_a:
    if 'href' in i.attrib:
        print i.attrib['href']

lxml.etree.tostring(element)

import xml.dom.minidom
xml.dom.minidom.parseString(lxml.etree.tostring(mytree)).toprettyxml()
```

## Selenium

* Download chrome driver from google - https://sites.google.com/a/chromium.org/chromedriver/home
* pip install selenium lxml csselect

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import bs4
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url)
src=bs4.BeautifulSoup(driver.page_source,'lxml')
with open('/tmp/a.html','w') as fd: fd.write(src.prettify())
src=driver.find_element_by_class_name('searchBox')
src
src.clear()
src.send_keys("123650")
src.send_keys(Keys.RETURN)

pg=driver.page_source
souped=bs4.BeautifulSoup(driver.page_source,'lxml')
with open('/tmp/a.html','w') as fd: fd.write(souped.prettify())

elem=driver.
l = driver.find_elements_by_class_name("gwt-TabLayoutPanelTab")
for n,i in enumerate(l):
    print('{} . {}'.format(n,i.text))
elem=l[10]
elem.click()
pg=driver.page_source
souped=bs4.BeautifulSoup(driver.page_source,'lxml')
with open('/tmp/a.html','w') as fd: fd.write(souped.prettify())
elem=driver.find_element_by_class_name('displayXML')
elem.text
```

## Simple http server

* Dishes out files in its cwd too!

```python
#python2
python -m SimpleHTTPServer 8080

#python3
python3 -m http.server 8080
```

### SSL stuff

https://www.electricmonk.nl/log/2018/06/02/ssl-tls-client-certificate-verification-with-python-v3-4-sslcontext/
https://stackoverflow.com/questions/19705785/python-3-simple-https-server

```py
from http.server import HTTPServer,SimpleHTTPRequestHandler
import ssl

server_cert="server.crt"
server_key="server.key"
cafiles="site-root.crt"

httpd = HTTPServer(('localhost', 1443), SimpleHTTPRequestHandler)

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=server_cert, keyfile=server_key)
# these 2 lines are needed only for mutual tls
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations(cafile=cafiles)
httpd.socket = context.wrap_socket (httpd.socket, server_side=True)
httpd.serve_forever()

```


## pickle

* Just use json instad!

```python
pickle.dump(object_to_dump, write_file_handle)

ob = picke.load(read_file_handle)
```

## pexpect

```python
child=pexpect.spawn("cmd",["arg1","arg2"])
try:
  result=child.pexpect(["regex1","regex2"], timeout=120)
  #result is 0-based index in the list
  #unfortunately EOF and TIMEOUT are always exceptions
except pexpect.EOF:
  #pass
except pexpect.TIMEOUT:
```
* See my_python_util.py for a general wrapper

## logging

```python
import logging
logging.basicConfig(filename="abc.log", level=logging.DEBUG)
# mode='w', will erase existing log file
# DEBUG, INFO, WARNING, ERROR, CRITICAL, FATAL

logging.debug("This is a debug message")

sess_logger = logging.getLogger("SESS")
sess_logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('session.log')
fh.setLevel(logging.WARN)
sess_logger.addHandler(fh)
sess_logger.debug("This is a session subsystem log")
```

* Note: logging defers calling the arg's __str__ function. Do

logging.debug("This is fmt - %s and %s", some_object1, some_object2)
The actual invocation of some_object1.__str__() doesn't happen if debug level is diabled.

* However, if u are calling a function as arg, then you might have to do this:

```
#lazy_eval
class lz:
    def __init__(self, callback, *args, **kwargs):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs
    def __repr__(self):
        return repr(self.callback(*self.args, **self.kwargs))

def expensive_function(marg1, oarg1=1, oarg2=2, nmarg1=0, nmarg2=2):
    print(f'expense {marg1}, {oarg1} {oarg2} {nmarg1} {nmarg2}')

def another_expensive_function():
    print("expensive")

logging.debug("%r", lz(expensive_function, 5, 6, nmarg1=10) )
logging.error("%r", lz(expensive_function, 5, 6, nmarg1=10) )
logging.debug("%r", lz(another_expensive_function))
logging.error("%r", lz(another_expensive_function))
```

### syslog

```python
import syslog
syslog.openlog(ident="Remote-ssh", logoption=syslog.LOG_PID, facility=syslog.LOG_LOCAL3)
syslog.syslog(syslog.LOG_INFO, "Done with remote ssh:%d"%sshpid)

```


## Context-manager

```python
@contextmanager
def change_dir_to(new_dir):
  current_dir = os.getcwd()
  os.chdir(new_dir)
  yield
  os.chdir(current_dir)
```

if your have thing.close() to do post yield:
```py
from contextlib import closing

with closing(socket.socket(socket.AF_INET, socket.SOCK_DGRAM)) as s:
    s.send(...)
```


## Daemonizing

pip install python-daemon

```python
import daemon

with daemon.DaemonContext():
    #whatever u want to daemonize
    main()
```

## csv


```python
import csv

with open("file_name.csv") as fd:
    csv_lines = csv.reader(fd)
    for row in csv_lines:
        print("col-0:%d col-1:%s"%(row[0],row[1]))

```

For writing

```
c = csv.writer(filehandle_from_open)
c = csv.writer(f, quoting=csv.QUOTE_ALL)
```

## excel to csv

```python
import openpyxl
import csv

def xls_to_csv(infile, outfile):
    wb = openpyxl.load_workbook(infile)
    sh = wb.active
    with open(outfile, 'w', newline="") as f:
        c = csv.writer(f)
        for r in sh.rows:
            c.writerow([cell.value for cell in r])

```

## Json

```python
import json

# from file
with open(json_file, 'r') as fd:
    obj = json.load(fd)
# from string
obj = json.loads(str_var)

#put an arbitrary phttps://pyformat.infoeython object as string
# Not all built-in python objects are convertible, but not user-defined objects
str_var = json.dumps(obj)
#pretty print json
str_var = json.dumps(obj, indent=4, sort_keys=True)

#for file
json.dump(obj, fd)
json.load(fd)
```

## yaml

* link: https://yaml.readthedocs.io/en/latest/basicuse.html

```python
import yaml

# from file
with open(yaml_file, 'r') as fd:
    obj = yaml.load(fd)
# from string
obj = json.safe_load(str_var)
pyobj = yaml.load(fd)

# to_string
#  default_flow_style
#    False  :  line-breaks used
#    True   :  dicts,lists are maintained on same line with [],{}
str_var = yaml.dump(data, default_flow_style=False)
```


## sha1

```python
def sha1file(filename):
    sha1=hashlib.sha1()
    size=65536
    with open(filename,'rb') as fd:
        while True:
            data=fd.read(size)
            if not data:
                break;
            sha1.update(data)
    return sha1.hexdigest()
```


## Curses

* window - is an internal representation containing an image of a part of the screen.
* screen - is a window with the size of the entire screen (from the upper left to the lower right)
* WINDOW stdscr - standard screen


## colorprint

```python
color_dict = { 'Black':0, 'Red':1, 'Green':2, 'Yellow':3,  'Blue':4,    'Magenta':5, 'Cyan':6,    'White':7 }

CSI='\033['
reset='\033[0m'

normal_foreground=30
normal_background=40
high_foreground=90
high_background=100

                          # foreground                        #background
chosen_color_prefix = CSI + str(30+color_dict[color]) + ';' + str(40+color_dict[color]) + 'm'

#in 256 color format

#foreground
chosen_color_prefix = CSI + '38;5;' + str(color_num) + 'm'
#background
chosen_color_prefix += CSI + '48;5;' + str(color_num) + 'm'

from colorama import Fore, Back, Style

colorama.init()
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
```

## Scapy

http://www.secdev.org/projects/scapy/files/scapydoc.pdf

* Look further in scapy.py file

## psutil

```python
import psutil

#collect all pros
ps = [ p for p in psutil.process_iter() ]

#collect  process with matching names
name="zsh"
ps = [ p for p in psutil.process_iter() if name in p.name() ]

#collect process of user
user="lakshman"
ps = [ p for p in psutil.process_iter() if user in p.username() ]

#collect uniq users
users = { p.username() for p in psutil.process_iter() }

#count ps per user
d=collections.defaultdict(int)
for p in psutil.process_iter() : d[p.username()] += 1

#if you have pid, get the process
p = psutil.Process(pid)
#and get anything of it (pid is field, everything else are functions())
#   you get psutil.Error if pid no longer exists!
p.pid
p.ppid()
p.name()
p.cmdline()
p.exe()
p.terminal()
p.cwd()
```

## Fuzzywuzzy

```python
import fuzzywuzzy

#Get a match from a list
choices=[....]
list = fuzzywuzzy.process.extract(choices, 'mylookup')
# you get a list of (string,ratio)
better_results = [ i[0] for i in list if i[1] > 70 ]

#get a ration
a='string1'
b='string2'
ratio = fuzzywuzzy.fuzz.ratio(a,b)
#ratio is 0.0 to 100.0
```

## Progress bar

```python
import tqdm

# i dont get this fully on how it auto-computes len()
# wrap it on any iterable.. how does it get len() ?
for i in tqdm.tqdm(range(10000)):
    pass

#explicitly pass the total
for i in tqdm.tqdm(myiter, total=10):

#for a changing message before the bar.
tqdm.setdescription("some string")
```


## ipython

%rerun <num>


## Virtual Env

```sh
mkdir path/to/a/parent_folder/hosting/virtual/envs
cd path/to/a/parent_folder/hosting/virtual/envs
virtualenv name_of_env
#upon that you will see a new folder name_of_env here

cd name_of_env/bin/

# you can use this to step in
source activate

# in this bash, you can pip install anything
# or run python here

(or you can direclyt invoke the python from here to run)

path/to/a/parent_folder/hosting/virtual/envs/name_of_env/bin/python <your script>
```


## pdb

just do

```python
import pdb

#This will break where you want
# you get a prompt
# and study variables here
pdb.set_trace()
```

## numpy

```python
a_numpy_array = numpy.linspace(-np.pi, np.pi, 256, endpoint=True)
```

## plotting

Excellent introduction in https://www.labri.fr/perso/nrougier/teaching/matplotlib/
Another good introduction in https://realpython.com/blog/python/python-matplotlib-guide/

```python
import matplotlib.pyplot

matplotlib.pyplot.plot(x,y,'b-')
matplotlib.pyplot.show()

#or if you have dates
matplotlib.pyplot.plot_date(xdates,y,'b-')
matplotlib.pyplot.show()

matplotlib.pyplot.xlabel('what is x')
matplotlib.pyplot.ylabel('what is in y')
matplotlib.pyplot.title('title of this figure')

```

## Oauth

```
pip install cryptography
pip install oauth-lib
```

Read here: http://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html


## vlc media player

```
player = vlc.MediaPlayer(f)
r = player.play()

#get time in ms
player.get_time()
#get tot-time
player.get_length()
#toggle play/pause
player.pause()
player.audio_get_volume()
```

## Sched

General purpose event scheduler

```python
import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    print "Doing stuff..."
    # do your stuff
    s.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()
```

## ipaddress

```python
import ipaddress

# a single /32 address
address = ipaddress.IPv4Address('1.1.1.1')
# usually decays to str() on representation.
# you can explicitly cast as well
str(address)

# a address with its netmask
interface = ipaddress.IPv4Interface('1.1.1.1/24')
interface = ipaddress.IPv4Interface('1.1.1.1/255.255.255.0')
# get network - IPv4Network()
interface.network
# get netmask - IPv4Address()
interface.netmask
# get just ip - IPv4Address()
interface.ip


# purely a network
ntwk = ipaddress.IPv4Network('1.1.1.0/24')
# get just address part - IPv4Address()
ntwk.network_address
# get netmask - IPv4Address()
ntwk.netmask
# prefix
ntwk.prefixlen

```

## pyroute2

https://docs.pyroute2.org/iproute.html

```python
import pyroute2
ipr = pyroute2.IPRoute()

from pyroute2.netlink.rtnl import ndmsg
ndmsg.states    ## --> dict of ARP states.

try:
    any_ipr_command
except pyroute2.netlink.exceptions.NetlinkError as e:
    print ("got err:%s", e)

def get_if_index(ipr, ifc_name):
    ifc_index_list = ipr.link_lookup(ifname=ifc_name)
    if not ifc_index_list:
        return None
    if_index = ifc_index_list[0]
    return if_index

## ip link show equivalent
all_ifcs = ipr.get_links()
### get one atr, eg: mac address:
all_ifcs[0].get_attr('IFLA_ADDRESS')

## ip link del
ipr.link("del", index = idx)

## ip link set state up/down
ipr.link("set", index=if_index, state=state)

## ip addr show dev one_ifc
exist_ip_infos = ipr.get_addr(index=if_index, family=socket.AF_INET)
for i in exist_ip_infos:
    ip_addr = i.get_attr('IFA_ADDRESS')
    ip_pfx = i['prefixlen']
## ip addr del <addr/nm> dev ifc
ipr.addr('del', index=if_index,
        address=str(i.ip),
        prefixlen=i.network.prefixlen)

# ip route show table 256
routes = ipr.get_routes(family=socket.AF_INET,table=MAIN_TABLE_NUM)

# add arp entry (use 'del' for delete)
ipr.neigh('set',
        dst=peer_ip,
        lladdr=peer_mac,
        ifindex=if_index,
        state=ndmsg.states['permanent'])
# get arp entries
entries = ipr.get_neighbours(ifindex=if_index,
                match=lambda x:x['state']== ndmsg.states['permanent'])

# get vlans on a ip
vlans_list = ipr.get_vlans(index=ifidx)

```



## TunTap interfaces

* snippet is here: https://gist.github.com/abdelrahman-t/a23f57986a40f54108a71d4b91f145b2

## Grpc

### links

https://developers.google.com/protocol-buffers/docs/reference/python-generated?csw=1#fields

### Old style -- without async

* Server

* Client

https://stackoverflow.com/questions/55202617/how-to-make-async-grpc-calls-in-python
