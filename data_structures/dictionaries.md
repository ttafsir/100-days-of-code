# Dictionaries

```python
>>> d = {[1,2,3]: "Hi"}
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    d = {[1,2,3]: "Hi"}
TypeError: unhashable type: 'list'
>>>
>>> # unshabble objects are mutable, and not suitable for hash functions
>>> l = [1,2,3]
>>> l[2] = 5
>>> l
[1, 2, 5]
>>>
>>> d = {(1,2,3): "Hi"}
>>> # tuples can be used as keys since they are hashable and immutable
>>>
>>> # iterating over dictionaries
>>> example = {'color': 'red', 'fruit': 'apple', 'species': 'dog'}
>>> example['color']
'red'
>>>
>>> # iterating over dictionaries with a for loop iterates over the keys only
>>> for item in example:
...     print(item)
...
...
color
fruit
species
>>> for key in example:
...     print(key, '->', example[key])
...
...
color -> red
fruit -> apple
species -> dog
>>>
>>> # what's in a dict?
>>> dir(example)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__'
, '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__',
 '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '
__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reve
rsed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook_
_', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setd
efault', 'update', 'values']
>>>
>>> example.values()
dict_values(['red', 'apple', 'dog'])
>>> # .values is a view object that changes as the values of the dict changes
>>> example.keys()
dict_keys(['color', 'fruit', 'species'])
>>> # .keys() is also a view object
>>>
>>> # looping through both
>>> example.items()
dict_items([('color', 'red'), ('fruit', 'apple'), ('species', 'dog')])
>>>
>>> for key, value in example.items():
...     print(key, '->', value)
...
...
color -> red
fruit -> apple
species -> dog
>>>
>>> # modifying values in a dict while iterating through them
>>> example2 = {'apple': .5, 'orange': .35, 'banana': .25}
>>> example2
{'apple': 0.5, 'orange': 0.35, 'banana': 0.25}
>>>
>>> # example 1
>>> for key in example2:
...     example2[key] = example2[key] + .1
...
...
>>> example2
{'apple': 0.6, 'orange': 0.44999999999999996, 'banana': 0.35}
>>>
>>> # example 2 (DOES NOT WORK)
>>> for key, value in example2.items():
...     value = value + .2
...
...
>>> example2
{'apple': 0.6, 'orange': 0.44999999999999996, 'banana': 0.35}
>>> # the change in example 2 doesnt work since you're really working with the v
iew object and not the original dictionary
>>>
>>> # you cannot delete keys while iterating
>>> for key in example2:
...     del example2['apple']
...
...
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    for key in example2:
RuntimeError: dictionary changed size during iteration
```



## Advanced Techniques with Dictionaries

```python
>>> # Advanced techniques with dictionary
>>> # dict comprehensions
>>> objects = ['blue', 'apple', 'dog']
>>> categories = ['color', 'fruit', 'pet']
>>> a_dict = {k: v for k,v in zip(objects, categories)}
>>> a_dict
{'blue': 'color', 'apple': 'fruit', 'dog': 'pet'}
>>>
>>> new_dict = {value: key for key, value in a_dict.items()}
>>> new_dict
{'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> num_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
>>> num_dict = {key: value for key, value in num_dict.items() if value > 2}
>>> num_dict
{'three': 3, 'four': 4}
>>>
```

```python
>>>
>>> incomes = {'jeff': 12000, 'annie': 23000, 'glen': 50000}
>>> # sorted by keys
>>> sorted_incomes = {k: incomes[k] for k,v in sorted(incomes.items())}
>>> sorted_incomes
{'annie': 23000, 'glen': 50000, 'jeff': 12000}
>>>
>>> # sorting by values
>>> def by_value(item):
...     return item[1]
...
>>> for k, v in sorted(incomes.items(), key=by_value):
...     print(k, v)
...
...
jeff 12000
annie 23000
glen 50000
>>> for k, v in sorted(incomes.items(), key=by_value, reverse=True):
...     print(k, v)
...
...
glen 50000
annie 23000
jeff 12000
>>>
>>> for k, v in sorted(incomes.items(), key=lambda x: x[1]):
...     print(k, v)
...
...
jeff 12000
annie 23000
glen 50000
```



### `.popitem()`

```python
>>> # How to use popitem
>>> a_dict = {'blue': 'color', 'apple': 'fruit', 'dog': 'pet'}
>>>
>>> a_dict.popitem()
('dog', 'pet')
>>>
>>> a_dict
{'blue': 'color', 'apple': 'fruit'}
>>> a_dict.popitem()
('apple', 'fruit')
>>> a_dict
{'blue': 'color'}
>>> # popitem returns and removes and item from the dict
>>>
>>> a_dict.pop()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    a_dict.pop()
TypeError: pop expected at least 1 argument, got 0
>>> a_dict.pop('blue')
'color'
>>> # pop returns a value and removes the item from the dict
```



### ChainMap

```python
>>> # Chainmap
>>> from collections import ChainMap
>>>
>>> # chain maps are dict like objects that allow you to work with multiple dict
s
>>> fruits = {'orange': 10, 'apple': 20}
>>> veggies = {'carrot': 5, 'potato': 45}
>>>
>>> chained_map = ChainMap(fruits, veggies)
>>> chained_map
ChainMap({'orange': 10, 'apple': 20}, {'carrot': 5, 'potato': 45})
>>>
>>> for key in chained_map:
...     print(key, '->', chained_map[key])
...
...
carrot -> 5
potato -> 45
orange -> 10
apple -> 20
>>>
>>>
>>> for key, value in chained_map.items():
...     print(key, '->', value)
...
...
carrot -> 5
potato -> 45
orange -> 10
apple -> 20
>>>
>>> # chain maps containing overlapping keys
>>> veggies = {'carrot': 5, 'potato': 45, 'orange': 11}
>>> chained_map = ChainMap(fruits, veggies)
>>> chained_map
ChainMap({'orange': 10, 'apple': 20}, {'carrot': 5, 'potato': 45, 'orange': 11})
>>> chained_map['orange']
10
>>> # returns the value for the first key
```



### `.fromkeys`

```python
>>> # create dictionary with all values at 0
>>> x = ('key1', 'key2', 'key3')
>>> y = 0
>>>
>>> thisdict = dict.fromkeys(x, y)
>>>
>>>
>>> print(thisdict)
{'key1': 0, 'key2': 0, 'key3': 0}
```



### Dictionary Unpacking

```python
>>> fruits = {'orange': 10, 'apple': 20}
>>> veggies = {'carrot': 5, 'potato': 45, 'orange': 11}
>>> {**fruits, **veggies}
{'orange': 11, 'apple': 20, 'carrot': 5, 'potato': 45}
>>>
>>> for k,v in {**fruits, **veggies}.items():
...     print(k, '->', v)
...
...
orange -> 11
apple -> 20
carrot -> 5
potato -> 45
```

The difference with unpacking and using `ChainMap` is that the unpacking will overwrite a key with the right most value. The `ChainMap` will store both but retrieve the left most value.

