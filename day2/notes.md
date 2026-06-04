# Day 2 Notes

## What is a String?

A string is a sequence of characters enclosed in quotes.

Example:

```python
name = "Ashutosh"
```

---

## String Indexing

Each character has a position.

```python
name = "Python"

P = 0
y = 1
t = 2
h = 3
o = 4
n = 5
```

Negative Indexing:

```python
n = -1
o = -2
```

---

## String Slicing

```python
name[0:4]
```

Output:

```text
Pyth
```

---

## Common String Methods

### Upper

```python
text.upper()
```

### Lower

```python
text.lower()
```

### Title

```python
text.title()
```

### Replace

```python
text.replace()
```

### Length

```python
len(text)
```

---

## Type Casting

Convert one datatype into another.

```python
int()
float()
str()
bool()
```

---

## f-Strings

Modern way of formatting strings.

```python
print(f"My name is {name}")
```

Benefits:

- Cleaner code
- More readable
- Faster formatting