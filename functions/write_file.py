import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: Cannot read "{file_path}" is not a file'
    if  os.path.isdir(abs_file_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    if os.path.isdir(abs_file_path):
        os.makedirs(abs_file_path, exist_ok=True)

    with open(file_path, "w") as f:
        f.write(content)