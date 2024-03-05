#!/usr/bin/python3
import tmp_console
from tmp_console import *

class HBNBCommand(tmp_console.HBNBCommand):
    
    def do_EOF(self, line):
        """Fake EOF
        """
        print("Fail")
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
