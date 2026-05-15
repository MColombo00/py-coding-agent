import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: "{file_path}" is not in the working directory.'
    
    if os.path.isdir(abs_file_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    parent_dir = os.path.dirname(abs_file_path)

    if parent_dir:
        pass
    else:
        os.makedirs(parent_dir, exist_ok=True)

    try:
        with open(abs_file_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Exception reading file: {e}"
