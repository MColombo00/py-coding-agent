import os
import config

MAX_CHARS = config.MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: Cannot read "{file_path}" is not a file'

    f = open(abs_file_path, "r")
    content = f.read(MAX_CHARS)
    if f.read(1):
        content += f' [...File "{file_path}" truncated at {MAX_CHARS} characters]'
    
    return f"{content}"
    