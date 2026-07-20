import random
import string
import uuid as UUID
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

