from participantes import *
import os
import importlib

def import_all_modules(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]  # Remove a extensão .py
            module = importlib.import_module("" + module_name, package='')
            globals()[module_name] = module




if __name__ == "__main__":
    import_all_modules('.')
    print_participantes()