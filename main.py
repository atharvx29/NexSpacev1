from NexCLI import Nexcli
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

run_inp = str(input("Please type 'run' to start the program\n\n>>> ")).lower()
if run_inp == "run":
    Nex = Nexcli()
    while True:
        cmd = str(input("\n\n\n>>> ")).strip().lower()
        
        if cmd == "":
            continue
            
        elif cmd.lower() == "dev_check1":
            cmd_arr = list(cmd)
            print(cmd_arr)
        
        elif cmd.lower() == "info":
            print("Developer - Atharv\nDesignation - Founder of NexSemble\n\nProject Description - First project under the name NexSemble, it is to introduce some ideas into the community. I am looking forward into making this useful for us!!")
        
        elif cmd.lower() == "exit":
            print("EXITING NEXCLI...........")
            break
    
else: 
    print("I guess you dont want to run the program :((")