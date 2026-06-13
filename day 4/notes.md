# Day 4 Notes

## What are Loops?

Loops are used to execute a block of code repeatedly.

Instead of writing:

```python
print("Hello")
print("Hello")
print("Hello")
```

We can use:

```python
for i in range(3):
    print("Hello")
```

---

## For Loop

Used when the number of iterations is known.

Syntax:

```python
for variable in range(start, stop):
    statements
```

Example:

```python
for i in range(1, 6):
    print(i)
```

Output:

1
2
3
4
5

---

## Range Function

```python
range(start, stop, step)
```

Examples:

```python
range(5)
range(1, 11)
range(1, 21, 2)
```

---

## While Loop

Used when the number of iterations is unknown.

Syntax:

```python
while condition:
    statements
```

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## Infinite Loop

Avoid:

```python
while True:
    print("Hello")
```

unless intentionally required.

---

## Applications of Loops

- Data Processing
- Automation Scripts
- Report Generation
- Dashboard Calculations
- Data Cleaning
- Repetitive Tasks