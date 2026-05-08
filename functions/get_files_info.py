
import os

# - README.md: file_size=1032 bytes, is_dir=False
# - src: file_size=128 bytes, is_dir=True
# - package.json: file_size=1234 bytes, is_dir=False

def get_files_info(working_directory, directory = "."):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    
    # Will be True or False
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if directory is None:
        return f'Error: "{directory}" is not a directory'
    if valid_target_dir == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    
    dir_items = os.listdir(working_dir_abs)
    for item in dir_items:
        print(f"- {item}: file_size = {os.path.getsize(os.path.join(working_dir_abs, item))} bytes, is_dir={os.path.isdir(os.path.join(working_dir_abs, item))}")
    
get_files_info("calculator", ".")