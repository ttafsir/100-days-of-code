# Lists

```python
>>> myname = "Tafsir"
>>> # you can create a list from a string, which is just a sequence of chars
>>> list(myname)
['T', 'a', 'f', 's', 'i', 'r']
>>> lst = list(myname)
>>> # you can access items in the list through indexing, starting from 0
>>> lst[0]
'T'
>>> lst[5]
'r'
>>> # access items from the right. -1 is the right most element
>>> lst[-1]
'r'
>>> # return a value at index and remove the value from the list. last index is default.
>>> lst.pop()
'r'
>>> lst
['T', 'a', 'f', 's', 'i']
>>> # inserting a value at an index
>>> lst.insert(5, 'r')
>>> lst
['T', 'a', 'f', 's', 'i', 'r']
>>> lst[0] = "t"
>>> lst
['t', 'a', 'f', 's', 'i', 'r']
>>> del lst[0]
>>> lst
['a', 'f', 's', 'i', 'r']
>>> lst.insert(0, 't')
>>> lst
['t', 'a', 'f', 's', 'i', 'r']
>>>
>>> lst.pop(3)
's'
>>> lst
['t', 'a', 'f', 'i', 'r']
>>> lst.insert(3, 'f')
>>>
>>> lst
['t', 'a', 'f', 'f', 'i', 'r']
>>> # lists are mutable, meaning that you can replace/assign a value in the list.
>>> lst[3] = 's'
>>> lst
['t', 'a', 'f', 's', 'i', 'r']
>>> lst.append('s')
>>> lst
['t', 'a', 'f', 's', 'i', 'r', 's']
>>>
```



### Methods and Attributes

```python
>>> dir(lst)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__'
, '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__'
, '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__',
 '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__r
educe__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__'
, '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear',
 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort
']
```

