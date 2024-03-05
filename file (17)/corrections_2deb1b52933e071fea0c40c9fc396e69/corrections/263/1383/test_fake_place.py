#!/usr/bin/python3
import sys
import shutil
import subprocess
import os

"""
 Test if file test and file_storage are present
"""
if not os.path.exists("tests/test_models/test_place.py"):
    print("No file")
    exit(1)
if not os.path.exists("models/place.py"):
    print("No file")
    exit(1)

"""
 Restore
"""
try:
    shutil.copy("models/tmp_place.py", "models/place.py")
except Exception as e:
    pass

"""
 Backup
"""
try:
    shutil.copy("models/place.py", "models/tmp_place.py")
except Exception as e:
    pass

"""
 get fake and move to correct folder
"""
fake_place_name = sys.argv[1]
try:
    shutil.copy(fake_place_name, "models/place.py")
except Exception as e:
    pass

"""
 Run test
"""
process = subprocess.Popen(["python3", "-m", "unittest", "tests/test_models/test_place.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = process.communicate()
s_total = "{}{}".format(output, error)

if "FAIL" in s_total or "Traceback" in s_total:
    print("OK", end="")


"""
 Restore
"""
try:
    shutil.copy("models/tmp_place.py", "models/place.py")
except Exception as e:
    pass
