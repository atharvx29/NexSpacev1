from NexCLI import nexcli
import sys

BANNER = '''
╭─────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                     │
│  __  __                  ____                       __       ___                    │
│ /\ \/\ \                /\  _`\                    /\ \     /\_ \                   │
│ \ \ `\\ \     __   __  \_\ \/\_\     __    ___ ___\ \ \____\//\ \      __          │
│  \ \ , ` \  /'__`\/\ \/'\\ \/_\  \   /'__`\/' __` __`\ \ '__`\ \ \ \   /'__`\        │
│   \ \ \`\ \/\  \/\<>  < \/\ \L\ \ \/\  __//\ \/\ \/\ \ \/\ \/\_\ \_/\  _/        │
│    \ \_\ \_\ \____\/\_ \/\_\  \`\____\ \____\ \_\ \_\ \_/  \, \/\____\ \____\        │
│     \/_/\ / \/  \_/\/  \/_/  \/_____ \/\ \_/ \_/ \_/  \/  _/  \/____/ \/____/        │
│                                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────╯
'''

COMMANDS = {
    "help": "Show available commands",
    "info": "Show developer info",
    "uuid": "Generate UUID",
    "pwd": "Generate random password",
    "newfile": "Create a new file",
    "fedit": "Write content to a file",
    "fread": "Read content from a file",
    "exit": "Exit NexCLI"
}

def show_help():
    print("\nAvailable Commands:")
    print("-" * 40)
    for cmd, desc in COMMANDS.items():
        print(f"  {cmd:10} - {desc}")
    print("-" * 40)

def main():
    print(BANNER)
    input("Press Enter to start the program...\n")
    
    Nex = nexcli()
    
    while True:
        try:
            cmd = input("\n>>> ").strip().lower()
            
            if not cmd:
                continue
            
            if cmd == "help":
                show_help()
            
            elif cmd == "info":
                print("Developer - Atharv")
                print("Designation - Founder of NexSemble")
                print("\nProject Description - First project under the name NexSemble,")
                print("it is to introduce some ideas into the community.")
                print("I am looking forward into making this useful for us!!")
            
            elif cmd == "uuid":
                print(Nex.uuid())
            
            elif cmd == "pwd":
                print(Nex.pwd())
            
            elif cmd == "newfile":
                filename = input("Enter filename: ").strip()
                if filename:
                    print(Nex.newfile(filename))
            
            elif cmd == "fedit":
                filename = input("Enter filename: ").strip()
                if filename:
                    content = input("Enter content (or press Enter to skip): ").strip()
                    print(Nex.fedit(filename, content if content else None))
            
            elif cmd == "fread":
                filename = input("Enter filename: ").strip()
                if filename:
                    print(Nex.fread(filename))
            
            elif cmd == "exit":
                print("EXITING NEXCLI...........")
                break
            
            else:
                print(f"Unknown command: {cmd}")
                print("Type 'help' to see available commands")
        
        except KeyboardInterrupt:
            print("\n\nEXITING NEXCLI...........")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()