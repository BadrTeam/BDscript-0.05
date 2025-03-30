# Programming Language Guide

## 1. Printing:
```crt
pr "Hello World"  // Print a string
pr x  // Print variable value
```

## 2. Variables and Assignment:
```crt
x = 10  // Assign a number to variable
name = "John"  // Assign a string
```

## 3. Input:
```crt
inp x  // Read input from user and store in variable x
```

## 4. Arithmetic Operations:
```crt
x = 5 + 3  // Addition
y = 10 - 2  // Subtraction
z = 4 * 3  // Multiplication
w = 15 / 3  // Division
p = 2 ^ 3  // Exponentiation
```

## 5. Arrays:
```crt
arr = array<>  // Create an empty array
arr = append<arr, 10>  // Add an element to the array
element = get<arr, 0>  // Get element at index 0
arr = set<arr, 0, 20>  // Modify element at index 0
len = length<arr>  // Get array length
```

## 6. Math Functions:
```crt
x = sqrt<16>  // Square root
y = pow<2, 3>  // Power
z = sin<45>  // Sine function
w = cos<60>  // Cosine function
p = abs<-5>  // Absolute value
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

// Function call
result = add<5, 3>
```

## 10. Comments:
```crt
// Single-line comment
/// Multi-line comment
///
```

## 11. File Import:
```crt
import math  // Import math library
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
pr sum  // Output the sum
```

### 2. Array Usage Example:
```crt
arr = array<>
arr = append<arr, 10>
arr = append<arr, 20>
arr = append<arr, 30>
pr get<arr, 1>  // Output: 20
arr = set<arr, 1, 25>  // Modify element at index 1
pr length<arr>  // Output: 3
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
// Program to calculate the average of three numbers
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

