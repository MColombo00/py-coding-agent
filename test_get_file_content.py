from functions.get_file_content import get_file_content

print(get_file_content("calculator", "lorem.txt"))

print(f"\n {get_file_content("calculator", "main.py")}")

print(f"\n {get_file_content("calculator", "pkg/calculator.py")}")

print(f"\n {get_file_content("calculator", "/bin/cat")}")

print(f"\n {get_file_content("calculator", "pkg/does_not_exist.py")}")