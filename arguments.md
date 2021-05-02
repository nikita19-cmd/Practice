# Python Function Arguments

## Positional Arguments
Positional arguments are the arguments that need to be passed to the function call in a proper order.

For example,

```python
def add_numbers(n1, n2):
    result = n1 + n2
    return result

result = add_numbers(5, 6.7)
print(result)
```
**Output**

```
11.7
```

## Default Arguments

Function arguments can have default values in Python.

We can provide a default value to an argument by using the assignment operator `=`. 

For example,

```python
def add_numbers(n1 = 100, n2 = 1000):
    result = n1 + n2
    return result

result = add_numbers(5.4)
print(result)
```
**Output**

```
1005.4
```


def add_numbers(n1 = 100, n2 = 1000):
    result = n1 + n2
    return result


## Keyword Arguments

In Python, we can not only pass arguments to a function based on position, but also using their parameter name.
result = add_numbers(n2=5)
print(result)
