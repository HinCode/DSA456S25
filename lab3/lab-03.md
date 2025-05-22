# Lab 3

This assessment contains materials that may be subject to copyright and other intellectual property rights. 

Modification, distribution or reposting of this document is strictly prohibited. Learners found reposting this document or its solution anywhere will be subject to the college’s Academic Integrity policy.

## Due: June 8

## Objectives:


- practice analysis of recursive functions
- practice programming linked lists


## Setup


All files needed for this lab were created by doing the first task in [lab 0](lab-00.md).  If you didn't do lab 0, do the first task to create your lab repository.


- All code is to be written in lab3.py
- All answers to non-coding questions and analysis is to be written in lab3.md

## Resources

You may find the following parts of the notes useful:
* [how to do an analysis in 5 steps](https://seneca-ictoer.github.io/data-structures-and-algorithms/B-Algorithms-Analysis/how-to-do-an-analysis)
* [how to do a recursive analysis](https://seneca-ictoer.github.io/data-structures-and-algorithms/C-Recursion/analysis-of-recursive-functions)


## Part A Analysis

Perform an analysis of the following recursive functions.

### function 1:

Analyze the following function with respect to number

```python
def function1(value, number):
	if (number == 0):
		return 1
	elif (number == 1):
		return value
	else:
		return value * function1(value, number-1)
```

### function 2:

Analyze function2 with respect to the length of the mystring.  Hint, you will need to set up two mathematical functions for operator counting.  one for function2 and the other for recursive_function2

```python

def recursive_function2(mystring,a, b):
	if(a >= b ):
		return True
	else:
		if(mystring[a] != mystring[b]):
			return False
		else:
			return recursive_function2(mystring,a+1,b-1)

def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1)

```

### function 3 (optional challenge):

Analyze the following function with respect to number

```python
def function3(value, number):
	if (number == 0):
		return 1
	elif (number == 1):
		return value
	else:
		half = number // 2
		result = function3(value, half)
		if (number % 2 == 0):
			return result * result
		else:
			return value * result * result

```

## Part B Programming

In this section of the lab, you will implement some functions for a doubly linked list, for both the sentinel and non-sentinel version of the list.  In your lab template you will find some drawing templates.  Use these to help you with your programming of these lists.


### Node class

The Node class is declared within both the DoublyLinked and Sentinel class.  It stores:
* a piece of data
* a reference to the next Node in the list
* a reference to the previous Node in the list
    
When a Node is initialized, it is passed a data value.  Optionally it is also passed a reference to the next node and a reference to the previous node (in that order).  If the data values are not passed in, they are defaulted to None.

The Node function has the following member functions:

---

```python
def get_data(self)
```
function returns data stored in node

---

```python
def get_next(self)
```
function returns reference to next node in the list

---

```python
def get_previous(self)
```
function returns reference to previous node in the list

---

### DoublyLinked and Sentinel List

---
```python
def get_front(self)
```
This function returns a reference to the first data node in the list.  If list is empty, function returns None

---

```python
def get_back(self)
```
This function returns a reference to the last data node in the list.  If list is empty, function returns None

---

```python  
def push_front(self, data)
```
This function adds data to the front of the list (before the first data node).  This function returns nothing

---

```python  
def push_back(self,data)
```
This function adds data to the back of the list (after the last data node).  This function returns nothing

---

```python  
def pop_front(self)
```
This function removes the first data node from the list.  Function returns value stored in that node

If the function is called on an empty DList, raise the IndexError with this statement

```python
  raise IndexError('pop_front() used on empty list')
```

---

```python  

def pop_back(self)
```
This function removes the last data node from the list.  Function returns value stored in that node

If the function is called on an empty DList, raise the IndexError with this statement

```python
raise IndexError('pop_back() used on empty list')
```

---



## Part C Reflection

1. Describe how to a approach writing recursive functions, what steps do you take?

2. Describe the process of analyzing recursive functions.  How does it differ from from analyzing non-recursive functions?  How is it the same? 


## Submitting your lab

Push your files into your github repo.  Part B is complete if it passes testing (green check mark for part B in actions tab)

When you are happy with the state of your files, submit a link to your repo's lab3 folder into blackboard. NOTE: a link submitted to BB is required for submission.

Note: Submission of a link to Blackboard is an indication that your lab is ready for grading in the current state.  Do not submit a link until you are ready to be graded.



## Lab Rubric:

| Criteria       | Poor - 0 mark     | Fair - 1 marks                                                                                                                     | Good - 2 marks                                                              |
| -------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| Lab Completion | Part A not completed | Coding Completed, analysis/reflection is missing or poorly done | Successfully complete coding, analysis and reflection portions |
