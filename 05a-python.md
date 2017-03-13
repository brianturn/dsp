# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are both sequences of elements that can be indexed. Lists are mutable (can be modified) and tuples are immutable. Tuples work as keys in dictionaries because they are immutable. 

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are both sequences of elements. Lists are mutable and indexed. Sets are unique elements only, unordered and immutable. 

```python
w = list('Moon')
print (w)
['M', 'o','o','n']
s = set('Moon')
print (s)
{'M', 'o', 'n'}
```

>> Lists are much less efficient at finding an element because at least half of the elements have to be checked. Sets are much quicker because the elements are unordered and are instead assigned to random buckets.


---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambdas are compact, anonymous functions that do not use def or return keywords. Lambdas follow the form: *lambda* [parameters(s)]: [expression]

>> Here is an example:

```python
#returns a function that squares the argument
a = lambda x: x**2
print (a(4))
16
```
>> Here is an example of using a lambda as a key to sort a tuple:

```python
t = [(300, 1, 'Adam'), (200, 0, 'Bob'), (100, 2, 'Cathy')]

print (sorted(t, key=lambda name: name[2]))

[(300, 1, 'Adam'), (200, 0, 'Bob'), (100, 2, 'Cathy')]
```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are succinct ways to traverse a list and return or modify values in the list.

```python
nums = [1, 2, 3, 4, 5]

new_list = [n*n for n in nums] # list comprehension

print (new_list)
# [1, 4, 9, 16, 25]
```

>> Map and filter functions have similar capabilities as list functions, however map/filter yield an iterable object:

```python
map_list = map(lambda n: n*n, nums)

print (list(map_list)) # iterable map_list object passed through list function
# [1, 4, 9, 16, 25]

another_list = [n for n in nums if n%2 == 0] # list comprehension, returns the number if even

print (another_list)
# [2, 4]
```
 
>> Here is the filter function compared to list comprehension:

```python
t = filter(lambda n: n%2 == 0, nums) # same thing with filter

print (list(t))
# [2, 4]

another_list = [n**2 for n in nums if n%2 == 0] # list comprehension, returns the square of each number if even

print (another_list)
# [4, 16]

# same thing but you have to wrap the filter function in a map function

filter_list = map(lambda n: n**2, filter(lambda n: n%2 == 0, nums))

print (list(filter_list))
# [4, 16]
```

>> Example of dictionary comprehension:

```python
names = ['Adam', 'Billy', 'Mary']
scores = [70, 80, 90]

my_dict = {name: score for name, score in zip(names, scores)}

print (my_dict)
# {'Adam': 70, 'Billy': 80, 'Mary': 90}
```

>> Example of set comprehension:

```python
numbers = [1, 3, 5, 6, 6, 7, 8, 8, 8, 9]

my_set = {n for n in numbers if n > 5}

print (sorted(my_set))
# [6, 7, 8, 9]
```

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





