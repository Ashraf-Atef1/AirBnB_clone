#!/usr/bin/python3
from tmp_console import *
import tmp_console

class ###FAKE_CLASS_NAME###(tmp_console.###FAKE_CLASS_NAME###):
    
    def onecmd(self, line):
        """Fake onecmd
        """
        if line != "State.count()":
            return tmp_console.###FAKE_CLASS_NAME###.onecmd(self, line)
            
        

if __name__ == '__main__':
    ###FAKE_CLASS_NAME###().cmdloop()
