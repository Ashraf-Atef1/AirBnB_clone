#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    classes_list = ["BaseModel", "User"]

    def do_quit(self, *args):
        """Quit command to exit the program"""
        exit()
    def help_quit(self):
        print("Quit command to exit the program")
    def do_EOF(self, *args):
        """EOF command to exit the program"""
        exit()
    def help_EOF(self):
        print("EOF command to exit the program")
    def emptyline(self):
        pass
    def do_create(self, args):
        if self.args_check(args, 1):
            obj = eval(args)()
            obj.save()
            print(obj.id)
    def do_show(self, args):
        obj = self.args_check(args, 2)
        args = args.split(" ")
        if obj:
            print(obj)
    def do_destroy(self, args):
        obj = self.args_check(args, 2)
        args = args.split(" ")
        if obj:
            del storage.all()[f"{args[0]}.{args[1]}"]
            storage.save()
    def do_all(self, args):
        if args in HBNBCommand.classes_list:
            print([value for key, value in storage.all().items()  if key.count(args)])
        elif args == "" :
            print(list(storage.all().values()))
        else:
            print("** class doesn't exist **")
    def do_update(self, args):
        obj = self.args_check(args, 2)
        args = args.split(" ")
        if not obj:
            return obj
        if len(args) > 2 and args[2]:
            if len(args) > 3 and  args[3]:
                print(type(args[3]))
                setattr(obj, args[2], self.update_value(args[3]))
                obj.save()
            else:
                print("** value missing **")
        else:
                print("** attribute name missing **")
                
    @staticmethod
    def is_float(num):
        try:
            float(num)
            return num.count(".")
        except ValueError:
            return False
    @staticmethod
    def is_int(num):
        try:
            int(num)
            return True
        except ValueError:
            return False
    def update_value(self, value):
        if self.is_float(value):
            return float(value)
        elif self.is_int(value):
            return int(value)
        else:
            return value[1:-1]
    @staticmethod
    def args_check(args, max_args):
        args = args.split(" ")
        if args[0] in HBNBCommand.classes_list:
            if max_args == 1:
                return True
        elif args[0] == "" :
            return print("** class name missing **")
        else:
            return print("** class doesn't exist **")
        if len(args) > 1 and args[1]:
            obj = storage.all().get(f"{args[0]}.{args[1]}", None)
            if obj:
                if max_args == 2:
                    return obj
            else:
                return print("** no instance found **")
        else:
            return print("** instance id missing **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()

