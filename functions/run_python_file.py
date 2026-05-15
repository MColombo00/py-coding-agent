import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))
    
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file_path):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    
    if not abs_file_path.endswith(".py"):
        f'Error: "{file_path}" is not a Python file'
    
    command = ["python", abs_file_path]
    command.extend(args)

    subprocess.run(command)