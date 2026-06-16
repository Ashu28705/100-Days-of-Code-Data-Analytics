# Day 6 Notes

## What is a Function?

A function is a reusable block of code designed to perform a specific task.

Instead of writing the same code repeatedly, we can place it inside a function and call it whenever needed.

---

## Syntax

```python
def function_name():
    statements
```

Example:

```python
def greet():
    print("Hello")
```

Calling:

```python
greet()
```

---

## Parameters

Parameters allow functions to accept input.

```python
def greet(name):
    print(name)
```

Example:

```python
greet("Ashutosh")
```

---

## Return Statement

The return statement sends a value back.

```python
def add(a, b):
    return a + b
```

---

## Variable Scope

### Local Variable

```python
def demo():
    x = 10
```

Only accessible inside the function.

---

### Global Variable

```python
x = 10
```

Accessible throughout the program.

---

## Benefits of Functions

- Reusable code
- Easier maintenance
- Better organization
- Reduced duplication
- Professional coding practices