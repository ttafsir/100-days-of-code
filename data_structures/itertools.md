# Itertools

### `cycle`

```python
>>> from itertools import cycle
>>> prices = {'apple': .25, 'orange': .50, 'kiwi': .75}
>>>
>>> # cycle allows you to iterate repeatedly
>>> num_items = 10
>>> for item in cycle(prices.items()):
...     if num_items == 0:
...         break
...     num_items -= 1
...     print(item)
...
...
('apple', 0.25)
('orange', 0.5)
('kiwi', 0.75)
('apple', 0.25)
('orange', 0.5)
('kiwi', 0.75)
('apple', 0.25)
('orange', 0.5)
('kiwi', 0.75)
('apple', 0.25)
```



## `chain`

```python
>>> from itertools import chain
>>> fruits = {'orange': 10, 'apple': 20}
>>> veggies = {'carrot': 5, 'potato': 45, 'orange': 11}
>>> for item in chain(fruits.items(), veggies.items()):
...     print(item)
...
...
('orange', 10)
('apple', 20)
('carrot', 5)
('potato', 45)
('orange', 11)
```

