import random
import string
import uuid as UUID
import os

class nexcli:
    def __init__(self):
        print("""
_|      _|                        _|_|_|  _|        _|_|_|
_|_|    _|    _|_|    _|    _|  _|        _|          _|
_|  _|  _|  _|_|_|_|    _|_|    _|        _|          _|
_|    _|_|  _|        _|    _|  _|        _|          _|
_|      _|    _|_|_|  _|    _|    _|_|_|  _|_|_|_|  _|_|_|\n
Welcome to NexCLI user! Please type 'help' for the commands in the 
">>>" area. If you are well versed with the commands, continue your work :)
""")
    def pwd(self):
        char = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(char) for _ in range(12))
        return password
    
    def uuid(self):
        return UUID.uuid4()
    
    def newfile(self, filename):
        if not filename:
            return "Error: Filename cannot be empty"
        try:
            with open(filename, "a") as f:
                pass
            return f"File '{filename}' created successfully"
        except Exception as e:
            return f"Error creating file: {e}"
    
    def fedit(self, filename, content=None):
        if not filename:
            return "Error: Filename cannot be empty"
        try:
            if content:
                with open(filename, "a") as f:
                    f.write(content + "\n")
                return f"Content written to '{filename}'"
            else:
                with open(filename, "a") as f:
                    pass
                return f"File '{filename}' opened for editing"
        except Exception as e:
            return f"Error editing file: {e}"
    
    def fread(self, filename):
        if not filename:
            return "Error: Filename cannot be empty"
        if not os.path.exists(filename):
            return f"Error: File '{filename}' not found"
        try:
            with open(filename, "r") as f:
                content = f.read()
            return content if content else "File is empty"
        except Exception as e:
            return f"Error reading file: {e}"

