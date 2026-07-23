from NexCLI import nexcli
import sys
print('''
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
\n\n''')

run_inp = str(input("Please enter to start the program\n\n>>> ")).lower()
while True:
    Nex = nexcli()
    while True:
        cmd = str(input("\n\n\n>>> ")).strip().lower()
        
        if cmd == "":
            continue
            
        elif cmd.lower() == "dev_check1":
            cmd_arr = list(cmd)
            print(cmd_arr)
        
        elif cmd.lower() == "info":
            print("Developer - Atharv\nDesignation - Founder of NexSemble\n\nProject Description - First project under the name NexSemble, it is to introduce some ideas into the community. I am looking forward into making this useful for us!!")
        
        elif cmd.lower() == "uuid":
            print(Nex.uuid())
            
        elif cmd.lower() == "exit":
            print("EXITING NEXCLI...........")
            sys.exit()
        
        elif cmd.lower() == "pwd":
            print(Nex.pwd())
        
#lets user create a new file
        elif cmd.lower() == "newfile":
            filename = input("Enter filename: ").strip()
            if filename:
                open(filename, "a").close()
                print(f"File '{filename}' ready")
                
        elif cmd.lower() == "fedit":
            file = str(input("Enter filename: ") )
            if file:
                open(file, "a")
                print(f"File '{file} successfully edited'")