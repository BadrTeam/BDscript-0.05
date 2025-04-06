# Programming Language Guide

## 1. Printing:
```crt
pr "Hello World"
pr x
```

## 2. Variables and Assignment:
```crt
x = 10
name = "John"
```

## 3. Input:
```crt
inp x
```

## 4. Arithmetic Operations:
```crt
x = 5 + 3
y = 10 - 2
z = 4 * 3
w = 15 / 3
p = 2 ^ 3
```

## 5. Arrays:
```crt
arr = array<>
arr = append<arr, 10>
element = get<arr, 0>
arr = set<arr, 0, 20>
len = length<arr>
```

## 6. Math Functions:
```crt
x = sqrt(16)
y = pow(2, 3)
z = sin(45)
w = cos(60)
p = abs(-5)
```

## 7. Conditions:
```crt
if x > 10 <
   pr "large"
>

if x > 10 <
   pr "large"
> elif x > 5 <
   pr "medium"
> else <
   pr "small"
>
```

## 8. Loops:
```crt
while x < 10 <
   pr x
   x = x + 1
>
```

## 9. Function Definition:
```crt
func add<x, y> {
   return x + y
}

result = add<5, 3>
```

## 10. Comments:
```crt
//
///
///
```
---

# Examples

### 1. Calculate Sum of Numbers from 1 to N:
```crt
n = 5
sum = 0
i = 1
while i <= n <
   sum = sum + i
   i = i + 1
>
pr sum
```

### 2. Array Usage Example:
```crt
arr = array<>
arr = append<arr, 10>
arr = append<arr, 20>
arr = append<arr, 30>
pr get<arr, 1>
arr = set<arr, 1, 25>
pr length<arr>
```

### 3. Factorial Function Example:
```crt
func factorial<n> {
   if n <= 1 <
      return 1
   >
   return n * factorial<n - 1>
}
```

### 4. Complete Program Example:
```crt
pr "Enter three numbers:"
inp x
inp y
inp z
avg = (x + y + z) / 3
pr "The average is:"
pr avg
```

---

## Important Notes:
- Each conditional statement and loop must end with `>`
- Built-in math functions like `sqrt`, `pow`, `sin`, `cos` are available
- Arrays are zero-indexed
- Conditions and loops can be nested

---

This guide provides a fundamental overview of the programming language syntax and features. Feel free to contribute or suggest improvements!

