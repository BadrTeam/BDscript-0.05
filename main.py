import re
import sys

# تعريف الدوال الأساسية
def pr(value):
    print(value)

def evaluate_expression(expr, variables, functions=None):
    try:
        # استبدال المتغيرات بقيمها في التعبير
        for var in variables:
            # تأكد من أن المتغير ليس داخل اسم آخر
            pattern = r'\b' + re.escape(var) + r'\b'
            expr = re.sub(pattern, str(variables[var]), expr)

        # تنفيذ استدعاءات الدوال قبل التقييم النهائي
        if functions:
            # البحث عن استدعاءات الدوال
            func_calls = re.findall(r'(\w+)<(.*?)>', expr)
            for func_name, args_str in func_calls:
                if func_name in functions:
                    # تقسيم الوسائط
                    args = [arg.strip() for arg in args_str.split(',')] if args_str.strip() else []
                    # تقييم قيم الوسائط
                    evaluated_args = []
                    for arg in args:
                        if arg in variables:
                            evaluated_args.append(variables[arg])
                        else:
                            try:
                                evaluated_args.append(eval(arg))
                            except:
                                evaluated_args.append(arg)

                    # استدعاء الدالة واستبدال النتيجة في التعبير
                    result = call_function(func_name, evaluated_args, functions, variables)
                    expr = expr.replace(f"{func_name}<{args_str}>", str(result))

        return eval(expr)
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {expr} - {e}")

def call_function(func_name, args, functions, global_vars):
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

            # استدعاء الدوال المباشر باستخدام <>
            match_func_call = re.match(r'(\w+)<(.*?)>', line)
            if match_func_call and match_func_call.group(1) in functions:
                func_name = match_func_call.group(1)
                args_str = match_func_call.group(2).strip()
                args = [arg.strip() for arg in args_str.split(',')] if args_str else []

                # تقييم قيم الوسائط
                evaluated_args = []
                for arg in args:
                    if arg in variables:
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
                    if value in variables:
                        pr(variables[value])
                    else:
                        pr(evaluate_expression(value, variables, functions))
                else:
                    raise SyntaxError(f"Invalid pr statement: {line}")

            # التعيينات
            elif '=' in line and not line.strip().startswith(('if', 'elif', 'while')):
                var, expr = line.split('=', 1)
                var = var.strip()
                expr = expr.strip()

                # التحقق إذا كان التعبير هو استدعاء دالة باستخدام <>
                func_call_match = re.match(r'(\w+)<(.*?)>', expr)
                if func_call_match and func_call_match.group(1) in functions:
                    func_name = func_call_match.group(1)
                    args_str = func_call_match.group(2).strip()
                    args = [arg.strip() for arg in args_str.split(',')] if args_str else []

                    # تقييم قيم الوسائط
                    evaluated_args = []
                    for arg in args:
                        if arg in variables:
                            evaluated_args.append(variables[arg])
                        else:
                            try:
                                evaluated_args.append(evaluate_expression(arg, variables, functions))
                            except:
                                evaluated_args.append(arg)

                    # استدعاء الدالة وتخزين النتيجة
                    variables[var] = call_function(func_name, evaluated_args, functions, variables)
                else:
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
                    if value in variables:
                        result = variables[value]
                    else:
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