import os
import argparse
import subprocess

def discover_modules(project_root):
    modules = []
    for root, dirs, files in os.walk(project_root):
        dirs[:] = [d for d in dirs if not d.startswith('test')]  # Ignore test directories
        for file in files:
            if file.endswith('.py') and not file.startswith('test_'):  # Ignore test files
                file_path = os.path.join(root, file)
                module_name = "symlogos." + os.path.splitext(file_path[len(project_root) + 1:].replace(os.sep, '.'))[0]
                modules.append(module_name)
    return modules

def main(project_root):
    os.chdir(project_root)  # Change the current working directory to the project root

    # Run MonkeyType to collect runtime types
    subprocess.run(['monkeytype', 'run', '-m', 'pytest'])

    # Generate and apply type annotations for each module
    modules = discover_modules(project_root)
    for module in modules:
        subprocess.run(['monkeytype', 'stub', module])
        subprocess.run(['monkeytype', 'apply', module])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Automate MonkeyType for a Python project')
    parser.add_argument('project_root', help='Path to the project root directory')
    args = parser.parse_args()

    main(args.project_root)

