import re
import sys
import math

                                                # تعريف الدوال الأساسية
def pr(value):
                                                    print(value)

                                                # تعريف الدوال الرياضية المدمجة
def create_array():
    return []

def get_array_element(arr, index):
    if not isinstance(arr, list):
        raise ValueError("Not an array")
    if index >= len(arr):
        raise ValueError("Index out of bounds")
    return arr[index]

def set_array_element(arr, index, value):
    if not isinstance(arr, list):
        raise ValueError("Not an array")
    if index >= len(arr):
        # Extend array if needed
        arr.extend([0] * (index - len(arr) + 1))
    arr[index] = value
    return arr

def array_length(arr):
    if not isinstance(arr, list):
        raise ValueError("Not an array")
    return len(arr)

def array_append(arr, value):
    if not isinstance(arr, list):
        raise ValueError("Not an array")
    arr.append(value)
    return arr

def get_builtin_math_functions():
                                                    def safe_sqrt(x):
                                                        if x < 0:
                                                            raise ValueError("Cannot calculate square root of negative number")
                                                        return math.sqrt(x)

                                                    def safe_log(x):
                                                        if x <= 0:
                                                            raise ValueError("Cannot calculate logarithm of non-positive number")
                                                        return math.log(x)

                                                    builtin_funcs = {
                                                        # دوال المصفوفات
                                                        "array": create_array,
                                                        "get": get_array_element,
                                                        "set": set_array_element,
                                                        "length": array_length,
                                                        "append": array_append,
                                                        # الدوال الرياضية الأساسية - Mathematical Functions
                                                        "sin": math.sin,
                                                        "cos": math.cos,
                                                        "tan": math.tan,
                                                        "sqrt": safe_sqrt,
                                                        "pow": math.pow,
                                                        "abs": abs,
                                                        "floor": math.floor,
                                                        "ceil": math.ceil,
                                                        "round": round,
                                                        "log": safe_log,
                                                        "log10": math.log10,
                                                        "exp": math.exp,

                                                        # الدوال الإضافية
                                                        "min": min,
                                                        "max": max,
                                                        "sum": sum,
                                                        "asin": math.asin,
                                                        "acos": math.acos,
                                                        "atan": math.atan,
                                                        "sinh": math.sinh,
                                                        "cosh": math.cosh,
                                                        "tanh": math.tanh,
                                                        "degrees": math.degrees,
                                                        "radians": math.radians,
                                                    }
                                                    return builtin_funcs

def evaluate_expression(expr, variables, functions=None):
                                                    # معالجة خاصة لدوال المصفوفات
                                                    if expr.strip() == "array<>":
                                                        return []
                                                    elif "append<" in expr:
                                                        # تحليل استدعاء append
                                                        match = re.match(r'append<(.*?),\s*(.*?)>', expr)
                                                        if match:
                                                            arr_expr = match.group(1).strip()
                                                            val_expr = match.group(2).strip()
                                                            # تقييم المصفوفة والقيمة
                                                            arr = evaluate_expression(arr_expr, variables, functions)
                                                            val = evaluate_expression(val_expr, variables, functions)
                                                            return array_append(arr, val)
                                                        else:
                                                            raise ValueError(f"Invalid append expression: {expr}")
                                                    elif "get<" in expr:
                                                        # تحليل استدعاء get
                                                        match = re.match(r'get<(.*?),\s*(.*?)>', expr)
                                                        if match:
                                                            arr_expr = match.group(1).strip()
                                                            idx_expr = match.group(2).strip()
                                                            # تقييم المصفوفة والمؤشر
                                                            arr = evaluate_expression(arr_expr, variables, functions)
                                                            idx = evaluate_expression(idx_expr, variables, functions)
                                                            return get_array_element(arr, idx)
                                                        else:
                                                            raise ValueError(f"Invalid get expression: {expr}")
                                                    elif "set<" in expr:
                                                        # تحليل استدعاء set
                                                        match = re.match(r'set<(.*?),\s*(.*?),\s*(.*?)>', expr)
                                                        if match:
                                                            arr_expr = match.group(1).strip()
                                                            idx_expr = match.group(2).strip()
                                                            val_expr = match.group(3).strip()
                                                            # تقييم المصفوفة والمؤشر والقيمة
                                                            arr = evaluate_expression(arr_expr, variables, functions)
                                                            idx = evaluate_expression(idx_expr, variables, functions)
                                                            val = evaluate_expression(val_expr, variables, functions)
                                                            return set_array_element(arr, idx, val)
                                                        else:
                                                            raise ValueError(f"Invalid set expression: {expr}")
                                                    elif "length<" in expr:
                                                        # تحليل استدعاء length
                                                        match = re.match(r'length<(.+?)>', expr)
                                                        if match:
                                                            arr_expr = match.group(1).strip()
                                                            # تقييم المصفوفة
                                                            arr = evaluate_expression(arr_expr, variables, functions)
                                                            return array_length(arr)
                                                        else:
                                                            raise ValueError(f"Invalid length expression: {expr}")
                                                    try:
                                                        # إضافة الثوابت الرياضية
                                                        math_constants = {
                                                            "PI": math.pi,
                                                            "E": math.e,
                                                            "TAU": math.tau
                                                        }

                                                        # التحقق من وجود استيراد ملف
                                                        if isinstance(expr, str) and expr.startswith("import"):
                                                            module_name = line.split()[1].strip()
                                                            try:
                                                                with open(f"{module_name}.bd", 'r') as file:
                                                                    imported_code = file.read()
                                                                    # تنفيذ الكود المستورد في نطاق متغيرات جديد
                                                                    module_vars = {}
                                                                    module_funcs = {}
                                                                    interpret(imported_code, module_vars, module_funcs)
                                                                    # إضافة المتغيرات والدوال إلى النطاق الحالي
                                                                    for name, value in module_vars.items():
                                                                        variables[f"{module_name}.{name}"] = value
                                                                    for name, func in module_funcs.items():
                                                                        functions[f"{module_name}.{name}"] = func
                                                            except FileNotFoundError:
                                                                raise ValueError(f"Module not found: {module_name}")
                                                            next(lines, None)  # Skip to next line

                                                        # دمج الثوابت مع المتغيرات
                                                        for const, value in math_constants.items():
                                                            if const not in variables:  # لا تستبدل المتغيرات المعرفة بنفس الاسم
                                                                variables[const] = value

                                                        # استبدال المتغيرات بقيمها في التعبير
                                                        for var_name, var_value in sorted(variables.items(), key=lambda x: len(x[0]), reverse=True):
                                                            # تأكد من أن المتغير ليس داخل اسم آخر
                                                            pattern = r'\b' + re.escape(var_name) + r'\b'
                                                            expr = re.sub(pattern, str(var_value), expr)

                                                        # تنفيذ استدعاءات الدوال قبل التقييم النهائي
                                                        if functions:
                                                            # معالجة استدعاءات الدوال المتداخلة
                                                            while True:
                                                                # البحث عن أعمق استدعاء للدالة (الذي لا يحتوي على '<' داخل وسائطه)
                                                                func_match = re.search(r'(\w+)<([^<>]*)>', expr)
                                                                if not func_match:
                                                                    break

                                                                func_name = func_match.group(1)
                                                                args_str = func_match.group(2).strip()
                                                                full_match = func_match.group(0)  # الاستدعاء الكامل للدالة

                                                                # تقسيم الوسائط
                                                                args = []
                                                                if args_str:
                                                                    # معالجة أكثر دقة للفواصل - تجاهل الفواصل داخل التعابير الرياضية
                                                                    current_arg = ""
                                                                    parenthesis_count = 0

                                                                    for char in args_str:
                                                                        if char == '(' or char == '[' or char == '{':
                                                                            parenthesis_count += 1
                                                                            current_arg += char
                                                                        elif char == ')' or char == ']' or char == '}':
                                                                            parenthesis_count -= 1
                                                                            current_arg += char
                                                                        elif char == ',' and parenthesis_count == 0:
                                                                            args.append(current_arg.strip())
                                                                            current_arg = ""
                                                                        else:
                                                                            current_arg += char

                                                                    if current_arg:
                                                                        args.append(current_arg.strip())

                                                                # تقييم قيم الوسائط
                                                                evaluated_args = []
                                                                for arg in args:
                                                                    # تحقق أولا إذا كان هناك استدعاء دالة في الوسيط
                                                                    if re.search(r'(\w+)<([^<>]*)>', arg):
                                                                        # تقييم الدالة المتداخلة
                                                                        arg_value = evaluate_expression(arg, variables, functions)
                                                                        evaluated_args.append(arg_value)
                                                                    elif arg in variables:
                                                                        evaluated_args.append(variables[arg])
                                                                    else:
                                                                        try:
                                                                            # محاولة تقييم التعبير كتعبير رياضي
                                                                            arg_value = eval(arg, {"__builtins__": {}}, {**variables, **math_constants})
                                                                            evaluated_args.append(arg_value)
                                                                        except:
                                                                            evaluated_args.append(arg)

                                                                # استدعاء الدالة
                                                                builtin_math = get_builtin_math_functions()
                                                                if func_name in functions or func_name in builtin_math:
                                                                    result = call_function(func_name, evaluated_args, functions, variables)
                                                                    # استبدال استدعاء الدالة بالنتيجة
                                                                    expr = expr.replace(full_match, str(result))
                                                                else:
                                                                    raise ValueError(f"Function '{func_name}' is not defined")

                                                        # تقييم التعبير النهائي
                                                        # استخدم فقط المتغيرات والثوابت المُعرفة لتجنب المخاطر الأمنية
                                                        safe_globals = {"__builtins__": {}}
                                                        safe_locals = {
                                                            **variables,
                                                            **math_constants,
                                                            "INF": float('inf'),
                                                            "NAN": float('nan')
                                                        }

                                                        # إضافة دوال رياضية محددة للتقييم الآمن
                                                        safe_math_funcs = {
                                                            "sin": math.sin,
                                                            "cos": math.cos,
                                                            "tan": math.tan,
                                                            "sqrt": math.sqrt,
                                                            "pow": math.pow,
                                                            "abs": abs,
                                                            "log": math.log,
                                                            "exp": math.exp,
                                                            "min": min,
                                                            "max": max,
                                                            "round": round,
                                                            "radians": math.radians,
                                                            "degrees": math.degrees,
                                                            "asin": math.asin,
                                                            "acos": math.acos,
                                                            "atan": math.atan,
                                                            "INF": float('inf'),
                                                            "NAN": float('nan')
                                                        }
                                                        safe_locals.update(safe_math_funcs)

                                                        return eval(expr, safe_globals, safe_locals)
                                                    except Exception as e:
                                                        raise ValueError(f"Error evaluating expression: {expr} - {e}")

def call_function(func_name, args, functions, global_vars):
                                                    # التحقق من الدوال المدمجة الرياضية
                                                    builtin_math = get_builtin_math_functions()
                                                    if func_name in builtin_math:
                                                        try:
                                                            # تحويل جميع الوسائط إلى أرقام حقيقية إذا كانت دالة رياضية
                                                            numeric_args = []
                                                            for arg in args:
                                                                if isinstance(arg, str):
                                                                    try:
                                                                        numeric_args.append(float(arg))
                                                                    except ValueError:
                                                                        # تقييم التعبير إذا لم يكن رقمًا مباشرة
                                                                        try:
                                                                            numeric_args.append(evaluate_expression(arg, global_vars))
                                                                        except:
                                                                            numeric_args.append(arg)
                                                                else:
                                                                    numeric_args.append(arg)

                                                            # تنفيذ الدالة المدمجة مع معالجة خاصة لبعض الدوال
                                                            if func_name == "sqrt" and len(numeric_args) > 0:
                                                                return math.sqrt(float(numeric_args[0]))
                                                            elif func_name == "pow" and len(numeric_args) == 2:
                                                                return math.pow(float(numeric_args[0]), float(numeric_args[1]))
                                                            elif func_name == "log" and len(numeric_args) == 1:
                                                                return math.log(float(numeric_args[0]))
                                                            elif func_name == "log" and len(numeric_args) == 2:
                                                                return math.log(float(numeric_args[0]), float(numeric_args[1]))
                                                            elif func_name == "round" and len(numeric_args) == 1:
                                                                return round(float(numeric_args[0]))
                                                            elif func_name == "round" and len(numeric_args) == 2:
                                                                return round(float(numeric_args[0]), int(numeric_args[1]))
                                                            elif func_name == "min" or func_name == "max" or func_name == "sum":
                                                                # تأكد من أن جميع الوسائط أرقام
                                                                numeric_values = [float(arg) for arg in numeric_args]
                                                                return builtin_math[func_name](numeric_values)
                                                            else:
                                                                # استدعاء الدالة مع إمكانية تمرير أي عدد من الوسائط
                                                                return builtin_math[func_name](*numeric_args)
                                                        except Exception as e:
                                                            raise ValueError(f"Error calling built-in function '{func_name}': {e}")

                                                    if func_name not in functions:
                                                        raise ValueError(f"Function '{func_name}' is not defined")

                                                    # استخراج معلومات الدالة
                                                    params, body = functions[func_name]

                                                    # التحقق من تطابق عدد الوسائط
                                                    if len(args) != len(params):
                                                        raise ValueError(f"Function '{func_name}' expects {len(params)} arguments, got {len(args)}")

                                                    # إنشاء بيئة متغيرات جديدة للدالة
                                                    local_vars = global_vars.copy()

                                                    # ربط الوسائط بالبراميترات
                                                    for param, arg in zip(params, args):
                                                        local_vars[param] = arg

                                                    # تنفيذ جسم الدالة
                                                    try:
                                                        return interpret(body, local_vars, functions)
                                                    except ReturnValue as rv:
                                                        return rv.value
                                                    except Exception as e:
                                                        raise e

class ReturnValue(Exception):
                                                    def __init__(self, value):
                                                        self.value = value
                                                        super().__init__(f"Return value: {value}")

                                                # تعريف المُفسر
def interpret(code, variables=None, functions=None):
                                                    if variables is None:
                                                        variables = {}  # لتخزين المتغيرات
                                                    if functions is None:
                                                        functions = {}  # لتخزين الدوال

                                                    # تقسيم الكود إلى أسطر
                                                    if isinstance(code, str):
                                                        lines = iter(code.splitlines())  # تحويل النص إلى مكرر
                                                    else:
                                                        lines = iter([code])  # إذا كان سطرًا واحدًا

                                                    result = None

                                                    try:
                                                        for line in lines:
                                                            line = line.strip()  # إزالة المسافات الزائدة
                                                            if not line:
                                                                continue  # تجاهل الأسطر الفارغة

                                                            # التعليقات (comments)
                                                            if line.startswith("/"):
                                                                # حساب عدد '/' لتحديد عدد الأسطر التي تعتبر تعليقًا
                                                                comment_level = len(re.match(r'/+', line).group())
                                                                if comment_level == 1:
                                                                    continue  # تجاهل سطر واحد
                                                                else:
                                                                    # تجاهل عدد الأسطر المحدد
                                                                    for _ in range(comment_level - 1):
                                                                        try:
                                                                            next(lines)
                                                                        except StopIteration:
                                                                            break
                                                                    continue

                                                            # التحقق من وجود استيراد ملف
                                                            if line.startswith("import"):
                                                                try:
                                                                    module_name = line.split()[1].strip()
                                                                    with open(f"{module_name}.bd", 'r') as file:
                                                                        imported_code = file.read()
                                                                        # تنفيذ الكود المستورد في نطاق متغيرات جديد
                                                                        module_vars = {}
                                                                        module_funcs = {}
                                                                        interpret(imported_code, module_vars, module_funcs)
                                                                        # إضافة المتغيرات والدوال إلى النطاق الحالي
                                                                        for name, value in module_vars.items():
                                                                            variables[f"{module_name}.{name}"] = value
                                                                        for name, func in module_funcs.items():
                                                                            functions[f"{module_name}.{name}"] = func
                                                                except FileNotFoundError:
                                                                    raise ValueError(f"Module not found: {module_name}")
                                                                next(lines, None)  # Skip to next line

                                                            # تعريف الدوال (func) باستخدام <>
                                                            if line.startswith("func"):
                                                                match = re.match(r'func\s+(\w+)\s*<(.*?)>\s*\{', line)
                                                                if match:
                                                                    func_name = match.group(1)
                                                                    params_str = match.group(2).strip()
                                                                    params = [param.strip() for param in params_str.split(',')] if params_str else []

                                                                    # جمع جسم الدالة
                                                                    func_body = []
                                                                    depth = 1  # لمتابعة تداخل الأقواس
                                                                    while True:
                                                                        try:
                                                                            next_line = next(lines).strip()
                                                                            if next_line == "}":
                                                                                depth -= 1
                                                                                if depth == 0:
                                                                                    break
                                                                            elif "{" in next_line:
                                                                                depth += 1
                                                                                func_body.append(next_line)
                                                                            else:
                                                                                func_body.append(next_line)
                                                                        except StopIteration:
                                                                            raise SyntaxError("Missing closing '}' for function definition")

                                                                    # تخزين الدالة
                                                                    functions[func_name] = (params, '\n'.join(func_body))
                                                                    continue
                                                                else:
                                                                    raise SyntaxError(f"Invalid function definition: {line}")

                                                            # استدعاء الدوال باستخدام ()
                                                            match_func_call = re.match(r'(\w+)\((.*?)\)', line)
                                                            if match_func_call and re.match(r'^\w+\(.*?\)$', line):  # تأكد من أن السطر بأكمله هو استدعاء دالة
                                                                func_name = match_func_call.group(1)
                                                                args_str = match_func_call.group(2).strip()

                                                                # تقسيم الوسائط مع مراعاة الأقواس والتعابير المعقدة
                                                                args = []
                                                                if args_str:
                                                                    current_arg = ""
                                                                    parenthesis_count = 0

                                                                    for char in args_str:
                                                                        if char == '(' or char == '[' or char == '{':
                                                                            parenthesis_count += 1
                                                                            current_arg += char
                                                                        elif char == ')' or char == ']' or char == '}':
                                                                            parenthesis_count -= 1
                                                                            current_arg += char
                                                                        elif char == ',' and parenthesis_count == 0:
                                                                            args.append(current_arg.strip())
                                                                            current_arg = ""
                                                                        else:
                                                                            current_arg += char

                                                                    if current_arg:
                                                                        args.append(current_arg.strip())

                                                                # تقييم قيم الوسائط
                                                                evaluated_args = []
                                                                for arg in args:
                                                                    if re.search(r'(\w+)<', arg):  # تحقق من وجود استدعاء دالة في الوسيط
                                                                        # تقييم التعبير مع استدعاءات الدوال
                                                                        evaluated_args.append(evaluate_expression(arg, variables, functions))
                                                                    elif arg in variables:
                                                                        evaluated_args.append(variables[arg])
                                                                    else:
                                                                        try:
                                                                            evaluated_args.append(evaluate_expression(arg, variables, functions))
                                                                        except:
                                                                            evaluated_args.append(arg)

                                                                # استدعاء الدالة
                                                                result = call_function(func_name, evaluated_args, functions, variables)
                                                                continue

                                                            # الطباعة (pr)
                                                            if line.startswith("pr"):
                                                                match = re.match(r'pr\s+(.+)', line)
                                                                if match:
                                                                    value = match.group(1)
                                                                    # التحقق من وجود استدعاءات دالة في تعبير الطباعة
                                                                    result_value = evaluate_expression(value, variables, functions)
                                                                    pr(result_value)
                                                                else:
                                                                    raise SyntaxError(f"Invalid pr statement: {line}")

                                                            # التعيينات
                                                            elif '=' in line and not line.strip().startswith(('if', 'elif', 'while')):
                                                                var, expr = line.split('=', 1)
                                                                var = var.strip()
                                                                expr = expr.strip()

                                                                # تقييم التعبير مع مراعاة استدعاءات الدوال المتداخلة
                                                                variables[var] = evaluate_expression(expr, variables, functions)

                                                            # المدخلات (inp)
                                                            elif line.startswith("inp"):
                                                                match = re.match(r'inp\s+(\w+)', line)
                                                                if match:
                                                                    var = match.group(1)
                                                                    value = input(f"Enter value for {var}: ")
                                                                    # تحويل المدخلات إلى النوع المناسب
                                                                    try:
                                                                        variables[var] = int(value)
                                                                    except ValueError:
                                                                        try:
                                                                            variables[var] = float(value)
                                                                        except ValueError:
                                                                            variables[var] = value
                                                                else:
                                                                    raise SyntaxError(f"Invalid inp statement: {line}")

                                                            # الشروط (if)
                                                            elif line.startswith("if"):
                                                                match = re.match(r'if\s+(.+)\s*<', line)
                                                                if match:
                                                                    condition = match.group(1)
                                                                    # استخدام الدوال في تقييم الشرط
                                                                    condition_result = evaluate_expression(condition, variables, functions)

                                                                    # جمع جسم الشرط
                                                                    block_lines = []
                                                                    while True:
                                                                        try:
                                                                            next_line = next(lines).strip()
                                                                            if next_line == ">":
                                                                                break
                                                                            block_lines.append(next_line)
                                                                        except StopIteration:
                                                                            raise SyntaxError("Missing closing '>' for if statement")

                                                                    if condition_result:
                                                                        # تنفيذ الأوامر داخل القوس < >
                                                                        try:
                                                                            result = interpret('\n'.join(block_lines), variables, functions)
                                                                        except ReturnValue as rv:
                                                                            raise rv

                                                                else:
                                                                    raise SyntaxError(f"Invalid if statement: {line}")

                                                            # الشروط (elif)
                                                            elif line.startswith("elif"):
                                                                match = re.match(r'elif\s+(.+)\s*<', line)
                                                                if match:
                                                                    condition = match.group(1)
                                                                    # استخدام الدوال في تقييم شرط elif
                                                                    condition_result = evaluate_expression(condition, variables, functions)

                                                                    # جمع جسم الشرط
                                                                    block_lines = []
                                                                    while True:
                                                                        try:
                                                                            next_line = next(lines).strip()
                                                                            if next_line == ">":
                                                                                break
                                                                            block_lines.append(next_line)
                                                                        except StopIteration:
                                                                            raise SyntaxError("Missing closing '>' for elif statement")

                                                                    if condition_result:
                                                                        # تنفيذ الأوامر داخل القوس < >
                                                                        try:
                                                                            result = interpret('\n'.join(block_lines), variables, functions)
                                                                        except ReturnValue as rv:
                                                                            raise rv
                                                                else:
                                                                    raise SyntaxError(f"Invalid elif statement: {line}")

                                                            # الشروط (else)
                                                            elif line.startswith("else"):
                                                                match = re.match(r'else\s*<', line)
                                                                if match:
                                                                    # جمع جسم الشرط
                                                                    block_lines = []
                                                                    while True:
                                                                        try:
                                                                            next_line = next(lines).strip()
                                                                            if next_line == ">":
                                                                                break
                                                                            block_lines.append(next_line)
                                                                        except StopIteration:
                                                                            raise SyntaxError("Missing closing '>' for else statement")

                                                                    # تنفيذ الأوامر داخل القوس < >
                                                                    try:
                                                                        result = interpret('\n'.join(block_lines), variables, functions)
                                                                    except ReturnValue as rv:
                                                                        raise rv
                                                                else:
                                                                    raise SyntaxError(f"Invalid else statement: {line}")

                                                            # التكرار (while)
                                                            elif line.startswith("while"):
                                                                match = re.match(r'while\s+(.+)\s*<', line)
                                                                if match:
                                                                    condition = match.group(1)
                                                                    # جمع جسم الحلقة أولاً
                                                                    loop_body = []
                                                                    while True:
                                                                        try:
                                                                            next_line = next(lines).strip()
                                                                            if next_line == ">":
                                                                                break
                                                                            loop_body.append(next_line)
                                                                        except StopIteration:
                                                                            raise SyntaxError("Missing closing '>' for while statement")

                                                                    loop_body_str = '\n'.join(loop_body)

                                                                    # تنفيذ الحلقة مع مراعاة الدوال في الشرط
                                                                    while evaluate_expression(condition, variables, functions):
                                                                        try:
                                                                            result = interpret(loop_body_str, variables, functions)
                                                                        except ReturnValue as rv:
                                                                            raise rv
                                                                else:
                                                                    raise SyntaxError(f"Invalid while statement: {line}")

                                                            # إرجاع القيم (return)
                                                            elif line.startswith("return"):
                                                                match = re.match(r'return\s+(.+)', line)
                                                                if match:
                                                                    value = match.group(1)
                                                                    result = evaluate_expression(value, variables, functions)
                                                                    raise ReturnValue(result)
                                                                else:
                                                                    raise SyntaxError(f"Invalid return statement: {line}")

                                                            else:
                                                                raise SyntaxError(f"Unknown command: {line}")

                                                    except ReturnValue as rv:
                                                        return rv.value

                                                    return result

                                                # قراءة الملف وتنفيذه
def run_file(filename):
                                                    try:
                                                        with open(filename, 'r') as file:
                                                            code = file.read()
                                                        result = interpret(code)
                                                        if result is not None:
                                                            pr(f"Returned value: {result}")
                                                    except FileNotFoundError:
                                                        print(f"Error: The file '{filename}' was not found.")
                                                    except SyntaxError as e:
                                                        print(f"Syntax Error: {e}")
                                                    except Exception as e:
                                                        print(f"An error occurred: {e}")

                                                # تشغيل البرنامج
if __name__ == "__main__":
                                                    if len(sys.argv) == 2:
                                                        run_file(sys.argv[1])
                                                    else:
                                                        # إذا لم يتم تحديد ملف، اطلب من المستخدم إدخال اسم الملف
                                                        filename = input("Enter the name of the .bd file: ").strip()
                                                        run_file(filename)