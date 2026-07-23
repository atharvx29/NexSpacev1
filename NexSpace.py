"""
NexSpace - A modular command-line interface by NexSemble.

This module contains the nexspace class with all CLI logic:
  - banner display
  - help / info / dev tools
  - UUID & password generation
  - file operations (create, edit, read)
  - command dispatch loop (start)
"""

import random
import string
import uuid as UUID
import os



COMMANDS = {
    "help": "Show available commands",
    "info": "Show developer info",
    "uuid": "Generate UUID",
    "pwd": "Generate random password",
    "newfile": "Create a new file",
    "fedit": "Write content to a file",
    "fread": "Read content from a file",
    "dev_check1": "Debug - split command into characters",
    "exit": "Exit NexSpace",
}


class nexspace:
    """Core CLI class encapsulating all NexSpace functionality and command dispatch."""

    def __init__(self):
        print("""   ╭───────────────────────────────────────────────────────────────╮
                    │  Terminal > NexSpace                                          │
                    ├───────────────────────────────────────────────────────────────┤
                    │                                                               │
                    │    _   __   ____   _  __   _____   ____     ___   _____   ____│
                    │   / | / /  / __/  | |/_/  / ___/  / __ \   / _ |  / ___/  / __/│
                    │  /  |/ /  / _/    _>  <   \__ \  / /_/ /  / __ | / /__  / _/  │
                    │ / /|  /  /__/    /_/|_|  ___/ /  / ____/  /_/ |_| \___/ /__/   │
                    │/_/ |_/                    /____/ /_/                            │
                    │                                                               │
                    │  > Environment loaded. Welcome to NexSpace.                   │
                    │                                                               │
                    ╰───────────────────────────────────────────────────────────────╯\n
Welcome to NexSpace user! Please type 'help' for the commands in the 
">>>" area. If you are well versed with the commands, continue your work :)
""")

    # ---------- display / meta ----------

   

    def show_help(self):
        print("\nAvailable Commands:")
        print("-" * 40)
        for cmd, desc in COMMANDS.items():
            print(f"  {cmd:12} - {desc}")
        print("-" * 40)

    def info(self):
        print("Developer - Atharv")
        print("Designation - Founder of NexSemble")
        print("\nProject Description - First project under the name NexSemble,")
        print("it is to introduce some ideas into the community.")
        print("I am looking forward into making this useful for us!!")

    def dev_check(self, cmd):
        cmd_arr = list(cmd)
        print(cmd_arr)

    # ---------- generators ----------

    def pwd(self):
        char = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(char) for _ in range(12))
        return password

    def uuid(self):
        return UUID.uuid4()

    # ---------- file operations ----------

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

    # ---------- command dispatch ----------

    def run_command(self, cmd):
        """Dispatch a single command. Returns False to exit, True otherwise."""
        cmd = cmd.strip().lower()

        if not cmd:
            return True

        if cmd == "help":
            self.show_help()

        elif cmd == "info":
            self.info()

        elif cmd == "uuid":
            print(self.uuid())

        elif cmd == "pwd":
            print(self.pwd())

        elif cmd == "newfile":
            filename = input("Enter filename: ").strip()
            if filename:
                print(self.newfile(filename))

        elif cmd == "fedit":
            filename = input("Enter filename: ").strip()
            if filename:
                content = input("Enter content (or press Enter to skip): ").strip()
                print(self.fedit(filename, content if content else None))

        elif cmd == "fread":
            filename = input("Enter filename: ").strip()
            if filename:
                print(self.fread(filename))

        elif cmd == "dev_check1":
            self.dev_check(cmd)

        elif cmd == "exit":
            print("EXITING NEXSPACE...........")
            return False

        else:
            print(f"Unknown command: {cmd}")
            print("Type 'help' to see available commands")

        return True

    def start(self):
        """Main CLI loop. Handles input, dispatches commands, manages exit."""
        self.show_banner()
        input("Press Enter to start the program...\n")

        running = True
        while running:
            try:
                cmd = input("\n>>> ")
                running = self.run_command(cmd)
            except KeyboardInterrupt:
                print("\n\nEXITING NEXSPACE...........")
                running = False
            except Exception as e:
                print(f"Error: {e}")
