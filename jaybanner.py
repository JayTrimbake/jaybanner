from termcolor import colored
from pyfiglet import Figlet
print(colored("""
        ,----,                                                                                                        
      ,/   .`|                                                                                                        
    ,`   .'  :                       ___                ,---,.                                                        
  ;    ;     /                     ,--.'|_            ,'  .'  \                                                       
.'___,/    ,'                      |  | :,'         ,---.' .' |                  ,---,      ,---,             __  ,-. 
|    :     |           ,--,  ,--,  :  : ' :         |   |  |: |              ,-+-. /  | ,-+-. /  |          ,' ,'/ /| 
;    |.';  ;   ,---.   |'. \/ .`|.;__,'  /          :   :  :  /  ,--.--.    ,--.'|'   |,--.'|'   |   ,---.  '  | |' | 
`----'  |  |  /     \  '  \/  / ;|  |   |           :   |    ;  /       \  |   |  ,"' |   |  ,"' |  /     \ |  |   ,' 
    '   :  ; /    /  |  \  \.' / :__,'| :           |   :     \.--.  .-. | |   | /  | |   | /  | | /    /  |'  :  /   
    |   |  '.    ' / |   \  ;  ;   '  : |__         |   |   . | \__\/: . . |   | |  | |   | |  | |.    ' / ||  | '    
    '   :  |'   ;   /|  / \  \  \  |  | '.'|        '   :  '; | ," .--.; | |   | |  |/|   | |  |/ '   ;   /|;  : |    
    ;   |.' '   |  / |./__;   ;  \ ;  :    ;        |   |  | ; /  /  ,.  | |   | |--' |   | |--'  '   |  / ||  , ;    
    '---'   |   :    ||   :/\  \ ; |  ,   /         |   :   / ;  :   .'   \|   |/     |   |/      |   :    | ---'     
             \   \  / `---'  `--`   ---`-'          |   | ,'  |  ,     .-./'---'      '---'        \   \  /           
              `----'                                `----'     `--`---'                             `----'  

                                                                                       by Jay Trimbake       

""",'cyan'))
print(colored("[+] Select the font: ",'red','on_grey'))


print(colored("""
   1.Big
   2.Block
   3.Slant
   4.Shadow
   5.Digital

""",'green','on_grey'))
x = int(input(colored("[+] Enter the number: ",'red','on_grey')))
if x == 1:
 custom_fig = Figlet(font= 'big')
elif x == 2:
     custom_fig = Figlet(font= 'block')
elif x == 3:
    custom_fig = Figlet(font= 'slant')
elif x == 4:
    custom_fig = Figlet(font= 'shadow')
elif x == 5:
    custom_fig = Figlet(font= 'digital')
else:
    print("No option Found")
user = input(colored("[+] Enter the name: ",'red','on_grey'))
user1 = input(colored("[+] Enter the color: ",'red','on_grey'))
print(colored(custom_fig.renderText(user),user1))
