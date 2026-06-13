# Day 5 Notes

## What are Collections?

Collections are data structures used to store multiple values in a single variable.

Python provides:

1. List
2. Tuple
3. Set
4. Dictionary

---

## Lists

Lists are ordered and mutable.

Example:

```python
fruits = ["Apple", "Banana", "Mango"]
```

Access:

```python
print(fruits[0])
```

Methods:

```python
append()
remove()
insert()
sort()
pop()
```

---

## Tuples

Tuples are ordered and immutable.

```python
student = ("Ashutosh", 21, "Ahmedabad")
```

Cannot be modified after creation.

Useful for storing fixed data.

---

## Sets

Sets are unordered collections.

```python
numbers = {1,2,3}
```

Features:

- No duplicates
- Fast lookup

Example:

```python
{10,20,30,10}
```

Output:

```python
{10,20,30}
```

---

## Dictionaries

Store data as key-value pairs.

```python
student = {
    "name": "Ashutosh",
    "age": 21
}
```

Access:

```python
student["name"]
```

Output:

```python
Ashutosh
```

---

## Why Dictionaries Matter

Most datasets and APIs return data in dictionary format.

Example:

```python
{
    "employee": "John",
    "salary": 50000
}
```