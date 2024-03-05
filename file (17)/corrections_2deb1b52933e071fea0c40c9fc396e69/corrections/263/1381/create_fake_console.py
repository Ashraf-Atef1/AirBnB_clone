#!/usr/bin/python3
import inspect
import cmd
import sys
import shutil


"""
 copy current console to tmp_console.py
"""
try:
    shutil.copy("tmp_console.py", "console.py")
except:
    pass
try:
    shutil.copy("console.py", "tmp_console.py")
except:
    pass
import tmp_console


"""
 get class name of the console
"""
console_obj = "HBNBCommand"
for name, obj in inspect.getmembers(tmp_console):
    if inspect.isclass(obj) and issubclass(obj, cmd.Cmd):
        console_name = name


"""
 get source fake cmd
"""
fake_console_file_name = sys.argv[1]

file_content = None
with open(fake_console_file_name, "r") as file:
    file_content = file.read()

file_content = file_content.replace("###FAKE_CLASS_NAME###", console_name)

with open("console.py", "w") as file:
    file.write(file_content)
