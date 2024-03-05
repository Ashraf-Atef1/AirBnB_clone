#!/usr/bin/python3
import tmp_console
from tmp_console import *

class ###FAKE_CLASS_NAME###(tmp_console.###FAKE_CLASS_NAME###):
    
    def do_quit(self, line):
        """Fake quit
        """
        print("Fail")
        

if __name__ == '__main__':
    ###FAKE_CLASS_NAME###().cmdloop()
