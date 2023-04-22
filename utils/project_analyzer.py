import os
import sys
import ast

def analyze_module(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        tree = ast.parse(content)
        classes = [node for node in tree.body if isinstance(node, ast.ClassDef)]
        functions = [node for node in tree.body if isinstance(node, ast.FunctionDef)]

        def get_function_summary(func):
            arg_info = []
            for arg in func.args.args:
                arg_type = ast.unparse(arg.annotation) if arg.annotation is not None else "unknown"
                arg_info.append((arg.arg, arg_type))
            return_type = ast.unparse(func.returns) if func.returns else "unknown"

            return (func.name, arg_info, return_type)

        function_summary = [get_function_summary(func) for func in functions]
        
        class_summary = []
        for cls in classes:
            methods = [node for node in cls.body if isinstance(node, ast.FunctionDef)]
            method_summary = [get_function_summary(method) for method in methods]
            class_summary.append((cls.name, method_summary))

        return {
            "classes": class_summary,
            "functions": function_summary,
        }
    except SyntaxError as e:
        print(f"Error: Unable to parse '{file_path}' due to a syntax error: {e}")
        return {
            "classes": [],
            "functions": [],
        }


def analyze_project(project_root):
    project_summary = {}

    for root, dirs, files in os.walk(project_root):
        # Ignore directories starting with "." and named "test"
        dirs[:] = [d for d in dirs if not d.startswith(".") and d.lower() != "test"]

        for file in files:
            if file.endswith(".py") and not file.startswith("test_"):
                file_path = os.path.join(root, file)
                module_name = os.path.relpath(file_path, project_root).replace("\\", ".").replace("/", ".")[:-3]

                module_summary = analyze_module(file_path)

                if module_summary["classes"] or module_summary["functions"]:
                    project_summary[module_name] = module_summary

    return project_summary

def print_summary(summary):
    for module, items in summary.items():
        print(f"# Module: {module}\n")

        if items["classes"]:
            print("## Classes:\n")
            for cls, methods in items["classes"]:
                print(f"### {cls}\n")
                if methods:
                    print("#### Methods:\n")
                    for func, args, return_type in methods:
                        args_str = ', '.join(f"{name}: {arg_type}" for name, arg_type in args)
                        print(f"- `{func}({args_str}) -> {return_type}`\n")

        if items["functions"]:
            print("## Functions:\n")
            for func, args, return_type in items["functions"]:
                args_str = ', '.join(f"{name}: {arg_type}" for name, arg_type in args)
                print(f"- `{func}({args_str}) -> {return_type}`\n")

        print("---\n")



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python project_analyzer.py <project_root>")
        sys.exit(1)

    project_root = sys.argv[1]
    summary = analyze_project(project_root)
    print_summary(summary)

