# Custom Programming Language Course

Welcome to the course for your custom programming language! This guide will help you understand how to write, execute, and expand code using your language.

---


---

## 🛠️ **2. Running the Interpreter**
You can execute scripts written in your custom language by running the Python interpreter:

```bash
python main.py filename.bd
```

If no filename is provided, the interpreter will prompt you to enter the file name manually.

---

## ✍️ **3. Language Syntax and Examples**

### **A. Variables Declaration**
```plaintext
x = 5
y = 10
```

### **B. Printing Values**
```plaintext
pr x
pr y
```
_Output:_
```
5
10
```

### **C. Taking User Input**
```plaintext
inp name
pr name
```

### **D. Defining Functions**
```plaintext
func add<a, b> {
    return a + b
}
```

### **E. Calling Functions**
```plaintext
result = add<5, 10>
pr result
```
_Output:_
```
15
```

### **F. Conditional Statements**
```plaintext
if x > y <
    pr "x is greater"
>
elif x == y <
    pr "x is equal"
>
else <
    pr "y is greater"
>
```

### **G. While Loops**
```plaintext
counter = 0
while counter < 5 <
    pr counter
    counter = counter + 1
>
```
_Output:_
```
0
1
2
3
4
```

### **H. Return Values from Functions**
```plaintext
func square<n> {
    return n * n
}
result = square<4>
pr result
```
_Output:_
```
16
```

---

## ⚠️ **4. Common Errors and Troubleshooting**
- **SyntaxError:** Ensure all blocks (`if`, `else`, `while`, and functions) are properly closed with `>` or `}`.
- **Undefined Function:** Verify that the function is defined before being called.
- **Variable Not Defined:** Always declare variables before using them.

---

## 🧩 **5. Advanced Tips**
- Optimize your functions for faster performance.
- Use `numba` for computational-heavy tasks.
- Structure your code into separate `.bd` files for better organization.

---

## ✅ **6. Best Practices**
- Keep your functions small and focused.
- Use clear and descriptive variable names.
- Always handle edge cases and invalid inputs.

---

That's it! You now have a solid understanding of how to write and execute code using your custom language. Happy coding! 🚀

