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
   1.Banner3-D
   2.Banner4
   3.Banner
   4.Banner3
   5.Barbwire

""",'green','on_grey'))
x = int(input(colored("[+] Enter the number: ",'red','on_grey')))
if x == 1:
 custom_fig = Figlet(font= 'banner3-D')
elif x == 2:
     custom_fig = Figlet(font= 'banner4')
elif x == 3:
    custom_fig = Figlet(font= 'banner')
elif x == 4:
    custom_fig = Figlet(font= 'banner3')
elif x == 5:
    custom_fig = Figlet(font= 'barbwire')
else:
    print("No option Found")
user = input(colored("[+] Enter the name: ",'red','on_grey'))
user1 = input(colored("[+] Enter the color: ",'red','on_grey'))
print(colored(custom_fig.renderText(user),user1))