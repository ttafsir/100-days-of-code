# Tuples

Tuples are sequences that are **immutable**, unlike `list` objects.

```python
>>> tup = tuple(myname)
>>> lst = list(myname)
>>>
>>> tup
('T', 'a', 'f', 's', 'i', 'r')
>>> lst
['T', 'a', 'f', 's', 'i', 'r']
>>>
>>> tup[0]
'T'
>>> lst[0]
'T'
>>> lst[0] = "t"
>>> tup[0] = "t"
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    tup[0] = "t"
TypeError: 'tuple' object does not support item assignment
```



### Methods and Attributes

```python
>>> dir(tup)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '_
_eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs
__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__'
, '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_e
x__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclas
shook__', 'count', 'index']
```

