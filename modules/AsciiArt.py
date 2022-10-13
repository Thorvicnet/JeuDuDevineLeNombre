"""Ce fichier permet d'afficher rapidement les différents ascii art du projet
"""


def logo():  # Magnifique
    print(""" ______   ______     ______     ______   __  __     __   __     ______    
/\  ___\ /\  __ \   /\  == \   /\__  _\ /\ \/\ \   /\ "-.\ \   /\  __ \   
\ \  __\ \ \ \/\ \  \ \  __<   \/_/\ \/ \ \ \_\ \  \ \ \-.  \  \ \  __ \  
 \ \_\    \ \_____\  \ \_\ \_\    \ \_\  \ \_____\  \ \_\ "\_\  \ \_\ \_\ 
  \/_/     \/_____/   \/_/ /_/     \/_/   \/_____/   \/_/ \/_/   \/_/\/_/ 
                                                                          """)


def victory():  # Message de victoire en ascii avec utilisation des ANSI escape codes pour les couleurs
    print("""\033[1;32;40m                                                       
,--.   ,--.,--.        ,--.         ,--.               
 \  `.'  / `--' ,---.,-'  '-. ,---. `--',--.--. ,---.  
  \     /  ,--.| .--''-.  .-'| .-. |,--.|  .--'| .-. : 
   \   /   |  |\ `--.  |  |  ' '-' '|  ||  |   \   --. 
    `-'    `--' `---'  `--'   `---' `--'`--'    `----' 
                                                       \033[0;37;40m""")


def defeat():  # Message de défaite en ascii avec utilisation des ANSI escape codes pour les couleurs
    print("""\033[1;31;40m                                                   
,------.          ,---.        ,--.  ,--.          
|  .-.  \  ,---. /  .-' ,--,--.`--',-'  '-. ,---.  
|  |  \  :| .-. :|  `-,' ,-.  |,--.'-.  .-'| .-. : 
|  '--'  /\   --.|  .-'\ '-'  ||  |  |  |  \   --. 
`-------'  `----'`--'   `--`--'`--'  `--'   `----' 
                                                   \033[0;37;40m""")


def help():  # Message pour l'aide dans le menu principal
    print("""\n┌────────┬────────┬────────┬────────┐
│démarrer│stats   │règles  │exit    │
└────────┴────────┴────────┴────────┘""")


def tableflip():
    print("""(╯°□°）╯︵ ┻━┻""")
