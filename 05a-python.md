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

>> REPLACE THIS TEXT WITH YOUR RESPONSE

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





