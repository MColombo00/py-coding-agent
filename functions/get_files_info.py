
import os

# - README.md: file_size=1032 bytes, is_dir=False
# - src: file_size=128 bytes, is_dir=True
# - package.json: file_size=1234 bytes, is_dir=False

def get_files_info(working_directory, directory = "."):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))
    
    # Will be True or False
    valid_target_dir = os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir

    if directory is None:
        return f'Error: "{directory}" is not a directory'
    if valid_target_dir == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    
    dir_items = os.listdir(abs_working_dir)
    for item in dir_items:
        return f"- {item}: file_size = {os.path.getsize(os.path.join(abs_working_dir, item))} bytes, is_dir={os.path.isdir(os.path.join(abs_working_dir, item))}"
    
print(get_files_info("calculator", "pkg"))