# 100 Days of Python Challenge

Repo to track my progress over the next 100 days of Python challenges. This challenge is based on the [#100DaysOfCode in Python](https://training.talkpython.fm/courses/details/100-days-of-code-in-python) course and challenge from [talkpython.fm](talkpython.fm)

:rocket: [Initial Repository](../../tree/737dea6bcb47f57880959065882255be102d09ea/) - Click here for the initial version of this repository.

### The plan

<details><summary>Days 1-3: Playing with Datetimes</summary>

#### Day 1

* Lecture: learning datetime and date (TalkPython)
* Reading: [Using Python datetime to Work With Dates and Times](https://realpython.com/python-datetime/)
* Code:
  * [datetime shell exercises](./code/day1/day1_datetime.py)
  * [fun exercise](./code/day1/pyramid.py)

#### Day 2

* Lecture: Datetime `timedelta` usage (TalkPython)
* Code:
  * [datetime shell exercises](./code/day2/day2_datetime.py)

#### Day 3

* Code:
  * [pomodoro timer](./code/pomodoro.py)
  * [logtime parser](./code/logtimes.py)

</details>

<details><summary>Days 4-6: Collections Module</summary>

#### Day 4

* Lecture: Collections module (TalkPython)
  *  Namedtuples
  *  Defaultdicts
  *  Counter
  *  Deque

The `collections` module implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers, [`dict`](https://docs.python.org/3/library/stdtypes.html#dict), [`list`](https://docs.python.org/3/library/stdtypes.html#list), [`set`](https://docs.python.org/3/library/stdtypes.html#set), and [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple).

| [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple) | factory function for creating tuple subclasses with named fields |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`deque`](https://docs.python.org/3/library/collections.html#collections.deque) | list-like container with fast appends and pops on either end |
| [`ChainMap`](https://docs.python.org/3/library/collections.html#collections.ChainMap) | dict-like class for creating a single view of multiple mappings |
| [`Counter`](https://docs.python.org/3/library/collections.html#collections.Counter) | dict subclass for counting hashable objects                  |
| [`OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict) | dict subclass that remembers the order entries were added    |
| [`defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict) | dict subclass that calls a factory function to supply missing values |
| [`UserDict`](https://docs.python.org/3/library/collections.html#collections.UserDict) | wrapper around dictionary objects for easier dict subclassing |
| [`UserList`](https://docs.python.org/3/library/collections.html#collections.UserList) | wrapper around list objects for easier list subclassing      |
| [`UserString`](https://docs.python.org/3/library/collections.html#collections.UserString) | wrapper around string objects for easier string subclassing  |

**`namedtuple`**

```python
>>> from collections import namedtuple
>>> User = namedtuple('User', 'name role')
>>> user = User(name="Tafsir", role="Architect")
>>> user.name
'Tafsir'
>>> user.role
'Architect'
>>>
```

**`defaultdict`**

```python
>>> scores = {"player1": 100, "player2": 75}
>>> scores["player3"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'player3'
>>>
>>> # using get to avoid KeyError
>>> scores.get("player3")
>>>
>>> # assigning a value to non-existent key
>>> scores["player3"] = 99
>>> scores["player4"] = 99
>>>
>>> # assigning values while building a collection
>>> results = {}
>>> for player, scores in scores.items():
...   results[player].append(scores)
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyError: 'player1'
>>>
>>>
>>> from collections import defaultdict
>>> results = defaultdict(list)
>>> for player, score in scores.items():
...   results[player].append(score)
...
>>> results
defaultdict(<class 'list'>, {'player1': [100], 'player2': [75], 'player3': [99], 'player4': [99]})
```

**`counter`**

```python
# most_common.py
# find and printing the most common IPs
from pathlib import Path

ip_list = Path("ip_addresses.txt").read_text().split()

most_common = {}
for ip, port in (string.split(":") for string in ip_list):
    if ip not in most_common:
        most_common[ip] = 0
    most_common[ip] += 1

for k,v in sorted(most_common.items(),
                  key=lambda x: x[1],
                  reverse=True)[:5]:
    print(k, v)
```

```sh
➜ python most_common.py
192.168.10.103 16
192.168.100.1 13
192.168.10.113 3
192.168.100.11 2
192.168.100.13 2
```


```python
# using the most_common method from Counter
from pathlib import Path

ip_list = Path("ip_addresses.txt").read_text().split()
addresses = [text.split(":")[0] for text in ip_list]
for ip, count in (Counter(addresses).most_common(5)):
  print(ip, count)
```



**`dueque`**

Stacks and Queues that are useful for insert and delete from a sequence.

```python
import random
from collections import deque

lst = list(range(100000))
deq = deque(range(100000))

def insert_and_delete(ds):
  for _ in range(10):
    index = random.choice(range(100))
    ds.remove(index)
    ds.insert(index, index)

# in ipython
#   ...:    ...: %timeit insert_and_delete(lst)
#   ...:    ...: %timeit insert_and_delete(deq)
#   ...: 701 µs ± 4.49 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
#   ...: 17.3 µs ± 208 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```


#### Day 5

* Lecture: `collections` challenge

* Reading: https://docs.python.org/3/library/collections.html#collections

* Code: https://github.com/pybites/challenges/pull/797/files


#### Day 6

* Lecture: Datetime `timedelta` usage (TalkPython)

* reading: https://docs.python.org/3/library/collections.html#collections

</details>



<details><summary>Days 7-9: Python Data Structures</summary>

#### Day 7

* :video_camera: **Lecture**: List, Tuple and Dictionary videos (TalkPython)
* :books: **Reading**: https://realpython.com/iterate-through-dictionary-python/
* :notebook: **Notes**: [data structures](./datastructures)

#### Day 8

* :page_with_curl: **Code:**  [Bite 21 from codechalleng.es](https://codechalleng.es/bites/21/) - [My Solution](./code/day8/bite21.py)

#### Day 9

* :page_with_curl: **Code:**  [Bite 89 from codechalleng.es](https://codechalleng.es/bites/89/) - [My Solution](./code/day9/states.py)

</details>

<details><summary>Days 10-12: Testing with `pytest`</summary>

#### Day 10

* :video_camera: **Lecture**: Testing your code with pytest (TalkPython)

#### Day 11

* :page_with_curl: **Code:** [Tests for htping](https://github.com/ttafsir/htping/tree/main/tests)
</details>

<details><summary>Days 13-15: Test-based games (classes)</summary></details>

<details><summary>Days 16-18: List comprehensions and generators</summary></details>

<details><summary>Days 19-21: Iteration with itertools</summary></details>

<details><summary>Days 22-24: Decorators</summary></details>

<details><summary>Days 25-27: Error handling</summary></details>

<details><summary>28-30: Regular Expressions</summary></details>

<details><summary>Days 31-33: Logging</summary></details>

<details><summary>Days 34-36: Refactoring / Pythonic code</summary></details>

<details><summary>Days 37-39: Using CSV data</summary></details>

<details><summary>Days 40-42: JSON in Python</summary></details>

<details><summary>Days 43-45: Consuming HTTP services</summary></details>

<details><summary>Days 46-48: Web Scraping with BeautifulSoup4</summary></details>

<details><summary>Days 49-51: Measuring performance</summary></details>

<details><summary>Days 52-54: Parsing RSS feeds with Feedparser</summary></details>

<details><summary>Days 55-57: Structured API clients with uplink</summary></details>

<details><summary>Days 58-60: Twitter data analysis with Python</summary></details>

<details><summary>Days 61-63: Using the Github API with Python</summary></details>

<details><summary>Days 64-66: Sending emails with smtplib</summary></details>

<details><summary>Days 67-69: Copy and Paste with Pyperclip</summary></details>

<details><summary>Days 70-72: Excel automation with openpyxl</summary></details>

<details><summary>Days 73-75: Automate tasks with Selenium</summary></details>

<details><summary>Days 76-78: Getting Started with Python Flask</summary></details>

<details><summary>Days 79-81: Basic Database Access with SQLite3</summary></details>

<details><summary>Days 82-84: Data visualization with Plotly</summary></details>

<details><summary>Days 85-87: Fullstack web apps made easy</summary></details>

<details><summary>Days 88-90: Home Inventory App</summary></details>

<details><summary>Days 91-93: Database access with SQLAlchemy</summary></details>

<details><summary>Days 94-96: Rich GUI apps in Python</summary></details>

<details><summary>Days 97-99: Building JSON APIs</summary></details>



## The progress

| Day    | Status | Content |
| ------ | ------ | ------- |
| Day 1  |        |         |
| Day 2  |        |         |
| Day 3  |        |         |
| Day 4  |        |         |
| Day 5  |        |         |
| Day 6  |        |         |
| Day 7  |        |         |
| Day 8  |        |         |
| Day 9  |        |         |
| Day 10 |        |         |
| Day 11 |        |         |
| Day 12 |        |         |
| Day 13 |        |         |
| Day 14 |        |         |
| Day 15 |        |         |
| Day 16 |        |         |
| Day 17 |        |         |
| Day 18 |        |         |
| Day 19 |        |         |
| Day 20 |        |         |
| Day 21 |        |         |
| Day 22 |        |         |
| Day 23 |        |         |
| Day 24 |        |         |
| Day 25 |        |         |
| Day 26 |        |         |
| Day 27 |        |         |
| Day 28 |        |         |
| Day 29 |        |         |
| Day 30 |        |         |
| Day 31 |        |         |
| Day 32 |        |         |
| Day 33 |        |         |
| Day 34 |        |         |
| Day 35 |        |         |
| Day 36 |        |         |
| Day 37 |        |         |
| Day 38 |        |         |
| Day 39 |        |         |
| Day 40 |        |         |
| Day 41 |        |         |
| Day 42 |        |         |
| Day 43 |        |         |
| Day 44 |        |         |
| Day 45 |        |         |
| Day 46 |        |         |
| Day 47 |        |         |
| Day 48 |        |         |
| Day 49 |        |         |
| Day 50 |        |         |
| Day 51 |        |         |
| Day 52 |        |         |
| Day 53 |        |         |
| Day 54 |        |         |
| Day 55 |        |         |
| Day 56 |        |         |
| Day 57 |        |         |
| Day 58 |        |         |
| Day 59 |        |         |
| Day 60 |        |         |
| Day 61 |        |         |
| Day 62 |        |         |
| Day 63 |        |         |
| Day 64 |        |         |
| Day 65 |        |         |
| Day 66 |        |         |
| Day 67 |        |         |
| Day 68 |        |         |
| Day 69 |        |         |
| Day 70 |        |         |
| Day 71 |        |         |
| Day 72 |        |         |
| Day 73 |        |         |
| Day 74 |        |         |
| Day 75 |        |         |
| Day 76 |        |         |
| Day 77 |        |         |
| Day 78 |        |         |
| Day 79 |        |         |
| Day 80 |        |         |
| Day 81 |        |         |
| Day 82 |        |         |
| Day 83 |        |         |
| Day 84 |        |         |
| Day 85 |        |         |
| Day 86 |        |         |
| Day 87 |        |         |
| Day 88 |        |         |
| Day 89 |        |         |
| Day 90 |        |         |
| Day 91 |        |         |
| Day 92 |        |         |
| Day 93 |        |         |
| Day 94 |        |         |
| Day 95 |        |         |
| Day 96 |        |         |
| Day 97 |        |         |
| Day 98 |        |         |
| Day 99 |        |         |



