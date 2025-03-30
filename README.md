Programming Language Guide

1. Printing:
   pr value  // to print a value
   Example: pr "Hello World"
   Example: pr x  // print variable value

2. Variables and Assignment:
   x = 10  // assign value to variable
   name = "John"  // assign text

3. Input:
   inp x  // read value from user and store in variable x

4. Arithmetic Operations:
   x = 5 + 3  // addition
   y = 10 - 2  // subtraction
   z = 4 * 3  // multiplication
   w = 15 / 3  // division
   p = 2 ^ 3  // power

5. Arrays:
   arr = array<>  // create empty array
   arr = append<arr, 10>  // add element
   element = get<arr, 0>  // get element
   arr = set<arr, 0, 20>  // modify element
   len = length<arr>  // get array length

6. Math Functions:
   x = sqrt<16>  // square root
   y = pow<2, 3>  // power
   z = sin<45>  // sine
   w = cos<60>  // cosine
   p = abs<-5>  // absolute value

7. Conditions:
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

8. Loops:
   while x < 10 <
      pr x
      x = x + 1
   >

9. Function Definition:
   func add<x, y> {
      return x + y
   }
   
   // function call
   result = add<5, 3>

10. Comments:
    // single line comment
    /// multi-line comment
    ///

11. File Import:
    import math  // to import math.bd

Examples:

1. Calculate sum of numbers from 1 to n:
   n = 5
   sum = 0
   i = 1
   while i <= n <
      sum = sum + i
      i = i + 1
   >
   pr sum

2. Array Usage Example:
   arr = array<>
   arr = append<arr, 10>
   arr = append<arr, 20>
   arr = append<arr, 30>
   pr get<arr, 1>  // will print 20
   arr = set<arr, 1, 25>  // change value
   pr length<arr>  // will print 3

3. Factorial Function Example:
   func factorial<n> {
      if n <= 1 <
         return 1
      >
      return n * factorial<n - 1>
   }

4. Complete Program Example:
   // program to calculate average of three numbers
   pr "Enter three numbers:"
   inp x
   inp y
   inp z
   avg = (x + y + z) / 3
   pr "The average is:"
   pr avg

Important Notes:
- Each conditional statement and loop must end with >
- Built-in math functions like sqrt, pow, sin, cos are available
- Arrays are zero-indexed
- Conditions and loops can be nested
