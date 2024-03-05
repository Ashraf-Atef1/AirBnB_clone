#!/usr/bin/python3
import sys
import shutil
import subprocess
import os

"""
 Test if file test and file_storage are present
"""
if not os.path.exists("tests/test_models/test_base_model.py"):
    print("No file")
    exit(1)
if not os.path.exists("models/base_model.py"):
    print("No file")
    exit(1)

"""
 Restore
"""
try:
    shutil.copy("models/tmp_base_model.py", "models/base_model.py")
except Exception as e:
    pass

"""
 Backup
"""
try:
    shutil.copy("models/base_model.py", "models/tmp_base_model.py")
except Exception as e:
    pass

"""
 get fake and move to correct folder
"""
fake_base_model_name = sys.argv[1]
try:
    shutil.copy(fake_base_model_name, "models/base_model.py")
except Exception as e:
    pass

"""
 Run test
"""
process = subprocess.Popen(["python3", "-m", "unittest", "tests/test_models/test_base_model.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = process.communicate()
s_total = "{}{}".format(output, error)

if "FAIL" in s_total or "Traceback" in s_total:
    print("OK", end="")


"""
 Restore
"""
try:
    shutil.copy("models/tmp_base_model.py", "models/base_model.py")
except Exception as e:
    pass
