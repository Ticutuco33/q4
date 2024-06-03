print("❤️Welcome to Enzo's dating simulator❤️")

def choose_a_date():
    date = input("Choose a date: Kratos, Goku, Sonic, Dante, Master Chief, Gojo, Po, Gru, Senator Armstrong and Doom Guy? ")
    if date == "Kratos" or date == "kratos":
        kratos()
    elif date == "Goku" or date == "goku":
        goku()
    elif date == "Sonic" or date == "sonic":
        sonic()
    elif date == "Dante" or date == "dante":
        dante()
    elif date == "Master Chief" or date == "master chief":
        master_chief()
    elif date == "Gojo" or date == "gojo":
        gojo()
    elif date == "Po" or date == "po":
        po()
    elif date == "Gru" or date == "gru":
        gru()
    elif date == "Senator Armstrong" or date == "senator armstrong":
        senator_armstrong()
    elif date == "Doom Guy" or date == "doom guy":
        doom_guy()
    else:
        print("Please choose a available date.\n")
        choose_a_date()  
def kratos():
    print('''
                                                         :::                                        
                                                     -==-----===                                    
                                                   =====-----===-                                   
                                                   ==+=------==---                                  
                                                  =++++=-----==--=-                                 
                                                  =+*++=+====+---==                                 
                                                 *+++++=---=++=-==-=                                
                                                 *%#*####+==*#%#*++=                                
                                                  @#**##%#+-+***====                                
                                                  %%#*+==+=---=++*##                                
                                                  %%%%%***=-++=**%##                                
                                                  %@%%%#*#@#****##%#                                
                                                  %%%%%%#%*+*#####%#                                
                                             %%%@##@@%%%%%%#%%@*#%#*                                
                                          +==#%%%%%%@%%%%%####%%%#*                                 
                               ==+++++=++*+***#@%%#%@@@%%#####%%%*-:--=                             
                              *++*********#****%@%%%%@@@%%####%%*=---+++==                          
                             +####*#**#*******#*%@%%%%@@@%%%%%%*=--==++==-::                        
                            =+*+##*##*#**+*+*++**%@@%%%@@@%%%%*----=====-:::::::                    
                          ==*#%*+#***###%***++=*#+*#%@%#%@@%#=--:-=+++==--::::::-                   
                        ++#%%%@@#%%#*%##%##%#*++*+*##**###+==--:--==++=-:-::::::==                  
                         *%###%@%#%###+%#####%#+%%****#++#*----:-==+++=-::::::::=+-                 
                          ##%%@%@%####+*+**%#%@%##**+++++%#+=---======-::::-----=+-                 
                         #%@%%%%%@@@@@@@@@@%##**+*+++====+===+*#**+++=-::::--=--=*=-                
                         %@@@@@@@%%%@@@%@@@@@@@%***+*++++++======+*##*+=-:--=+==+#*=                
                        #%@@@@@@%@@@%@@%%%%%%##****###***+++++++++*+++*####=+#*+*##+                
                        #%@@@@@@@@@@@@@@%%@@@@@%%%#***#%%%###*+****++*##*#%%%%#**##*+               
                         *%@@@@@@@@@@@@@@@@%%%%%%%%#%%%#+*%%%%%%#%%###%###*%@%*+==++*               
                        **#%%@@%%%@@@@@%%%%%%%%##**++++++*%%%%%%%%%%%%%%#++=%#=-------              
                       +***###%%%%%%@@%%%%%%%%%%%%%%%%##***###*#%%%@@@@@@@@%%*==------              
                       +**+*+++*##%#*#@%%%#%%#####*+==-:--=+**+++*#%@@@%%@@@%*++==-====             
                      ==++*+++++*##* +@%%%#####++++====-----===+=-=*%%%%%@@%#%**+======-            
                    ======***+**##*  *@@%%##*+++=--==++*+++======+*#%%%%@@@@#%%**++++=---           
                    +++=--+######     %@%%###*+====--------=====---=+*#%%@@% %%%%###+---==          
                   ++++====#%%%+      #%%%%%######**++++=+++=+===+++*%%%%@%   %%%%%**+******        
                  ##*++==++++**        %%***%%###**###%%#**+++***##**+#%@@%%* %#***#%#*+###*        
    #%##          %%%%%#*++++**        %%%@@@####**++=====++++=====+++##%@%%%#%%@%##****#####       
  #%%@%###       %%%%#****##*+         @@@%%%%@%@%%%#*+=++****+**###%%%%%%%@# #%%#**#**+*#%%%       
  #%@%@%##**     #%%##****#***        %%@%%%**@%%%@@%%%%%**++#%@%%%%%##%%%@%#  #%###**++++%%#       
   %%%@%%%###*   %%%##***####*   ##*  #%+*%@@%%@%%%%@%%#%++**%%#*#%%%%%%%@@%*   *@%#*##%#*###       
     #%@@@%%#####%%%%%##**#*    %%@@*#@%#*+*@%%@@@@@@@@%%%%%%@#+*#%%%%%%%###%    *@%%#%%##+==       
       #%@@%%%%%#%#%##%#***=    %@@@*%@@@%%*+*%@@@@@@%%@@%%%%%@@%##**##%###%%     %%%###**##*=      
          %@@@@@%%###%%%#%#     #%@@@@##@@%@@#+=+###%@@**#%##@%###*+=+**#@%%*      %%#**##%%%+      
            %@@@@%%##***##       @@@@%@%#%%#@@%##**+=+***=+**++=+++**##@%#%%%      *%@@%%**####     
             #@@%###****#        #%@@%#%@@@%%%%**+%%##*+++++**#####%@@%###%#%+==     %%%#*+*###     
              %%%%#%%##**         #@@@@%#%@@%@%%%##%#%####**###%@%##**##*#%%%#+*+    *%%%#***##     
               %%%##*++++          #@@@@%%%%%@@@%@%%%%%@@@@%%#****###****#%@%%#**=    #%#***###*    
               %%%%%##*##          #@@@%#%@%##*%%%@@%%%#%##*##############%%%@%%#     #***####%%    
               %%%%##*++++=        %@@@%*#%%#*##%%##@@@@%#*##****##%##%#####%%%%%*   #%*+*#%##%%*   
               ##########**=       #@@@@%*#@%#**#%@@@%#####+****##%%#%%######%%%%#   ***#%%##%%%#   
               #%#%***+*%%#**       @@%@%#*#@%###%@@%******#**###%###%########***#*  *##%%%###%%%   
               #%###**#%%%%##      #@@@@%%#*%@@%%%@@%########*##%%##%##%#####%%%%%# +++##%%%##%#    
                *#%%########*      %%%@%%%%##%%%%@@@@########%##%####%%%%#####%%%#   #*  #%%#%*     
                   *##%@%#%%#     #@@%%%%%%##%%%%@%@%%%######%%######%%%%#%#####*       #%%##*      
                     #%%@%##%#    %%@%%%%%%%%%%%%%%@%%%%###%%%%%###%%%%%@%@##%%#        *##%#       
                        #@%##%#   #%%%%@@@%%%%@%%%@%%%%%%%%%%%%%%#%#%%%%@@@@##%%       #####        
                         #@%###%+ #%@#@@@%%%#%%%%@@@%%%%%%%%%%%%%%#%%%%%@@@@%%%%         #          
                          %%%%####@%@%@@@%%%#%%%%@@@@%%%%%%%@%%%%#%@%%%%@@@@@%@@                    
                           #%@%###%@@@@@@%#%%%@@%@@@%%#%%%%@%%#%%%@@%%%%@@@@@@@@                    
                             %@@%##%@@@@%%%#@%@@@%%@@%%%%%%#%@@@%@@@%%#%@@@@@@@%%                   
                              #@@%###%@@@@@@@%%@%%@@@@@%%@%%%@@%%@@@%@%@@@@@@@@@%                   
                                %@@%##%%@@@@@#%@%%%%@@@@%%%%%%%%#@@@@@@@@@@@@@@@%                   
                                 %@%%%###%@@@%%%@%#%@@@%%%%%%%%%@@@@@@@@@%%@@@@@%                   
                                %%@@@%%%###%@@@%%%%%%@@%%%#%#*%@@@@@@@@@@@@@@@@@@#                  
                                 %@@@@@%###*#@@@%%%%%@@%%%%%**+@@@@@@@@@@@@@@@@@@#                  
                                %%@@@@@%%###*#%@@ %%%@@%%##*   %@@@@@@@@@@@@@@@@%                   
                                %@@@%%@@%%#****#%  %%%%#**      %@@@@@@@@@@@%%%%%                   
                                %%@@@@@@%%#%*#*+*#  %%%%#**+=    #@@@@@@@%%@@%%%@#                  
                                %@@@%%#%%@%%%##*++*%  %%%###+=    %@@@@@@@@@%%%%%%                  
                              # %@%%%%%%%%%@+@#*#++*# %%####*=-   +@@@@@@@@@@%%@@%                  
                              ##%%%%%%%###%@@%%#**+*#%%#%%%%#*+    %@@@@@@@@@@@@@%#                 
                             ###@%%%%%%%%%%@@@%#****###%%%%#*      %@@@@@@@@@@@@@@#                 
                              ##%%%#%%%%%%%@@%**+=**+###%%#        @@@@@@@@@@@@@@%*                 
                              ##%%%%#%%%%@@@@# %#*###+++%%        #@@@@@@@@@@@@@@%                  
                             ##*%%%%%%%@@@@@@#%%@@%%#++**%        *@@@@@@@@@@@@@@#                  
                             #%#*%%%%####%%#%%%%%%#%##*#%#         @@@@@@@@@@@@@@%                  
                             #%#*%%%%##%#%%#%%###%%@#%%%#          @@@%%%%%@%@@@@%                  
                             *###%%%%##%%%%%#%##*%#                @@@@@@@@@@%%@@%                  
                             #@@##%%%%%#%%%%######                 @@@@@@@@@@@@@@@#                 
                             %@@%#%%%###%%#%###%                   *@@@@@@@@@@@@@%                  
                             #@@@%#%%%%%%%###%+                    #@@@@@@@@@@@@@%                  
                             %@%%%##%%%%%%%##                       @@@@@@@@@@@@@%                  
                             %%@%%%%##%@%%%*                        #@@@@@@@@@@%@#                  
                             #@%@%%@%#%@@@#                          @@@@@@@@@@@@#                  
                             %@@%%@@%%%%@@@                          %@@@@@%%%%@@#                  
                             #@@%@@@@@%%@%#                          %%@@@@@@@@@%                   
                              @@@%%%@@@@@%                            %@@@@@@%%@%                   
                              %@%%%%@@@@%#                           #@@@@@@@@@%%                   
                              %@%%%%@@@@%%                           %@@@@@@@@@%%*                  
                              %@%%%@@@@@%%                          #@@@@@@@@@%%%#                  
                             #%@%%%%%@@%%%                          %@@@@@@@%%%%%%#                 
                            #%@%%%%%%@%%%%                          *%%%%%%%%%%%@@%#*               
                            #%@%%%%@@@%%%##                          @%%%%@@@@@@@@@%%%#             
                            #@@%%%%@@@@@@%                           %@%@@@@@@@@@@@@@%@%%*          
                           *@@%@%%%@@@@@%#                            %@@@@@@@@@@@@@%%@%@@%#        
                           %@@@@%%%%@@@%%                               #%@@@@@@%%%%%%%%%%%@%       
                          %@@@@%%%@@@@@%                                    *%%@@@@@@@@@@@@@%       
                         %@@@@@@%@@@@@@*                                       +#%@@@@@@%#*         
                         %@@@@@@%@@@@@@                                                             
                          #%@@@@@@@@%#                                                              
          ''')
    print("I am the God of War!!! What do you want with me human?")
    kratos_choise1 = input("1. I want to go kill gods with you.\n2. I came here to kill you!!\nMake your choice: ")
    if kratos_choise1 == "1":
        kratos1()
    elif kratos_choise1 == "2":
        deathk()
    else:
        print("Invalid input, Boy!\n")
        kratos()
def kratos1():
    print("I see human, but do you have the strength to fight alongside the God of War?")
    kratos_choise2 = input("1. Tell him that you are stronger than him.\n2. Tell him that you are not that strong but you have the power of revenge.\nMake your Choice: ")
    if kratos_choise2 == "1":
        deathk2()
    elif kratos_choise2 == "2":
        kratos2()
    else:
        print("Invalid input, Boy!\n")
        kratos1()
def deathk():
    print("You dare to challenge the God of War? Prepare for battle!\nHe completely oblitarated you, womp womp.")
    try_againk = input("Do you want to try again? ")
    if try_againk == "yes":
        kratos()
    elif try_againk == "no":
        choose_a_date()
    else:
        print("Invalid input, Boy!\n")
        deathk()
def deathk2():
    print("He punches you to test your strength, since you're weak he kills you.")
    try_againk = input("Do you want to try again? ")
    if try_againk == "yes":
        kratos()
    elif try_againk == "no":
        choose_a_date()
    else:
        print("Invalid input, Boy!\n")
        deathk2()
def kratos2():
    print("I like your spirit human, I will train you and together we will have our REVENGE!!!\nKratos trains you for a year and now you have become much stronger. Kratos asks which god do you want to take down first?")
    kratos_choise3 = input("1. Hermes\n2. Aphrodite\nMake your choise: ")
    if kratos_choise3 == "1":
        kratos3()
    elif kratos_choise3 == "2":
        death_aphrodite()
    else:
        print("Invalid input, Boy!\n")
        kratos2()
def death_aphrodite():
    print("Kratos agreed but was not so sure. When you went to fight her you succumbed to her and your desires.\nYour now her slave.")
    try_againk = input("Do you want to try again? ")
    if try_againk == "yes":
        kratos()
    elif try_againk == "no":
        choose_a_date()
    else:
        print("Invalid input, Boy!\n")
        death_aphrodite()
def kratos3():
    print("Good choice, he can run fast but that is everything he does. You and Kratos fought together and killed Hermes pretty easily.\nKratos then asks you, who is next?")
    kratos_choise4 = input("1. We should fight Poseidon. \n2. We should fight Hades.\nMake your choice: ")
    if kratos_choise4 == "1":
        kratos4()
    elif kratos_choise4 == "2":
        kratos4_1()
    else:
        print("Invalid input, Boy!\n")
        kratos3()
def kratos4():
    print("Great choise Poseidon is strong but together he will be a piece of cake. You and Kratos defeat Poseidon pretty easily. You guys keep defeating more and more gods, until the only god left is Zeus, the god of the gods. Zeus knows that you guys together are too strong so he calls his father Cronos to help him. Kratos wants to fullfill his revenge by killing his father.")
    kratos_choise5 = input("Do you fight Zeus or Cronos?\n1. Zeus\n2. Cronos\nMake your choice: ")
    if kratos_choise5 == "1":
        deathk3()
    elif kratos_choise5 == "2":
        kratos_win()
    else:
        print("Invalid input, Boy!\n")
        kratos4()
def deathk3():
    print("Kratos wants his revenge, he wants to kill his father with his own hands, so he stabs you in the back and you die.")
    try_againk = input("Do you want to try again? ")
    if try_againk == "yes":
        kratos()
    elif try_againk == "no":
        choose_a_date()
    else:
        print("Invalid input, Boy!\n")
        deathk3()
def kratos_win():
    print("You go and take on Cronos, he is strong but you will being filled by anger and revenge you manege to kill Cronos with averege difficulty. Kratos defeats Zeus, both of you and Kratos got their revenge.\nThe End!!!")
    the_end = input("Do you want to go back to the menu? ")
    if the_end == "yes":
        choose_a_date()
    elif the_end == "no":
        print("Bye Bye 🤫🧏‍!!!")
    else:
        print("Invalid input, Boy!\n")
        kratos_win()
def kratos4_1():
    print("Hades will be hard but we can do it. You and Kratos fight Hades it was a hard battle, you guys won but you came of injured. You two keep defeating all the other gods with averege difficulty, until the only god left is Zeus, the god of the gods. Zeus knows that you guys together are too strong so he calls his father Cronos to help him. Kratos wants to full fill his revenge by killing his father.")
    kratos_choise51 = input("Do you fight Zeus or Cronos?\n1. Zeus\n2. Cronos\nMake your choice: ")
    if kratos_choise51 == "1":
        deathk3()
    elif kratos_choise51 == "2":
        kratos_win_death()
    else:
        print("invalid input, Boy!\n")
        kratos4_1()
def kratos_win_death():
    print("You go and take on Cronos, but you are still injured from the fight with Hades. The battle is hard and both you and Cronos are in the verge of the death, but with you wanting to fullfill your revenge, you use your last bit of strengh to kill Cronos. Kratos comes to you and say: You fought well my brother, now you may rest. After you he finishes talking you close your eyes and die.\nThe End!!!")
    the_endk2 = input("Do you want to go back to the menu or try again? ")
    if the_endk2 == "menu":
        choose_a_date()
    elif the_endk2 == "try again":
        kratos()
    else:
        print("Invalid input, Boy!\n")
        kratos_win_death()
def goku():
    print('''
                                            @%                                                      
                                   @@    @%%%                                                       
                                  @@   @%%##                                                        
                                  @@  @%%##@    @@@@@@@@@@@                                         
                                  @  @%%%*%  @%%%%%%%%%%@ @@@                                       
                                  @@ @%%%%@@%%%%%%#*%@@@@           %+#                             
                                   @@%%%%%%%%%%%%*@@@%%@         %++:-%                             
                                   @@%%%%%%%%%%%%#######***%   %=-+=#%                              
                                @%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@+::-++#                              
                     @@@@@@@@  %%%%%#%%%*#%%%%%%%%%%%%%%%@@@   ***#+-*  *:%                         
                      @@@%%%%%%%%%%+#%###%#*%%#%%%%%%%@@      %-:=-==-+*+=+                         
                 @@@@@    @@%%%%%%##%*+%%+::=%%%%%%%@@  @      +++=*-::=-#@                         
                  @@%%%%%%%%%%%%%%%%++##%=-:-#%%%%%%%%%%@     @#===+::::*                           
                    @@%%%%%%%%%%+#%%:.-.:%=:+#%%%%%%%@@   @%##%%+===+-=#@                           
                        @@%%%%%%#*-::::-:.::-:+%%%%@@   @%##%%%%*##*==:.:.:+*#                      
                    @@%%%%%%%%%%+#+:..::=-++-:%%@@@%*==+*%%%%%%@@@+-::-:::--+:-@                    
                           @@%%%%%*+:.::*#%#:-%=::=--:::-%%%%%%@@@#==----=+@ #++                    
                         @%@@%%%@%=+#-::+*+#=:.-+=::::::::#@%@@@@@@%*=:=:..:#%+=                    
                       %#%#*#%%@@%*+*++==+*::-+-::::..::::+*@@@#@@@@@++-+=-*-*--@                   
                      %##*%+::-+=-:.::-==:-=++:...::::::=#%@@%==+%@@@%=#++=+=+%@                    
                      #@#%+-==#:.........:::::::....::=#+...:+=+++**++= #+%*@                       
                     @%%%%*+-=:....::::::::==-:=---=+%#::.::++=++**++++                             
                     @%@@#--=+::::=*-:::--==+*++*#%**@*---==*++*+++++-%                             
                     @#@@%++**+***++++++++*+=*%%@%%##@#+*##*++**+++*=%                              
                      %#@%*+========+*#%%%%%%%%%%%%*#%#++++***+++**#                                
                       @%@@%##*#%%%##*#%%%%%%%%%%%%+*%#++***###@@@                                  
                         %@@@@@@%#%*#*+%%%%%##%%%%#++#%@@@@                                         
                         @#*#%%####**#*+%####%%%%%=+++#@                                            
                         %%#******#***#*+%%%%%%@%=++=**#@                                           
                         @*##*****#+++***=#%%%%%=+###***%                                           
                          @*##*****++++***=+%%@+*=+##-#*%                                           
                          @*+*#****+++*#+**+++++=#*+*-#%%                                           
                           #++**#*+++++*#+*#*++*##++*##%@      @@%%@@                               
                           @#*+**#**+++*##**###%#%%%%%%@@   @%%%%%%@                                
                             @#***%#***##%%%%%%%%%%%%%%%@ @%%%%%@%%@@@                              
                                @%@%%%%%%%%%%%%%@%%@%**+#%%%@%%@                                    
                               @%#%%%%%%%%%%%%%@%%%%@@@%%%+*==++++*##%%%                            
                          @%+==*+++*+*%*#%%%%%#%%#####*++*++#*+++++++====++%@                       
                  @@#*+=+=++++*+++**++*+##%#%##%%#*#++++**#*+++++++++++++=====++%@                  
            @%*+======+*#*****+++*+++=++##%%%*#%%#***+++*#*+++++*++++++++++++=====+%@               
         %*+====++++++=====+**#**++**++++%##%##%%%*#+++##*+++***+++++++**+++++++++==*%              
       %+===+++====+++++++++++==+***++**++#%##%%%%%@@@%#*++***+++++++**%*+*++++++++++*%             
     @*+++==++%*+++===++++++++++++++++++******#%%%%%%%%%#***+++++++*#*##*+*+++++++++**%@            
    %+*#**+=++*%#++*++++++++++++++++**********#%%##*#%%%#++*+++++**%#*##+==#++++++++**#%@           
  @%+*##***==*+###*+**++++***+++==+++++*******#%%###**#+*#*+++****#%***%+==**++++++***##%           
  %+*##****+=+***###****+++++***##*++===++**###%###***###*+*******###***+===#*++++******%           
  #+*%#*****+++#**#%%********++****###%##*****#%%###%##************%##*+++===+#********#%           
  #++###*****++**#%##%#***************####%%%%@@@@@ @%%#############%*+*+++====+#******#%@          
  %+++##******++***###%%%%%%%%%%%%%%%%%%@                @@@@@     %#**++++++**+=+#***##%%@         
  %+*+*%#***********#%##@                                          @%*#++++++++****+#####%#%        
  @#**+*##***********#%%                                            @#*+++++++++***#**#@*%##%       
  %%+#*+**#**********#%                                              @#+++*++++++****###*%##%       
  %#**#*************###@                                             @*+******++++****#**##%@       
  @##**%********##**###@                                              #*******##******#*#%%         
   %#%*##******###*###%                                                @#**#***##%###%%%%@          
    %%%*#%***#%######@                                                   %%%%%%%%%###%%##%          
       %#%%%%%%%%%%%%@                                                     @@@%%%%%%%%%%##@         
       @%@@%%%%%@@@@@                                                       @@%%%%%%%%%%##@         
       @%@%%%%%%%@@@                                                         @%%%%%%%%%%%%%         
       @%@%%%%%%%%%@                                                          @%%%%%%%%%%#%         
        @%%%%%%%%%@@                                                           @%%%%%%%%%%%         
     @%%@#%@@@@@%%%                                                             @%%%%%%%###%%%      
     @%%%%%%%%%%%%##                                                            @@%%%#%%%%#%@@      
 @%%##%%%%%%%%%%%%%%                                                            @%%%%%%%%%%%%%@     
%%%%%%%%%%%%%%%%%%%@                                                            @%%%%%%%%%%######%%%
#=+*########*#%@@@                                                              @%%%%%%%%%%%%%%%%%%%
                                                                                 @@@@@%##******+==*%
          ''')
    print("Hey, I am Goku, are you strong?")
    goku_choise1 = input("1. No but I came to meet you so I can became stronger.\n2. Yes I am.\nMake your choice: ")
    if goku_choise1 == "1":
        goku1()
    elif goku_choise1 == "2":
        deathg()
    else:
        print("Invalid input, Saiyan!\n")
        goku()
def goku1():
    print("I like your spirit, warrior. I will train you so I can have someone strong to fight. Goku trains you, you became much stronger and gain new abilities like the ability to fly, ki control, kamehameha, spirit bomb, instant transmission and many other abilities. One day on the last the day of training, Freeza appers and starts attacking Goku, Do you help him?")
    goku_choise2 = input("1. Yes\n2. No and run away.\nMake your choice: ")
    if goku_choise2 == "1":
        goku2()
    elif goku_choise2 == "2":
        deathg2()
    else:
        print("Invalid input, Saiyan!\n")
        goku1()
def goku2():
    print("You chose to stay and help Goku in the fight agaist Freeza. You wanna join the fight with a attack. Which attack do you use?")
    move = input("1. kamehameha.\n2. fly in and try to punch him.\n3. Make a spirit bomb.\nMake your choice: ")
    if move == "1":
        goku3_1()
    elif move == "2":
        deathg3()
    elif move == "3":
        goku3_2()
    else:
        print("Invalid input, Saiyan!\n")
        goku2()
def goku3_1():
    print("You shoot a kamehameha at Freeza and it hit him, he took a lot of damage. What do you do now?")
    move2 = input("1. fly in to hit him.\n2. shoot another kamehameha.")
    if move2 == "1":
        goku4_1()
    elif move2 == "2":
        deathg4()
    else:
        print("Invalid input, Saiyan!\n")
        goku3_1()
def goku4_1():
    print("")
def goku3_2():
    print("You start charging the spirit bomb, Goku notices you charging the spirit bomb so he keeps Freeza ocupied. Your spirit bomb is fully charged, you throw it at Freeza, Goku makes sure that it hits Freeza by throwing him at the bomb. Freeza gets hit and his body gets evaporated. 10 years have passed since the fight with Freeza, you and Goku have went on many adventures and got a lot stronger. Goku wants to fight you. Do you fight him?")
    goku_choice3 = input("1. Fight Goku using 100% of your power.\n2. Fight Goku using 50% of your power.\nMake your choice: ")
    if goku_choice3 == "1":
        goku5()
    elif goku_choice3 == "2":
        deathg5()
    else:
        print("Invalid input, Saiyan!\n")
        goku3_2()
def goku5():
    print("You and Goku fight seriously, using your full power, it was a even match up no one was stronger than the other, both you and Goku had a lot of fun. THE END.")
    the_end = input("Do you want to go back to the menu? ")
    if the_end == "yes":
        choose_a_date()
    elif the_end == "no":
        print("Bye Bye 🤫🧏‍!!!")
    else:
        print("Invalid input, Saiyan!\n")
        goku5()
def deathg():
    print("You and Goku fight but since Goku is much stronger than you, you DIE.")
    try_againg = input("Do you want to try again? ")
    if try_againg == "yes":
        goku()
    elif try_againg == "no":
        choose_a_date()
    else:
        print("Invalid input, Saiyan!\n")
        deathg()
def deathg2():
    print("Freeza killed Goku while you were running away, but Freeza manege to catch up to you and he killed you. You are DEAD.")
    try_againg = input("Do you want to try again? ")
    if try_againg == "yes":
        goku()
    elif try_againg == "no":
        choose_a_date()
    else:
        print("Invalid input, Saiyan!\n")
        deathg2()
def deathg3():
    print("Freeza noticed you flying in, so he shoot a lazer beam at you. The lazer beam hit your heart and you DIED.")
    try_againg = input("Do you want to try again? ")
    if try_againg == "yes":
        goku()
    elif try_againg == "no":
        choose_a_date()
    else:
        print("Invalid input, Saiyan!\n")
        deathg3()
def deathg4():
    print("Freeza sees you charging another kamehameha, so he teleports behind you and stabs you in the heart with his tail. You DIED.")
    try_againg = input("Do you want to try again? ")
    if try_againg == "yes":
        goku()
    elif try_againg == "no":
        choose_a_date()
    else:
        print("Invalid input, Saiyan!\n")
        deathg4()
def deathg5():
    print("You and Goku went on many adventures, fought enemis together many times and he was your teacher. Goku didn't like how you disripected him by not using 100% of your power in the fight after all the things you guys went through, so he KILLS you.")
    try_againg = input("Do you want to try again? ")
    if try_againg == "yes":
        goku()
    elif try_againg == "no":
        choose_a_date()
    else:
        print("Invalid input, Saiyan!\n")
        deathg5()
def sonic():
    print('''
                                                                                                    
                                                         ##%%#                                      
                                         =+++*********+##%++##                                      
                                     ==++******#######%#+===*%#                                     
                                  ===++*****#########%+=---=+##                                     
                                ==+++******#####**#%#=------=###                                    
           **++++++=+         ==++*+*****#########%*--------=#%#####                                
          %%%#####********+++++*******##############+:::::--=#%#########                            
           %%#+**########*********#*###################=-::-+%%#############                        
            %%*+++++*#######***############################*#%%%##############                      
             %%#==+++++*%%#**###############################%%%#################                    
              %%#+==+++*#***####################################%#################                  
               %%%*==+****###%%%%%%%%#############%%%%%%###########################                 
                 %%%##**####%%%%%%%%%%#####%%##%#=....=#%##############%%%####%%%####               
                  %%#*#####%%%%%%%%%######%%###-........+%#########%%%%%%%%%%%%%%%%%##              
                    *#%##%%%%%%%%%%%#####%%###.. ........*#######%%###%%%%%%%%%%%%%%%##             
                    #%%*=+#%%%%%%%%######%###..  ........:###########%%%%%%%%%%%%%%%%%#             
                    #%%==-=#%%%%%%%%%#######:. ..     ....%%#######%%%%%%%%%%%%%%%%%%%%#            
                    #%%==--=#%%%%%%%%######+...:+=.. .....###%%#%%%%%%%%%%%%%%%%%%%%%%%##           
                    *%%==----*%%%%%%%%#####=..:+**+......-%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%#           
                    =#%*-=----*%%%%%%%%#%%#:..-*%%#:.....*#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#           
                     +%#==----=#%%%%%%%%%%+...-*%%*=....-#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%           
                     -*%+==----*%%%%%%%%%#....:=.#+=...:*%%%%%%%%%%%%%%%%%%#  %%%%%%%%%%%%          
                      =#%===---+##%%%%%%*:.....=--=...:=+*%%%%%%%%%%%%%%%%%%#      %%%%%%%          
                      =+#%===---+=%%#=-::.......:-:::::::-=%%%%%%%%%%%%%%%%%%#         @%           
                       =*#%+==---=#@%%=-:::::::::::::-=---=#%%%%%%%%%%%%%%%%%%#                     
                       =+*#%*====--=*+-::::::::::::-:----=+%%%%%%%%%%%%%%%%%%%%#                    
                        +*+==--======-------------::---==+%%%%%%%%%%%%%%%%%%%%%%#                   
                        =+*=============----==-::--====+*%%%%%%%%%%%%%%%%%%%%%%%%                   
                         =*#=+++++=================+++#%%%@%%%%%%%%%%%%%%%%%%%%%%#                  
                          +#%%*+++++++++++++++++**##%@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%                 
                          +*#%%%%%#******###%%%@@@@@@@%%%%%%%@@@@@@@@%%%%%%%%%%%%%%                 
                           *#%%@@@@@@%##*****#%@@%%%%%%%%%%%%%%%@@@@@@@@%%%%%%%%%%%                 
                           +*%%@@@@%*======----#%%%%%%#*%%%%%%%%%%@@@@@@@@%%%%%%%%%%                
                            +#%@@@%==----::::::-%%%%%%+--=#% #%%%%%@@@@@@@@%%%%%%%%%                
                             *%%@%+=---:::::::::#%%%%%%*=---+  %%% #%%@@@@@@@%%%%%%%                
                              #%@#=----:::::::::=%%%%%%%%+--::-      #%%@@@@@@%%%%%%                
                              *#%*=----:::::::::=%%%%%%%%@%+-::::      #%%@@@@@%%%%%                
                               *#*==----::::::::#%%%%%%%%%@%#=-::::      %%%@@@@%%%%                
                                #*==----::::::::%%%%%%%%%%%@@%#+-::::      #%@@@@%%%                
                                =====----::::::+%%%%%%%%%%@@@@%%+=::::       #%@@%%                 
                              -=++===-----::::-#%%%%%%%#%%@@@@@%%*=-::::       %%%%                 
                         :- -===++*===-----:::+%%%%%%%#   %@@@@@@%*=-::--:...::                     
                       :----===++++====-------%@@%%%%#      @@@@@@%+=-::.......::                   
                    ::-------=++++  *+===---=%@@%%%%#          %@@%+-::::....::::                   
                    =++-:::---=+    #%%#***%@@@@%%%%             @@=--::::......::                  
                ::::---==::----=+   #%@@@@@@@@@@%%%%##             ----=======--:::                 
            .::::--::.::=-::--====  #%@@@@@@@@@@@%%%%               :-:::...::-+*=--                
          ::::::----...:-+---=====-  %@@@@@@% %%@@%%%%           ::::.........::==-                 
         :::...:::--:..:-=*=-===     #@@@@@@%  %@@@%%%%        .:..............:::                  
         :::..:::.:-::::--===-       #%@@@@@%  #%@@@%%%      ::....:::::.......::::                 
         :-::.....:-::::--            %@@@@@%   #@@@@%%#    :::..:::--::.......::::                 
         -=--:::::-=-::---            #@@@@@%#   %@@@%%%#   :-:::::..::........::::                 
         :=+=====-::----              #@@@@@@#   %%@@@%%%   ---:::..:::........:::::                
          ---:::::::-:-:              #%@@@@@%   #%@@@@%%%   -=-::::::...:::...:::::                
           -==-----:::-::              %@@@@@%#   #@@@@@%%    -=--::::.:--::::::::::                
            -===-::::-:::              #@@@@@%#    %@@@@@%#     =-==-----:::==::--::                
              =======---               %@@@@@@%    #%@@@@%%#     -====-:::-----=---                 
                                       %%@@@@@%#    %@@@@@%%       -===-=---==---                   
                                       #%@@@@@%#    %%@@@%%%#        -======----                    
                                       #%@@@@@%%     %@@@%%%#              -                        
                                        %@@@@@%%     #%@@@%%%#                                      
                                        %@@@@@@%      %@@@%%%%#                                     
                                        #%@@@@@%       %@@@%%%#                                     
                                     --=*%@@@@@%+==--  #%@@@%%%#                                    
                                  :---=+*%@@@@@%+===-- #%@@@%%%%                                    
                                 :---==+*##*=-------=-:=#@@@@%%%+===---::                           
                                 -----::::::---======--=*%@@@@@@%+=-::::::                          
                                   -======+++++++=====--::::::........::::                          
                                  :---=========++++==+++==--::::::::-----                           
                                  ---::-------=========++==---::::::::::::                          
                               ...:=+=--------======+==+++==---::::...::::                          
                           ...:::::--=#%#*+++++++*#%#*===----:::......::::                          
                        .----::::::::::%%%%%%%%%%%%%%#++===--:::::::-----                           
                    .=*#%%#+:::::::..::=%%%%%%%%%%%%%%%#***++***===----:...                         
                 -=#%%%%%%%#=::.......:-#%%%%%%%%%%%%%%%%%%%%+:::::::::::....                       
              =+#%%%%%%%%%%#+:.........:#####%%%%%%%%%%%%%%*-::::::::::::::....                     
           :+#%%%%%%%%#######-.........:+######%%%%%%%%%%%#-::::::::::---=++=--::                   
         :*%%%%%%%###########-..........+**###%%%%%%%%%%%%---::::::-+#%%%%%%%#**=-                  
        -#%%%%%%%%%%#########=..........+%%%%%%%%%%%%%%%%+---::::-*%%%%%%%%%%%##**+                 
       -*%%%%%%%%%%%%%%%#####+..........+%%%%%%%%%#%%%%%%=----::-#%%%%%%%########*##                
       -==+*#%%%%%%%%%%%%%%%%*:.......::+%%%%###***%%%%%*-----:-#%%%%%%%%#########*#%               
         +++=====+++**#######*======+++++++++++****+#%%%*------+%%%%%%%%%%###########%              
             ++++++++++++++++++++++++++++++++****#+++*#%+------*%%%%%%%%%%%%#######%#%              
                    +++++++++++++++++++            =+++++=----=#%%%%%%%%%%%%%######%%%%             
                                                     +++++++=-+%%%%%%%%%%%%%%%%##%%%%%%             
                                                        +++++++**##%%%%%%%%%%%%##**++++=            
                                                            +*++****++++++=====---======            
                                                                *****++++++++++****                 
          ''')
    print("Sup, I am Sonic, nice to meet, you do you want to race?")
    sonic_choice = input("1. Yes.\n2. No.\nMake your choice: ")
    if sonic_choice == "1":
        sonic2()
    elif sonic_choice == "2":
        deaths()
    else:
        print("Invalid input, Hedgehog!\n")
        sonic()
def sonic2():
    print("You agreed to race agaist Sonic, both of you and Sonic get in teleported to a magical track in another planet, you and Sonic get in the start line and in a running position. 3, 2, 1, GO!!! Both you and Sonic start running, you are in winning so far. The race goes on and you get to a intersection and you can't see where the roads take you. Which path do you take?")
    sonic_choice2 = input("1. Left.\n2. Middle.\n3. Right\nMake your choice: ")
    if sonic_choice2 == "1":
        deaths2()
    elif sonic_choice2 == "2":
        sonic3_1()
    elif sonic_choice2 == "3":
        sonic3_2()
    else:
        print("Invalid input, Hedgehog!\n")
        sonic2()
def sonic3_1():
    print("The middle path lead you to a new planet full of sand and cactus. You keep running, unsure if Sonic followed you. The sand slows you down a bit, but you see a small oasis ahead. Do you stop at the oasis?")
    sonic_choice3_1 = input("1. Stop at the oasis.\n2. Keep running.\nMake your choice: ")
    if sonic_choice3_1 == "1":
       sonic4_12()
    elif sonic_choice3_1 == "2":
       sonic4_11()
    else:
       print("Invalid input, Hedgehog!\n")
       sonic3_1()
def sonic4_12():
    print("You stop at the oasis and find a refreshing drink that boosts your energy. Feeling rejuvenated, you start running again with a burst of speed. You see another portal ahead. Do you enter the portal?")
    sonic_choice4_2 = input("1. Enter the portal.\n2. Don't enter the portal.\nMake your choice: ")
    if sonic_choice4_2 == "1":
        sonic5_2()
    elif sonic_choice4_2 == "2":
        loser_sonic()
    else:
        print("Invalid input, Hedgehog!\n")
        sonic4_12()
def sonic4_11():
    print("You decide to keep running through the sand. It's tough, but you manage to keep your lead. You see another portal ahead. Do you enter the portal?")
    sonic_choice5_1 = input("1. Enter the portal.\n2. Don't enter the portal.\nMake your choice: ")
    if sonic_choice5_1 == "1":
        sonic5_11()
    elif sonic_choice5_1 == "2":
        loser_sonic()
    else:
        print("Invalid input, Hedgehog!\n")
        sonic4_11()
def sonic5_11():
    print("You enter the portal and the portal leads you to a place where everything is black expect the track and at the end of the track there is the finish line. You look to your right and see that Sonic is right next to you. Both of you start speeding to the finish line, since you ran in the sand your feet hurts and your speed is not at max, so you are inches behind Sonic. You and Sonic are getting close to the finish, Sonic is in front of you by four inches, so for you to win you take a leap foward and you reach foward with your arm. You both cross the finish line but you guys don't know who crossed the line first so you guys check a perfecly placed TV that was connected to a camera on the finish line. Your anxious, the video is slowed down. The TV shows that you crossed the finish line before Sonic. YOU WIN!!!\nYou are so happy that you won agaist Sonic. That's your date.")
    the_end = input("Do you want to go back to the menu? ")
    if the_end == "yes":
        choose_a_date()
    elif the_end == "no":
        print("Bye Bye 🤫🧏‍!!!")
    else:
        print("Invalid input, Hedgehog!\n")
        sonic5_11()
def sonic3_2():
    print("The right path took you to a planet full of mushrooms. You keep running not knowing with Sonic followed you or not. You look at the mushrooms and thinks that maybe you could use them to your adventage. What do you do with the mushrooms?")
    sonic_choice3_2 = input("1. Eat a mushroom.\n2. Jump on top of the mushrooms.\nMake your choice: ")
    if sonic_choice3_2 == "1":
        deaths3_2()
    elif sonic_choice3_2 == "2":
        sonic4_2()
    else:
        print("Invalid input, Hedgehog!")
        sonic3_2()
def sonic4_2():
    print("You jumped on top of the mushrooms which gave you a speed boost and you started zooming acroos the track. After a while you reach a portal. Do you enter the portal?")
    sonic_choice4_2 = input("1. Enter the portal.\n2. Don't enter the portal.\nMake your choice: ")
    if sonic_choice4_2 == "1":
        sonic5_2()
    elif sonic_choice4_2 == "2":
        loser_sonic()
    else:
        print("Invalid input, Hedgehog!\n")
        sonic4_2()
def sonic5_2():
    print("You enter the portal and the portal leads you to a place where everything is black expect the track and at the end of the track there is the finish line. You start runnig to the finish line. You are halfway to the finish line, when Sonic passes through the same portal you came from. Since you were already halfway you reach the finish line first and YOU WIN!!!\nYou are so happy that you won agaist Sonic. That's your date.")
    the_end = input("Do you want to go back to the menu? ")
    if the_end == "yes":
        choose_a_date()
    elif the_end == "no":
        print("Bye Bye 🤫🧏‍!!!")
    else:
        print("Invalid input, Hedgehog!\n")
        sonic5_2()
def loser_sonic():
    print("You didn't enter the portal, so Sonic runs past you and wins the race. YOU LOSE!!!")
    try_agains = input("Do you want to try again? ")
    if try_agains == "yes":
        sonic()
    elif try_agains == "no":
        choose_a_date()
    else:
        print("Invalid input, Hedgehog!\n")
        loser_sonic()
def deaths():
    print("Sonic didn't like you not racing with him, so he run away and you lost your date. GAME OVER!!")
    try_agains = input("Do you want to try again? ")
    if try_agains == "yes":
        sonic()
    elif try_agains == "no":
        choose_a_date()
    else:
        print("Invalid input, Hedgehog!\n")
        deaths()
def deaths2():
    print("You choose the wrong path, it lead you into a black whole, who sucked you in and you DIED!!")
    try_agains = input("Do you want to try again? ")
    if try_agains == "yes":
        sonic()
    elif try_agains == "no":
        choose_a_date()
    else:
        print("Invalid input, Hedgehog!\n")
        deaths2()
def deaths3_2():
    print("The mushroom is poisonous and you DIE.")
    try_agains = input("Do you want to try again? ")
    if try_agains == "yes":
        sonic()
    elif try_agains == "no":
        choose_a_date()
    else:
        print("Invalid input, Hedgehog!\n")
        deaths3_2()
def dante():
    print('''
                                                                                                              
                                 %%%@                                                               
                              %@%@%@                                                                
                               @@@%%%               +                                               
                             *%@@@@@%         -=========+                                           
                            #%%%%%%%%        -::--:::--==+#                                         
                           #%%%%@%@%#%@@    -::::::::---==++                                        
                              %@@@@@%#@@@@@@:......:::-===+%@                                       
                                  @@@#%@@@@@=::.::::--=+++*#@@% %%                                  
                                   %@%#%@%@@+-::-:-===+#%#*#@@@@@@%%                                
                                   %%%%%@@@@#-=---++-::**#*%@@@@@@@@@%%                             
                                    %@@@%   @+-===::::.-%*+@@@@@@@@@@%#%%                           
                                     %@%%@%%%%*+*+=--::=+*#@@@@@@@@@@%%#%%#                         
                                  @  @%##%%%%%%###*++-+##+@@@@@@@@@@@%%#%%%%#                       
                                   @@@%@@@%%%#%%#%%###++#@@%%@  @@@@@@%%#%%%#*#*                    
                                    %#####%%%%#%%##%%#%%@@@@@@    @@@@@%%%%%%%%***                  
                                   %%%%%%*::::-+%%%%%%%@@@@@%%@@@@@@@@@@@@%%#%%%#%*                 
                                  %%%%%=......:###+==##%%##*=*@@@@@@@@@@@@%#%%%%%%%#                
                                  %%%##=:::..:#*##+*#%##+*#*+#@%@@@@@@@@%@@%%%%%%%%%%               
                                  %%%%%*-::::*+#%=-##%#***+#+@@#%@@@@@%@%@%%@%%%%@%@                
                                  %%@@%@+==+*%#+#.-=%*+*%#==#%@@%%@@@@@@@@%@%%%@@@                  
                                   @@@@@@%%#+--.+..=#*+##+==+#%@@%%@@@@@@@@@@@                      
                                   @#@@@@@@::.=::=:+**+%*=#%-*%%@@%@@                               
                                  @@@%@@@@%-.=.=:+*+*+#**+@@@@@@@@@%%                               
                                   @@@%%%#%%%###%*+*=++=-@@@@@@@@@@@%%                              
                                      @%%%%%%@@@#+*=-=--%@@@@%%%@@@@@%*                             
                                      @%%**%%%%*+===@#=*@@%%%#%%@@@@@@%#                            
                                       @%%%%%%#=++==-+@@@@%@%*#%@@@@@@@*                            
                                        %%%#%%*==++*%%@@@@%@%*#%@@@@@@@%                            
                                        @%%%%%%%*#%%%%@@@@%@%***%@@@@@@%                            
                                         %%%%%%%%%%%%%%%@%%%%+*+*@@@@@@%*                           
                                         @%%#%%%%%%%%%%%##%%#*#**#@@@@@@#                           
                                          %%%%%%#%%%%%%%%#%%#%##+++%@@@@#                           
                                           %%%%%%%%%%%%%##%##%%#**+=#%@@@                           
                                           %%%%%%%%%%%%%####%@%%##*=+#%@%%                          
                                           %%#%%%#%%#%%#####%@@%%%#+*#@@@%%                         
                                            %#%%%%##%%%##*##@@@@@%%%@@@@@@%                         
                                           @%%%#%###%%%#***%@@@@@@@@@%%%%%%@                        
                                           %%%%%##%#%%%####@@@@%@%@@@*%%%%%@                        
                                           %%####%#*#%%###%@@@%#%@%%@++*#@%@#                       
                                           @%###%%%%*@%##*@@@@@@%%%@*#%#*+*#%                       
                                           @%#%%%%%%@@%##%@@@@@%%%%%%%@@%%%@@%                      
                                        =@@@@@@%%%%@@@%#*@@@@@@%%%#%%%%%@%@@@@@                     
                                      @-:%%%##%%%%@@@%##@@@@@@%%%%%%%%%%%%%%%@@                     
                                   @%-:*@#@%#%%%%@@@%%%@@@@@@%%%%%%@@%%#%%%%%@@                     
                                @@@%%%*+%%%@%%%@@@@@@@@@@@@@%%%%%@@@@@@%%%%%%%@@                    
                             @@%%#*%@@@+=*@%%@@@@@@@@@@@@@%###%@@@@@@@@@@@@%%@@@                    
                        @@%%%%%###@@@@@@%+*@%@@@@%@@@%#####%%%%@@@@@@@@@@@@@@@@@                    
               @@@%%%%%%%%%%%%%%@@@@@@@@%%%@@@@@@%@%+**#%##%@@@@@@@@@@@@@@@@@@@@@                   
          @@@%%%%%%%%%%%%%%%@@@@@@@@@@@@%%%%@@@%%@%=+*##%%%@@@@@@@@@@@@@@@@@@@@@@                   
        @@@%@@@%%%%%%%%%%@@@@@@@@@@%@%%%%%%%%%%#@%*#####%@@@@@@@@@@@@@@%@@@@@@@@@                   
       %@@%%%%%%@@%%%%@@@@@@@@@@@%%@%%%%%%%%%#%@%#**###%@@@@@@@@@@@@@@@@@@@@@@@@@                   
       %%%%%%%%%%%@@@@@@@@@@@@@%%%@@@%%%%%%#*%@#***###%@@@@@@@@@@@@@@@@%%@@@@@@@@                   
       ##%%%%%%%@@@@@@@@@@@@@%%%%%@%%%%%%%%*@@*######%%@@@@@@@@@@@@@@@@@@@@@@@@@@%                  
      ##%%@@%%    @@@@@@@@%%@%%%%@%%%%%%%#%@%*######%%@@@@@@@@@@@@@@@@@@@@@@@@@@@%                  
      %%@%%%        @@@%#%@%%%%%%%%%%%%%%@@#*#######%@@@@@@@@@@@@  @@@@@@@@@@@@%@@                  
     @@@%@          @%#@@@@%%%%%%%%%%#%%@%##*###%##%@@@@@@@@@@@@@   @@@@@@@@%%@@@@                  
     @%@          @#%@@@@%%%%%%%%%%#%%@@#**######%%@@@@@@@@@@@@@    @@@@@@@@@@@@@@                  
    %@         @@#%@@@@%%%%%%%%%%%%%@@@#*#######%%@@@@@@@@@@@@@     @@@@@@@@@@@@@@                  
             @@%%@@@@@%@@%%%%%%%%%@@@@%###*###%%%@@@@@@@@@@@@@      @@@@@@@@@@@@@@@                 
           @@%@@@@@@@@@%%%%#%%%@@@@@@%%#####%%%%@@@@@@@@@@@@@       @@%@@@@@@@@@@@%                 
         @@%@@@@@@@@@@%%%#%%%%@@@@@%%%%%###%%@@@@@@@@@@@@@@@@       @@@@%%%@@@@@@@@                 
       @@%@@@@@@@@@@@%%%%%%@@@@@@@%%%%%%%%%%%@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@%                 
      @@@@@@@@@@@@@@%%%%%@@@@@@@%%#%%%%%%%%@@@@@@@@@@@@@@@@         @@@@@@@@@@@@@@@                 
    @@@@@@@@@@@@@@%%@%%@@@@@@@@@@%%%%%%%%%@@@@  @@@@@@@@@           @@@@@@@@@@@@@@@@                
   @@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@%%%%@@@@@@     @@@@@@            @@@@@@@@@@@@@@@@@               
    @@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%@@@@@@@@        @@@             @@@@@@@@@@@@@@@@@%              
     @@@@@@@@@@@@%@@@@@@@@@@@@@%%%%%@@@@@@@                         @@@@@@@@@@@@@@@@@@              
      @@@@@@@@@@@@@@@@@@@@@@@@@@%%%%@@@@@@                           %%@@@@@@@@@@@@@%%@             
        @@@@@@@@@@@@@@@@@@@@@@@%%%%@@@@@@@                            @%%%%%@@@@@@@@%@@             
         @@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@                             @@@@@@@@@@@@@@@@#             
         @@%@@@@@@@@@%@@@@@@%%@@@@@@@@@@                                @@@@@@@@@@@@@%#             
         @%@@@@@@@@@@@%@@%@@@%%@@@@@@@@@                                  @@@@@@@%%%%@              
        @%@@@@@@@@@  @%%%@%@@@@@@@%%@@@                                   @@@@@@@@@@ @              
       @@@@@@@@@@@@  @@@%@@%%%%@@@@@@@                                    @@@@@@@@@@@@@             
      @@@@@@@@@@@@   @@@@%%@@@@@@@@@@                                     %@@@@@@@@@@@@@@           
     @@@@@@@@@@@     @@@@@@@@@@@@@@@                                      %%@@@@@@@@@@@@            
    @@@@@@          @@@@@@@@%%@@@%@@                                        @@%@@@@@@%%%@           
    @             @@@@@@@@@@@@@                                                @%@@@%%%%#@@         
                  @@@@@@@@@@@@                                                  %#@@%#%%%#*%%       
                 @@%@#@%@@@@@@                                                   @*@@@#%%%%%@%      
                  @%%@@@@@@@@                                                     @@#%@@@@@@%#      
                  @@%%*@@@@%                                                        @@@@%%%%@       
                 @@%@@%@@@@%                                                                        
                %@%%@@@@@@@%                                                                        
                #@%%@@@%%@%                                                                         
                #%%%#%#@@%%                                                                         
                 *#%@@@@%@                                                                          
                  @%%%@@@                                                                           
          ''')
    print("Hey Devil May Cry, I am Dante, would you like to kill some demons?")
    dante_choice = input("1. Yes.\n2. No.\nMake your choice: ")
    if dante_choice == "1":
        dante2()
    elif dante_choice == "2":
        deaths_dante()
    else:
        print("Invalid input, Devil!\n")
        dante()

def dante2():
    print("You agreed to join Dante on a demon-hunting mission. You are teleported to a dark, gothic city filled with eerie sounds and shadows lurking around every corner. Dante hands you a sword. Do you take the sword?")
    dante_choice2 = input("1. Take the sword.\n2. Refuse the sword.\nMake your choice: ")
    if dante_choice2 == "1":
        dante3()
    elif dante_choice2 == "2":
        deaths_dante2()
    else:
        print("Invalid input, Devil!\n")
        dante2()
def dante3():
    print("You take the sword from Dante and feel a surge of power. You follow Dante through the dark alleys and into an abandoned cathedral where a horde of demons awaits. Do you charge into battle?")
    dante_choice3 = input("1. Charge into battle.\n2. Wait for Dante's signal.\nMake your choice: ")
    if dante_choice3 == "1":
        deaths_dante1()
    elif dante_choice3 == "2":
        dante4_2()
    else:
        print("Invalid input, Devil!\n")
        dante3()
def deaths_dante1():
    print("You charge into battle recklessly. The demons overwhelm you, and you are quickly defeated. GAME OVER!!!")
    try_again_dante = input("Do you want to try again? ")
    if try_again_dante == "yes":
        dante()
    elif try_again_dante == "no":
        choose_a_date()
    else:
        print("Invalid input, Devil!\n")
        deaths_dante2()
def dante4_2():
    print("You wait for Dante's signal. He nods at you, and both of you charge into battle together. The demons are fierce, but you and Dante fight valiantly. After an intense battle, you stand victorious. Do you explore the cathedral further or leave?")
    dante_choice4 = input("1. Explore the cathedral.\n2. Leave.\nMake your choice: ")
    if dante_choice4 == "1":
        dante5_1()
    elif dante_choice4 == "2":
        dante5_2()
    else:
        print("Invalid input, Devil!\n")
        dante4_2()
def dante5_1():
    print("You decide to explore the cathedral further. As you venture deeper, you discover a hidden chamber filled with ancient artifacts and a mysterious portal. Do you enter the portal?")
    dante_choice5_1 = input("1. Enter the portal.\n2. Don't enter the portal.\nMake your choice: ")
    if dante_choice5_1 == "1":
        dante6_1()
    elif dante_choice5_1 == "2":
        dante6_2()
    else:
        print("Invalid input, Devil!\n")
        dante5_1()
def dante6_1():
    print("You enter the portal and find yourself in a strange, otherworldly realm. You encounter a powerful demon lord. You don't know a way to get out, so the only way to survive is to fight the demon lord. After an epic battle, you defeat the demon lord and gained a cool sword that is also a guitar. After you grabbed the guitar you are teleported to the front of the cathedral, where Dante is waiting for you. Dante sees you have a the sword which is also a guitar, he asks you to play for him. You start playing and it was awesome.\nYOU WIN!!! That's your date.")
    the_end_dante = input("Do you want to go back to the menu? ")
    if the_end_dante == "yes":
        choose_a_date()
    elif the_end_dante == "no":
        print("Bye Bye 🤫🧏‍!!!")
    else:
        print("Invalid input, Devil!\n")
        dante6_1()
def dante6_2():
    print("You decide not to enter the portal. You leave the cathedral with Dante, having successfully completed your mission.\nYOU WIN!!! That's your date.")
    the_end_dante = input("Do you want to go back to the menu? ")
    if the_end_dante == "yes":
        choose_a_date()
    elif the_end_dante == "no":
        print("Bye Bye 🤫🧏‍!!!")
    else:
        print("Invalid input, Devil!\n")
        dante6_2()
def dante5_2():
    print("You decide to leave the cathedral. As you walk away, you feel that you missed something important. YOU LOSE!!!")
    try_again_dante = input("Do you want to try again? ")
    if try_again_dante == "yes":
        dante()
    elif try_again_dante == "no":
        choose_a_date()
    else:
        print("Invalid input, Devil!\n")
        dante5_2()
def deaths_dante():
    print("Dante didn't appreciate your refusal to join him. He leaves you behind, and you miss out the best adventure of your LIFE. GAME OVER!!!")
    try_again_dante = input("Do you want to try again? ")
    if try_again_dante == "yes":
        dante()
    elif try_again_dante == "no":
        choose_a_date()
    else:
        print("Invalid input, Devil!\n")
        deaths_dante()
def deaths_dante2():
    print("Without the sword, you are defenseless against the demons. They quickly overpower you. GAME OVER!!!")
    try_again_dante = input("Do you want to try again? ")
    if try_again_dante == "yes":
        dante()
    elif try_again_dante == "no":
        choose_a_date()
    else:
        print("Invalid input, Devil!\n")
        deaths_dante2()
def master_chief():
    print('''
                                                                                                              
                                                  ====++*****                                       
                                              --=++++++++********                                   
                                            :-:--======+++***+*++***                                
                                           -:==----======+++*###**+=*##                             
                                           ::==+*++*#%%%%%%@%%%%%%%%%%%%                            
                                         +-:=#*#####*****++#%%%%###%@@@                             
                                         ++-++#####**+--:::.:-+#*+=*                                
                                        #*+-+*####%#%*====-==+###*+*                                
                                     *#%%+==+####*%%#*+++=====+##**                                 
                                     *#%*-==-#%*==+*##*++==+=+*#**#                                 
                                     *%#%====#%*+=---=++++=+#%%*#%#@@ %%@%%##*+                     
                                    *#####+++#%#*+++=----==+#####*=%@%@@@@@%%%#**                   
                                   *******###%%#*#**+++==++*###*%##@@%@@@@@@@%%#*                   
                             %#####*********%###%###%#+++**####%%#%@@@@@@@@@@@%*++                  
                         *++#*%%##***#++*#+*@@%@%%%@%%%#++*####%%@@@@@%%%@@@@##*+                   
                       ++*%#++=+**#%#*++*=#%@%%#####%%%@%##%%%%%@@@@@%%%%%%#**##*                   
                      *++***+++*%%#*#====**#%@%#######%%%@@@@@@@@@@@@@@@%#***##**                   
                    ++++++**++*#%#***+=+=++*%@%%#***%@@@@@@@@@@@@@@@@@@%%##%#*#***                  
                   +++++++++*%%##****++=+++##@%##%#+*##%@@@@@%%@@@@%%#%%%%%@++*+++**                
                  +##+++=*#%%%###***+++====*#*###*++**#%%%@#*******+##*%@+++++++++*#***             
                 =#%#**####@**%%#**++======+#***##**######*+*++*++****#@#=++++++=*###*#**           
                =#@%**##########%#*++++==-==+***#**#*****++=+=-+====*#@%=====++=*####**#*#          
                -*#**######**##*#%%**++=--==*****:**+=*++++===-+-===*%@*++++-=++#*#####*##          
              =-=+*+*#%%%%****#*#*#%#*+=-++=#%#**+#--=++++++++++===+%%@%++====--*##**#**##          
            ===++**+*****%###**##**#%%#***+=*#*#*+++*+++++**++*++++#%%@@%+=--:::*#*****##*          
           =+*++*+====**##%#%######*##%**+*+****#+=+++++*#**#**+++*%@%#***--::-=##*****##           
         +++++*++++++*#*%@%#%%##******#%%**#*#%@%*++*#*#####**+++*%@@**++*=--=*%@%%###+#+           
      +++*+++#-*###*#%+*#%%%%%%###**+***#@#**+*#**##***######*++#%@%**+++++-+#@%%%%*#+#*            
     +=+++*#**+*++++++*##***#*#%%##****+*##*+++*#**###%@@@###*#%@@#++*+++*##%%@@%%**+**             
    *++*+++***++******#%**+##**#%%###+++++**+*+#%@#**##%%%%%%%%@@%*+*+++++**#%%@@**#=               
   **++****####********%****+#**#%%#**+++**##=#%*#%###%####%@@@@%*++-+++++*####%%*##                
  *++++*******###*###*#%*****###**#@*##**+*+**#+***%%@@@%##%%%%@##**+*+*+*##*####%#                 
  ******+*######%##%#*##*#*+*%%%%#**%%#**++#+*++*+-=*%@@@@@@%%@@#*+*-+*##**######%#                 
  ****#####%%%%%%%%####***++%@#%%@%#**#*+*=+**=+=--+*%@@@@@@@@@@#**#+*#%#*##%#####                  
    +*####**+***###%%@  +***%%%%@@@@%%%*+**==+++--+**##%%@@@@%*********##%%@@%###*                  
                          ++@@@@@@@##%#*+#++==+*+=#***##%@@#*+*##%#****+*=*++%###                   
                             #%@@@*###%%***+*==+**=+****#####*++*****##+=**#+**                     
                                  ***#%%******+==+#++**+%%%%#*****+=*##**##*+++#                    
                                ##@*##%##+******+=+**+=#**#@@@%***=-*#%######**                     
                                *#%%#%%%%%**+++#*++*++=%%##@@@@%####%##%%##*#%                      
                                ###*@%%%@*##+*#%#**=+++@%%%@@@@@%#%%###%%#@@%%                      
                               =*#+=+#%*###**#*%*#**=*%*+*#@@@@%@@@%%%%%#**##                       
                               =+*+=++*#*##*%**%###*%%%%#**%@@%%%%@@%%%####%                        
                               +##*++++***##%#%%%@*%%@@@@#*+*#%%%@@@%%##                            
                                #****+++*#@%##%%@@%####@@@**#**@@@@@%*#                             
                             +++##%###**#*+***#@@@%%@%%%%@@%*%%%@@@@%#%##*                          
                            ==+*+*##%###@**#+*++++-+%##%%@@@@@%@@@@@@@%#+-*                         
                            -=+++++**%######*##****#%%@@@@@@@@@@@@@@@@%#*==*                        
                        ##%%#++++++++*#%#####%##*###@@@@@%##@@@@@@@@@%%%#+=+                        
                       **#%@#++++=====*####%#####**#@@@@%#####%@@@%%%%##%%*+=                       
                       *#%%@*++++====+***#%%#####**#@@@@%%####*#@@%%%%%###%*+                       
                       *%%@%*++*+++*++=+*#%@%##****#@@@@######*##@@%%%%####%+                       
                       *%%@#*+++***+==+++*#@@@#####%@@@@%########%@@@%%%###*#*                      
                       *%%@#***#*+++=+++**%@@@@%%%%%@@@%%##*#*#*##%@@%%%####+%                      
                      +*%@@%#*+++==++++**#@@@@@@@@%@ @@%%##****#*##%@%%%####**                      
                      +*%@%#*++++++++++*%@@@@@@@%%   @@%###*#******#%@%%%%%##=%                     
                      +#@@##*+++++++++*#@@@@@@@@%@   @%%#####******#@@@%%%%##+*                     
                     =+%%@##*+++++++++*%@@@@@@@@##    %%#######****%@@@%##%%#%+                     
                     =*%@@#**++++=+++**%@@@@@@@%*+     ####%##*#***%@@@@%##%%%*%                    
                     =#%@%#**++++***+##%@@@@@@@#+      *#%###*#*****#%%%%%#####*                    
                    ++%%@%#*+****+**%%%%@@@@@%%#        **##*****#*+=+##%%%%%%##%                   
                    +*%@@%#*****+***%%%@@@@@@%*+         =*###%%*++++=-+*#%%#%%#*                   
                   @**#@@###****+***@##%@@@@@#+          *+@%#*+=-=:-==+**#%%%%%*                   
                    +#@@@**+*******#%###%@%%@*            *#**+#+++++++==**#%%%%**                  
                        =+++#*******#%###%%%#+           ##++*+**++++++=*#%%%%%%#*                  
                        -=+*#*****##*###%%%@%%*         ******++#**+++**#%@@@@@%%#                  
                        -=**#*****##*#%%@@@@%%#          #****++*****#*#%@@%%%%@%#                  
                        =+*##%%@%%###%%%@@@%*@            ++%****###*#%@%%%%%%%%@%                  
                        =*%%%###%%@@%%%%@@@#*              **#*#*#%@@%#%%@@@@%%#%#                  
                         ==##%%%%%%@@%@@@@%#                **#%%%######%%**####***                 
                         =+#%%%%%@@@@@@%@%%                  #******####%*+*##**###                 
                         ++**%%%%@%%@@%##                     ++******###++*######***               
                       **+*##***#*+%@@%#*                      +****###%#*+=+**#******              
                       =*##%%%#####%@@#*                       ++***+++=*++==+**#*#****             
                      +=+*#%########@%*#                       ++*+++++++=+++*%%#**###              
                     ++-+*%##**#****#****                     +-*==+#**++=+++#########              
                     =*=##%####***#**##++                     --+=+++++++*+++#########              
                    =-=*#######%##*+*#**#                     ==**********++*#######%%              
                   +==+###########**##**#                     +++++++++*#****###%%#%%%              
                   +++#%%%#######%#%##**#                    *++*+++++**##**#%%@@@%%                
                   ****#%@@@@%%%%#%%%###%                    ++*+++++*****%%@@@@@@%                 
                   +*#**#%@@@@@@@%@%%####                    =+**+++***#***#%%%%%%#                 
                   +****#%%%%%%%%%@@%%#*                     =+=******##****#######                 
                    %*+##%%%%%%%%%@@@%##                     -+***##**#*****######%                 
                    %=+*%%%%%%%%%%@%%##                      =+*****###***###%%%%#                  
                    *++#%%%%%%%%%%%%#%                       +*****###*****#%%%%%*                  
                    +++#%#%%%%%%%%%@                          ***##*%******##%####                  
                    =+*#####%%%%%%#                            **##%#*******######                  
                   ===*%%#%%%%%%%#                              *#%%#*****+*######                  
                   *++#%###%%%%%%#                              %%##***++++*######                  
                  ****%%%%%%%%%%%#                                *******+++######%                 
                  ****%%%%%%%%%%%*                                ***********######                 
                  **+#%%%%%%%%%@%*                                **#********######                 
                  *++#@%%%%%%%%%%#                                 *#*******+*######                
                   +###%%%%%##%@@                                 +****#*#****#%%###                
                  +=#########**#                                  ***+*##*****#%####                
                 *-*%%%%%%%%##**                                  ****+*#*****%@%%%#                
                #+=#%%%%%%%%%#**#                                 +##****##%##%%%%%###              
                *+***###########%                                  #@%##%%###+#####****             
                #*++#####%%##*%%@                                    *##%#*+++*##*****#*            
                **=*######%######                                   ==#%#**+****########*           
              ++#**+###########%%##                                *-=+**********#%%%#%%%@          
             *-#%#++##**#####*%@%#+*                              **+*+********#%##%##****          
             =+%*+**#%%%%%%%#**#@%#*                              =*#*#*#***###****####****         
              #%**#%%%%%%%%%%##%@@                                ++****%##%#*******####****        
                 ###%@@@@@@%%%%                                   *****#@@###*****##*******#*#      
                   @@                                             *#*#**%****##*********####***     
                                                                    #%%%#**+##%##+********#####*    
                                                                       @*++*##%#***+*****######%#   
                                                                       +#*+#%#%#******#*#%%#%%%%#   
                                                                               %%#%##**###%@@@%%#   
                                                                                    @%##%@          
          ''')
    print("My name is Master Chief soldier, who is our enemy?")
    master_choice = input("1. The Covenant.\n2. The Flood.\nMake your choice: ")
    if master_choice == "1":
        master_covenant1()
    elif master_choice == "2":
        master_flood1()
    else:
        print("Invalid input, Soldier!\n")
        master_chief()
def master_covenant1():
    print("You have chosen to fight the Covenant. Master Chief briefs you on the mission. You are to infiltrate a Covenant base and retrieve important intel. Do you proceed with caution or go in guns blazing?")
    master_choice2 = input("1. Proceed with caution.\n2. Go in guns blazing.\nMake your choice: ")
    if master_choice2 == "1":
        master_covenant2()
    elif master_choice2 == "2":
        master_death_covenant()
    else:
        print("Invalid input, Soldier!\n")
        master_covenant1()
def master_covenant2():
    print("You proceed with caution. Master Chief signals you to take cover. You see a group of Grunts patrolling. Do you take them out silently or wait for them to pass?")
    master_choice3 = input("1. Take them out silently.\n2. Wait for them to pass.\nMake your choice: ")
    if master_choice3 == "1":
        master_covenant3()
    elif master_choice3 == "2":
        master_death_covenant()
    else:
        print("Invalid input, Soldier!\n")
        master_covenant2()
def master_covenant3():
    print("You take out the Grunts silently. Master Chief gives you a thumbs up. You continue deeper into the base and find the intel. Do you grab the intel and leave or explore further?")
    master_choice4 = input("1. Grab the intel and leave.\n2. Explore further.\nMake your choice: ")
    if master_choice4 == "1":
        master_victory()
    elif master_choice4 == "2":
        master_death_covenant()
    else:
        print("Invalid input, Soldier!\n")
        master_covenant3()
def master_flood1():
    print("You have chosen to fight the Flood. Master Chief hands you a shotgun and a flamethrower. Do you take both weapons or just one?")
    master_choice2 = input("1. Take both weapons.\n2. Take the shotgun only.\n3. Take the flamethrower only.\nMake your choice: ")
    if master_choice2 == "1":
        master_flood2()
    elif master_choice2 == "2":
        master_flood3()
    elif master_choice2 == "3":
        master_flood4()
    else:
        print("Invalid input, Soldier!\n")
        master_flood1()
def master_flood2():
    print("You take both weapons. Master Chief leads you into a dark, infested area. You hear the eerie sounds of the Flood. Do you stick close to Master Chief or scout ahead?")
    master_choice3 = input("1. Stick close to Master Chief.\n2. Scout ahead.\nMake your choice: ")
    if master_choice3 == "1":
        master_flood5()
    elif master_choice3 == "2":
        master_death_flood()
    else:
        print("Invalid input, Soldier!\n")
        master_flood2()
def master_flood3():
    print("You take the shotgun only. Master Chief leads you into a dark, infested area. You hear the eerie sounds of the Flood. Do you stick close to Master Chief or scout ahead?")
    master_choice3 = input("1. Stick close to Master Chief.\n2. Scout ahead.\nMake your choice: ")
    if master_choice3 == "1":
        master_flood5()
    elif master_choice3 == "2":
        master_death_flood()
    else:
        print("Invalid input, Soldier!\n")
        master_flood3()
def master_flood4():
    print("You take the flamethrower only. Master Chief leads you into a dark, infested area. You hear the eerie sounds of the Flood. Do you stick close to Master Chief or scout ahead?")
    master_choice3 = input("1. Stick close to Master Chief.\n2. Scout ahead.\nMake your choice: ")
    if master_choice3 == "1":
        master_flood5()
    elif master_choice3 == "2":
        master_death_flood()
    else:
        print("Invalid input, Soldier!\n")
        master_flood4()
def master_flood5():
    print("You stick close to Master Chief. Together, you fight off waves of the Flood. You reach the heart of the infestation. Do you destroy it with the shotgun or the flamethrower?")
    master_choice4 = input("1. Use the shotgun.\n2. Use the flamethrower.\nMake your choice: ")
    if master_choice4 == "1":
        master_flood6_shotgun()
    elif master_choice4 == "2":
        master_flood6_flamethrower()
    else:
        print("Invalid input, Soldier!\n")
        master_flood5()
def master_flood6_shotgun():
    print("You use the shotgun to destroy the heart of the infestation. The Flood is eradicated, and you and Master Chief are victorious. YOU WIN!!! That's your adventure.")
    the_end_master = input("Do you want to go back to the menu? ")
    if the_end_master == "yes":
        choose_a_date()
    elif the_end_master == "no":
        print("Bye Bye 🤫🧏‍!!!")
    else:
        print("Invalid input, Soldier!\n")
        master_flood6_shotgun()
def master_flood6_flamethrower():
    print("You use the flamethrower to destroy the heart of the infestation. The Flood is eradicated, and you and Master Chief are victorious. YOU WIN!!! That's your adventure.")
    the_end_master = input("Do you want to go back to the menu? ")
    if the_end_master == "yes":
        choose_a_date()
    elif the_end_master == "no":
        print("Bye Bye 🤫🧏‍!!!")
    else:
        print("Invalid input, Soldier!\n")
        master_flood6_flamethrower()
def master_death_covenant():
    print("You are mission was to invade not destroy the covenant forces. By not having a army or powerfull guns, you get overwhelmed by the Covenant forces. GAME OVER!!!")
    try_again_master = input("Do you want to try again? ")
    if try_again_master == "yes":
        master_chief()
    elif try_again_master == "no":
        choose_a_date()
    else:
        print("Invalid input, Soldier!\n")
        master_death_covenant()
def master_death_flood():
    print("You are overwhelmed by the Flood. GAME OVER!!!")
    try_again_master = input("Do you want to try again? ")
    if try_again_master == "yes":
        master_chief()
    elif try_again_master == "no":
        choose_a_date()
    else:
        print("Invalid input, Soldier!\n")
        master_death_flood()
def master_victory():
    print("You successfully retrieve the intel and returned to base. YOU WIN!!! That's your date.")
    the_end_master = input("Do you want to go back to the menu? ")
    if the_end_master == "yes":
        choose_a_date()
    elif the_end_master == "no":
        print("Bye Bye 🤫🧏‍!!!")
    else:
        print("Invalid input, Soldier!\n")
        master_victory()
def gojo():
    print('''
        
                                   :.::.:..:                                              
                               ..::.......::.:                                            
                              ::.............::                                           
                              :...............:                                           
                              :...............:-                                          
                              ::...::::::::::::                                           
                               :-:-------==+#+                                            
                     -=          ####%%%%@@@%+=                                           
                     --          =%%%%%%@%%*=+                                            
                   =-:=          ==-----::::=                                             
                   --:=   -+     %@%=::::::-@@@@                                          
                   --==-==-+    %%%%%=--==+#@@@%                                          
                   =-=-=++#      %@%%%%%%@@%%@@%                                          
                   =-::--+       @@@@@%%%%%%@@%##                                         
                   +-::==+     **#%%@@%@@%%%%%@%%#**                                      
                   #=:::=-*****%%%%%%%####@%%%%%%%%%****#                                 
                  #%#:::-%**%%%%%%%%%%%%%%%%%%#%%%%%%%%##%#                               
                  #*#=:--@@%###%%%%%%%##%%%%%%%%%#%%%%%%@@#                               
                  %#%%%%%%@%%%#**#%%%%*#%%%%####%%%%%%%@@@%#                              
                  #%%%%%%@@%%%%%%#***#*%%%%%%%%%%%%%%%%@@@%#                              
                  %@%%%%%@@@%%%%%%%#***%%%%%%%%%%%%%%%@@@@@#                              
                  %@@%%%%@@@@@%%%%%%%%*%%%%%%%%%%%%%%%@@@@@@%                             
                  #@%%%@@@@@@@@%%%%%%%#%%%%%%%%%%%%%%%@@@@@@%                             
                  #@%%%%@@@@@@%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@                            
                  #@%%@@@@@@@@@@%%%%%%%%%%%%%%%%%%%@@@@@@@@@@%                            
                 ##@@%@@@@@@@@@@%%#%%%@%%%%%%%%%@@@@@@@@@@%@@%                            
                  #%@@@@@@@%@@@@%%%%#%%%%@%%%%%%@@@@@%@@@%%@@@%                           
                  ##@@%@@@@ @@@@@%%%%%*##@%%%%@%@@@@%#@@@#@@@@@                           
                  ###%@@%  %@@@@@@%%%%#%%%%%%%@@%@@@@ %%#%@@@@@%                          
                     @     @@@@@@@@%%%%%%%%%@@@@#@@@@  %@@%%%@@%                          
                           @@@@%@@@%%%@%%%%%@@@@%@@@@  #%%%@@@@                           
                            @@@@#%%%%%@%%@%%@@@@@#@@@@%#%@@@@@%                           
                            @@@@@@@%%@@%%@%%%@@@@#@@@%%#%#%%%@%                           
                           %@@@@@@%%@%@%%%@@%@@@@@#@@%%%%%%@%%                            
                           @@@@@@@@@%%%%%@%%%@@@@@#%@%##%%%%%                             
                           @@@@@@@@@@%@%%@@@%%%@@@@#*#%@@%%%                              
                           @@@@@@@@@@@@%@@@%@@@@@@@%*%@@@@@%                              
                          %@@@@@@@@@@@@##%@@@@@@@@@@%=%@@@@                               
                          @@@@@@@%%%%%@@@@@@@@@@@@@@@=-%@%                                
                          %@@@@@@@%#**@@@@@@@@@@@@@@@@@%                                  
                          %@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                                  
                           @@@@@@@@@@@@@@@@@@@@@@@@@@@%%                                  
                           @@@@@@@@@@@@@@@@@@@@@@@@@@@%                                   
                           %@@@@@@@@@@@@ %@@@@@@@@@@@@                                    
                           %@@@@@@@@@@@  @@@@@@@%@@@@%                                    
                           @@@@@@@#%@@%   @@@@@@@@@@@%                                    
                           @@@@@%#@@@@    @@@@@@%%@@%                                     
                           @@@@%#@@@@%    @@@@@@@@@@%                                     
                           %%%%%@@@@%     @@@@@@@@@%                                      
                           %%%%%%%@@      @@@@@%%@@%                                      
                          %%%%%%#@@%      @@@%%%%%%                                       
                          #%%%%#*%@      @@@%%%%%@%                                       
                          %%%%#*#%@      %@@%%%%%%                                        
                          %%%#**#@%      %@%%%%%%%                                        
                          ###***%@@      %@%%%%%#%                                        
                          %#***#%@@      %@%%%%%*#                                        
                          %%%##%@@@      @@%%%%%#*                                        
                           %@@@@@@@      @%@%%%%%                                         
                            @@@@@@@@    %@@%%%@%                                          
                            @@@@@@@@    %@%%%##%                                          
                            %@@@@@@@%  %@@@%%%%%                                          
                             @@@@@@@%  %@@%%%@@%                                          
                             @@@@@@@   @@@%%%%%                                           
                             @@@@@@@@  @@@@@@@%                                           
                              %@@@@@@% %@@@@@@%                                           
                              %@@@@@@% %@@@@@@%                                           
                               @@@@@@@ %@@@%@@%                                           
                               %@@@@@@%%@@@@%%%                                           
                                @@@@@@@%@@@@@##                                           
                                @@@@@@@@@@%@@@                                            
                                @@@@%@#@@@@%@@#                                           
                                @@@%#%#@@@@@##                                            
                               %@@%%%%%@@@%%@@                                            
                               %%%%#%%%@@@%%@@                                            
                               %%%%%%%%@%%#%@@                                            
                                @@@%   @%%*%%@%                                           
                                       @@%#%%%@%                                          
                                        @@%##%%@%                                         
                                         @@%%%%%%%                                        
                                           %%@@@@@                                        
          ''')
    print("Your weak. I am Gojo the strongest sorcerer alive, would you like my help in killing curses?")
    gojo_choice = input("1. Yes, I need your help.\n2. No, I can handle it alone.\nMake your choice: ")
    if gojo_choice == "1":
        gojo_help()
    elif gojo_choice == "2":
        gojo_alone()
    else:
        print("Invalid input, Sorcerer!\n")
        gojo()
def gojo_help():
    print("Gojo decides to help you. He uses his incredible strength to defeat the curses effortlessly. After the battle, Gojo invites you to a special training session. Do you accept?")
    gojo_choice2 = input("1. Yes, I want to train with you.\n2. No, I am tired.\nMake your choice: ")
    if gojo_choice2 == "1":
        gojo_training()
    elif gojo_choice2 == "2":
        gojo_rest()
    else:
        print("Invalid input, Sorcerer!\n")
        gojo_help()
def gojo_training():
    print("You accept the training session. Gojo takes you to a secluded area where he teaches you advanced techniques. You feel your power growing. Do you challenge Gojo to a sparring match or continue learning from him?")
    gojo_choice3 = input("1. Challenge Gojo to a sparring match.\n2. Continue learning.\nMake your choice: ")
    if gojo_choice3 == "1":
        gojo_sparring()
    elif gojo_choice3 == "2":
        gojo_learning()
    else:
        print("Invalid input, Sorcerer!\n")
        gojo_training()
def gojo_rest():
    print("You decide to rest, but curses never rest and while you were asleep they killed you. GAME OVER!!!")
    try_again_gojo = input("Do you want to try again? ")
    if try_again_gojo == "yes":
        gojo()
    elif try_again_gojo == "no":
        choose_a_date()
    else:
        print("Invalid input, Sorcerer!\n")
        gojo_rest()
def gojo_sparring():
    print("You challenge Gojo to a sparring match. Despite your improved skills, Gojo easily defeats you but praises your progress. He offers you the chance to become his apprentice. Do you accept?")
    gojo_choice4 = input("1. Accept the apprenticeship.\n2. Decline and continue on your own path.\nMake your choice: ")
    if gojo_choice4 == "1":
        gojo_apprentice()
    elif gojo_choice4 == "2":
        gojo_independent()
    else:
        print("Invalid input, Sorcerer!\n")
        gojo_sparring()
def gojo_learning():
    print("You continue learning from Gojo. He teaches you many advanced techniques and secrets of sorcery. You feel confident and ready to face any challenge. YOU WIN!!!")
    the_end_gojo = input("Do you want to go back to the menu? ")
    if the_end_gojo == "yes":
        choose_a_date()
    elif the_end_gojo == "no":
        print("Bye Bye 🤫🧏‍!!!")
    else:
        print("Invalid input, Sorcerer!\n")
        gojo_learning()
def gojo_apprentice():
    print("You accept the apprenticeship. Gojo becomes your mentor, and under his guidance, you become one of the strongest sorcerers in history. YOU WIN!!!")
    the_end_gojo = input("Do you want to go back to the menu? ")
    if the_end_gojo == "yes":
        choose_a_date()
    elif the_end_gojo == "no":
        print("Bye Bye 🤫🧏‍!!!")
    else:
        print("Invalid input, Sorcerer!\n")
        gojo_apprentice()
def gojo_independent():
    print("You decide to continue on your own path. Gojo respects your decision and wishes you luck. You set out on your journey, stronger and more determined. YOU WIN!!!")
    the_end_gojo = input("Do you want to go back to the menu? ")
    if the_end_gojo == "yes":
        choose_a_date()
    elif the_end_gojo == "no":
        print("Bye Bye 🤫🧏‍!!!")
    else:
        print("Invalid input, Sorcerer!\n")
        gojo_independent()
def gojo_alone():
    print("You decide to handle the curses alone. Despite your efforts, you realize you are not strong enough, they overwhelmed you and you DIED. GAME OVER!!!")
    try_again_gojo = input("Do you want to try again? ")
    if try_again_gojo == "yes":
        gojo()
    elif try_again_gojo == "no":
        choose_a_date()
    else:
        print("Invalid input, Sorcerer!\n")
        gojo_alone()
def po():
    print('''
                                   ===                                                              
                                 *+*####                                                            
                                +*#%@@@%%                                                           
                                **#%%@%%=..........                                                 
                                ..::.......................=##*+                                    
                             .................:-:.........:::=%##                                   
                          .............:=*#%%%%%%*:.:...:::::::+                                    
                         ...........:*%%%%%%%%%@@%-.::.:-*%%%*---                                   
                        ...........=#%%%@%#+=*%@@%-..::-#%%%%%%*---                                 
                        ..........-*#%%%@+.+++-#%#:..::+%@@@@%%%*=--                                
                       +:..........-*%%%@%*##*+#*:...:-##-..-%@%#=--=                               
                      ##:...........:+*#%%%%%+:.......:+#*#:.+@%%*-=-                               
                     %%#-..............:::.....-=:......:*+:-#%%%#--=-                              
                    %%%%*:........::::::::....-%%%%#+=---=*%%%%%##=--==                             
                    %%%%#-:::::::::::::---::::.:%@@@@@@@@%=+#%%%#*---==                             
                   %%%%%%%-::::::::::----:..-+-::=#@@@@@#++======---===                             
                  %%%%%%%%%=::::::::::--:.....-#+==++=++**+++==========                             
                  %%%%%%%%%%*-:::::::::::......::=*#####+++++++====+++                              
                 %%%%%%%%@%%%%+::::::::::::::::::::--=++++++++++++++++                              
                #%%%%%%%%%%%%@%%+-::::::.::::::----==++++++++++++++++%                              
              ##%%%%%%%%%%@@%%%%%%+-:.....::----===++++++++++++++++*@@@                             
            #%%%%%%%%%%@@%@%@%@%%%%@#+-::::::-====++++++======+++*%@@@@@@@                          
          %%%%%%%%%%%@@@@@@%@@@@@@@@@%%%+-::::::--==========++*%@@@@@@@@%%%%%%                      
        %%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@%#*+=--------==+*#%@@@@@@@@@@%%%%%%%%%%%                   
      %###%%%%%%%%%@%@@@@@@@@@@@@@@@@@@@@@@@@@%%%##%%%%@@@@@@@@@@@@%%%%%%%%%%%%%%%%                 
     ###%%%%%%%%%%%%%@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%               
    %#%%%%%%%%%%%@@%%@@@@@@@@@@@@@@@@@@%@%@@%@@@@@@@@@@@@@@@%@@%%%%%%%%%%%%%%%%%%%%%%%%             
   %%%%%%%%%%%%%%%%@@@%@@@@@@%%%%%@@@@@@@@%@@@%@@@@@@@@@@@@@@@@@@%@@@%%%%%%%%%%%%%%%%@%%            
  %%%%%%%%%%%%%%%%@%@@@@@@%%%%%%@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%@%%%@@@@@@%%%%%%%%%%%%%%%@%%          
 %%%%%%%%%%%%%%%%%%%@@@@@@@@@%%%@%@@@%%%%%%%%%%%%%%%%%%%%%%%@%@@@@@@@@@@%%%%%%%%%%%%%%@@@@%         
 %%%%%%%%%%%%%%%%%%@%%%%%%%@@@@%%%%%%%%%%%%%%%@%%%%%%%%%%%%%@@@@@@@@@@@%%%%%%%%%%%%%%%%@@@@%        
%%%%%%%%%%%%%%%%%%%%%%%@%%@%%%%%%%%%%%%%%%%%%%@%%%@@%%%%%%@@@@@@@@@@@%%%%@%%%%%%%%%%%%@@@@@@@       
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@%%@%%@%@@@@@@@@%%@%@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%@@@@@@      
 %%%%%%%%%%%%%%@%%%%%%%%%@@%%%@%%%@@%@@%%%%@@@@@%@@@@@@@@@@@@@@@@%%%%%@%%%%%%@@%%%%%%%%@@@@@@@      
 %%%%%%%%%%%%%%%%%%@%%%@%%%@@@@%@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@%%%%%@@%%%%@@%%%%%%%%%@@@@@@@@@     
 %%%%%%%%%%%%%%%%%@%%%%%%@@%@@@%@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@%%%%%@%%%%@%%%%%@%%@%%@%@@@@@@@@@    
  %%%%%%%%%%%%%%%%%@%@%@@@@@@%@@@@%@@@@@@@@@%@@@@@@@@@@@@@@@@%%@%%@%%@@@%%@%%@%@@%%%%@@@@@@@@@@@    
  %%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@%%%@@%%@@%%%%%%%%%%%%%%%@@@@@@@@@@@@@%%  
   %%%%%%%%%%%%%%%%%%@@%@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%@@%@@%@%@%@%%%@@@%@@@@@@@@@@@@@@%  
    %%@%%%%@%@@@@@@@@@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@%@%@@@@@%%@@%%%@@%@@@@@@@@@@@@@@@@@@   
     %@@@%@%@%%@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@%%%@@@@@%@@@@@@@@@@@@@@@@@@@@@   
      @@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%   
      @@@@@@@@%@%%@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%   
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%     
         @@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%#%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        
           ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%##*******##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         
            .=%@@@@@@@@@@@@@@@@@@@@@@@@@@##**+++==========++*%@@@@@@@@@@@@@@@@@@@@@@@@@@            
           ...:-#@@@@@@@@@@@@@@@@@@@@%%#*+++===-------:::------==+*#%@@@@@@@@@@@@@@#*#              
           ....:::=%@@@@@@@@@@@@@%##**++===-----:::::::::::::::-----===+*##%%##**++==-              
           ....:::::-=+**####***+++====----::::::::::::::::::::::::-----===+++*++++===              
           ....::::::::----===--------:::::::::::::::::::::::::::::::-------===++++====             
           .....::::::::::::::::::::::::::::::::::::::::::::::::::::::::------=========             
           .......:::.:::::::::::::::::::::::::.....:::::::::::::::::::::------========             
           ..................:::::::::.:::.:.........::::::::::::::::::::------=========            
           ..........................::....:...........:::::::::::::::::::------========            
           ...........................................:.::::::::::::::::::-------=======            
            -:.....................................::::.:::::::::::::::::--------======+*           
            =-::::::::...........................:::::.::::::::::::::::----------=====+*#           
            +++-:::::::::......................:::::::::::::::::::::::---------=====++**#           
            -=+==--:::::::::::::.......:...::::::::::::::::::::::::::-------======+*#++#            
            -::-**==---:::::::::::::::::::::::::::::::::::::::::::-------=====++**++#+#%            
            :::::-+**+==-----::::::::::::::::::::::::::::::----------====++++**##*+###*             
            :::::---=+#**======----------------------------========+++++*##*++*##*##*++             
            :::::--:----+*+*#**===++++==================++++*++++####+++###**#%%#***+++             
            ::::::::::-----==+++**+###*+++*###*+++*###*++*###*++*%%%#*##%%###***+**+++=             
            ::=:::::--::------==---===*###%%%%####%%%%##%%%%%%%%%%#######**********++==             
            ::----:::::--------=-=-=====+++=++*#####################*************+===--             
            :---===-:::-------=====+++++++*=+*****#*######**####*###**********++==----:             
           :-----------======+==++++++++++*******#*#*#################*******+====-----             
           ---=--*+=========++=+++++++++++*****##########################**++======---:             
           #+---*@+=========++++++++++++********#######################***++++++====---             
           #%%#+@@+======++++++++++++******#*#########%###%%%########******++++++====+=             
          =#%%%%@%*=====++++++*+*******#############%%##%%%%%%####*##*********++=+*%%#              
          +#%%%%%@@@%#*+==+++++******######%%%         %%%%%###########***+++#%%@@@%%#              
          -*%%%%@@@@@@@@@@%##*******######%%             %%%%####*****#%%@@@@@@@@%@%%%              
          :-=#@@@@@@@@@@@@@@@@@@@@@@@@@@%%                @@@@@@@@@@@@@@@@@@@@@@@@@%%#              
          .:==-*%@@@@@@@@@@@@@@@@@@@@@@                    @@@@@@@@@@@@@@@@@@@@@@@%+-               
          :---====+#%@@@@@@@@@@@@@@@@                       @@@@@@@@@@@@@@@@@@%#+====               
          ---====++===+*#%@@@@@@@@%                           @@@@@@@@@@@%#*+++**+=----             
         ::-----=+++*************                              #**************+=+++=--+=            
        ---==--=====++**#####*                                    ##%##**++=============**          
        ==+++==-=**+++**####                                        %#**+=++======+%%*++*%          
       ###%#++=+#%%#+*##%%%@                                        %%%%%%%%#######%%%%%%%          
        %######%%%%%%%%%@@                                                 @@@%@@@@@@@@             
          ''')
    print("Hello I am Po, the Dragon Warrior, do you want to help me in saving China?")
    po_choice = input("1. Yes, I want to help.\n2. No, I have other things to do.\nMake your choice: ")
    if po_choice == "1":
        po_help()
    elif po_choice == "2":
        po_no_help()
    else:
        print("Invalid input, Warrior!\n")
        po()

def po_help():
    print("Po is glad to have your help. Together, you train hard and prepare for the upcoming battle against Tai Lung. Do you focus on learning martial arts or on strategy?")
    po_choice2 = input("1. Learn martial arts.\n2. Focus on strategy.\nMake your choice: ")
    if po_choice2 == "1":
        po_martial_arts()
    elif po_choice2 == "2":
        po_strategy()
    else:
        print("Invalid input, Warrior!\n")
        po_help()

def po_martial_arts():
    print("You train rigorously in martial arts. Your skills improve significantly, and you feel ready for the battle. Do you face Tai Lung directly or support Po from the sidelines?")
    po_choice3 = input("1. Face Tai Lung directly.\n2. Support Po from the sidelines.\nMake your choice: ")
    if po_choice3 == "1":
        po_battle()
    elif po_choice3 == "2":
        po_support()
    else:
        print("Invalid input, Warrior!\n")
        po_martial_arts()

def po_strategy():
    print("You focus on strategy and devise a clever plan to defeat Tai Lung. With your strategy, Po gains the upper hand in the battle. Do you assist Po in executing the plan or stay back and watch the outcome?")
    po_choice3 = input("1. Assist Po.\n2. Stay back.\nMake your choice: ")
    if po_choice3 == "1":
        po_plan()
    elif po_choice3 == "2":
        po_watch()
    else:
        print("Invalid input, Warrior!\n")
        po_strategy()

def po_battle():
    print("You face Tai Lung directly and engage in a fierce battle. Despite your efforts, Tai Lung is too strong, and you get defeated. GAME OVER!!!")
    try_again_po = input("Do you want to try again? ")
    if try_again_po == "yes":
        po()
    elif try_again_po == "no":
        choose_a_date()
    else:
        print("Invalid input, Warrior!\n")
        po_battle()

def po_support():
    print("You support Po from the sidelines, providing crucial assistance at key moments. Together, you and Po defeat Tai Lung. But soon, you learn about a new threat: Chen, a powerful warlord. Do you continue your journey to defeat Chen?")
    po_choice4 = input("1. Yes, let's defeat Chen.\n2. Nah, I'm done.\nMake your choice: ")
    if po_choice4 == "1":
        po_chen()
    elif po_choice4 == "2":
        po_no_chen()
    else:
        print("Invalid input, Warrior!\n")
        po_support()

def po_plan():
    print("You assist Po in executing the strategy. Your plan works perfectly, and Tai Lung is defeated without much struggle. However, a new threat arises: Chen, a powerful warlord. Do you join Po in facing this new challenge?")
    po_choice4 = input("1. Yes, let's defeat Chen.\n2. No, I'm done for now.\nMake your choice: ")
    if po_choice4 == "1":
        po_chen()
    elif po_choice4 == "2":
        po_no_chen()
    else:
        print("Invalid input, Warrior!\n")
        po_plan()

def po_watch():
    print("You stay back and watch as Po executes the plan. But Po's IQ is very bad and he didn't fully understand the plan. Po is deafeated and China gets destroyed by Tai Lung.\nGAME OVER!!!")
    try_again_po = input("Do you want to try again? ")
    if try_again_po == "yes":
        po()
    elif try_again_po == "no":
        choose_a_date()
    else:
        print("Invalid input, Warrior!\n")
        po_watch()

def po_chen():
    print("You and Po embark on a new journey to defeat Chen. Along the way, you encounter various challenges that test your strength and resolve. Do you continue to train or focus on gathering allies?")
    po_choice5 = input("1. Continue training.\n2. Focus on gathering allies.\nMake your choice: ")
    if po_choice5 == "1":
        po_training()
    elif po_choice5 == "2":
        po_allies()
    else:
        print("Invalid input, Warrior!\n")
        po_chen()

def po_training():
    print("You and Po continue your training, becoming even stronger. As you near Chen's fortress, do you plan a surprise attack or confront him head-on?")
    po_choice6 = input("1. Plan a surprise attack.\n2. Confront him head-on.\nMake your choice: ")
    if po_choice6 == "1":
        po_surprise()
    elif po_choice6 == "2":
        po_head_on()
    else:
        print("Invalid input, Warrior!\n")
        po_training()

def po_allies():
    print("You focus on gathering allies and form a formidable team. With the help of your new allies, you prepare to face Chen. Do you launch a coordinated attack or try to infiltrate his fortress?")
    po_choice6 = input("1. Launch a coordinated attack.\n2. Infiltrate his fortress.\nMake your choice: ")
    if po_choice6 == "1":
        po_coordinated_attack()
    elif po_choice6 == "2":
        po_infiltrate()
    else:
        print("Invalid input, Warrior!\n")
        po_allies()

def po_surprise():
    print("You and Po plan a surprise attack on Chen's fortress. The attack catches Chen off guard, and after a fierce battle, you defeat him. YOU WIN!")
    the_end_po = input("Do you want to go back to the menu? ")
    if the_end_po == "yes":
        choose_a_date()
    elif the_end_po == "no":
        print("Bye Bye 🐼👋!!!")
    else:
        print("Invalid input, Warrior!\n")
        po_surprise()

def po_head_on():
    print("You and Po confront Chen head-on. The battle is tough, but with your combined strength, you manage to defeat him. YOU WIN!!! That's your date.")
    the_end_po = input("Do you want to go back to the menu? ")
    if the_end_po == "yes":
        choose_a_date()
    elif the_end_po == "no":
        print("Bye Bye 🐼👋!!!")
    else:
        print("Invalid input, Warrior!\n")
        po_head_on()

def po_coordinated_attack():
    print("You launch a coordinated attack with your allies. The plan works perfectly, and Chen's forces are overwhelmed. You defeat Chen and save China. YOU WIN!!! That's your date.")
    the_end_po = input("Do you want to go back to the menu? ")
    if the_end_po == "yes":
        choose_a_date()
    elif the_end_po == "no":
        print("Bye Bye 🐼👋!!!")
    else:
        print("Invalid input, Warrior!\n")
        po_coordinated_attack()

def po_infiltrate():
    print("You and your allies infiltrate Chen's fortress. Using stealth and strategy, you reach Chen and defeat him in a surprise attack. YOU WIN!!! That's your date.")
    the_end_po = input("Do you want to go back to the menu? ")
    if the_end_po == "yes":
        choose_a_date()
    elif the_end_po == "no":
        print("Bye Bye 🐼👋!!!")
    else:
        print("Invalid input, Warrior!\n")
        po_infiltrate()

def po_no_help():
    print("You decide not to help Po. Without your assistance, Po loses, Tai Lung wreaks havoc and destroys China. GAME OVER!!!")
    try_again_po = input("Do you want to try again? ")
    if try_again_po == "yes":
        po()
    elif try_again_po == "no":
        choose_a_date()
    else:
        print("Invalid input, Warrior!\n")
        po_no_help()

def po_no_chen():
    print("You decide not to help Po against Chen. Without your assistance, Chen defeats Po, conquers China and rules with an iron fist. GAME OVER!!!")
    try_again_po = input("Do you want to try again? ")
    if try_again_po == "yes":
        po()
    elif try_again_po == "no":
        choose_a_date()
    else:
        print("Invalid input, Warrior!\n")
        po_no_chen()

def po_alone():
    print("You decide to handle your own tasks. Po respects your decision and wishes you luck. Unfortunately, without your help, Po is deafeated against Tai Lung and China is destroyed. GAME OVER!!!")
    try_again_po = input("Do you want to try again? ")
    if try_again_po == "yes":
        po()
    elif try_again_po == "no":
        choose_a_date()
    else:
        print("Invalid input, Warrior!\n")
        po_alone()
def gru():
    print('''
                                                                                                              
                                                  ::-                                               
                                                  ::=                                               
                                                  ::::-                                             
                          ==*##                 -==-+--                                             
                     +*+::+**+**==              ===**:-=                                            
                   #*++=--=+-+=+--===*           --:---=                                            
                   :-==-+*+-:::---==+*#             =----=                                          
                  ::::::==------==+**#%#####%%#####%@  +++#%%@                                      
                  -::::-----++--=+**%@#*%%#%%#####%%###@##%%%%%                                     
                 *#---*%%#*=---+**@#**#@@@@%####%%%###%%%%%%%%%%%                                   
             ******#+=--===**+#@#*#%%%#%%%####%%%%%######%%%%%%%%%%                                 
          ##**#++*##*%**%**#%*+#%####*#@@%##%%%%%%%%%#%%%%%%%%%%%%%%                                
        #*##%##%%%#*+#++%*+*%%%%##%***#%%%#%%%%%%%%%%%%%%%%%%%%%%%%%%                               
      ####*##%*++##%#*%%**%#**%%#%#####%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                               
     ############@%###%@##%###%%@%#****%%%%%%%%%%%%%@@%%%%%%%%%%%%%%                                
     ###%%###*+++%###%%#*%%%%%###%#%%%%%%%%%%%%%%%%#                                                
     ###%%####*+*%#####*+########%*****%%%%%%%%%%%##                                                
     ##%%%####***%#####=*########%%@@@@@%%%%%%%%%%#                                                 
     ##%%####*+++%####*-########%%*+*+*%%%%%%%%%%%#                                                 
     ##%%#*###%%%%####++########%%%@@%%%%%%%%%%%%#                                                  
     ##%%#*##*++*%###*=########%%%*****%%%%%%%%%%#                                                  
     ##%%%#######@%###=#######%%%%###**%%%%%%%%%#                                                   
     ##%%%####++*@%##*+######%%%%%##%##%%%%%%%%%#                                                   
     ##%%%##%#*+*@%%#**######%%%%%*+***%%%%%%%%#                                                    
     ###%%####%%%@%%%**#####%%%%%%%@@@@%%%%%%%##                                                    
      ##%%%###+++%@%%**#####%%%%%%*****#%%%%%%#                                                     
      ##%%@%##***%@%%**#%%##%%%%%%%@%%%%%%%%%%#                                                     
      ##%%%@##***%@%%##%%%%%%%%%%%**+++#%%%%%#                                                      
      %##%%@%#+++#@%%#*#%%%%%%%%%%@@@@@%%%%%%#                                                      
       #%%%@@#%%%@@@%#*%%%%%%%%%%#+++++#%%%%#                                                       
       ##%%@@#+++*%@%#*#%%%%%%%%%%%%%%%%%%%#                                                        
       %#%%@@%####%@%%*#%%%%%%%%%%%%%%%%%%%#                                                        
        #%%%@@+**#%@%%+#%%%%%%%%%%%%%%%%%%#                                                         
        %%%%@@*++*%@%%**%%%%%%%%%%%%%%%%%##                                                         
         %%%@@###%%%%%+*#%%%%%%%%%%%%%%%##                                                          
         +==# *++++#%%%%@@@@@%%%%%%%##                                                              
     :::--=+# %##%%@%%%%%@@@@%%%%%%%#%                                                              
     -:-===*  +++++ %%%%%@@@@%%%%%%##                                                               
      --*==   @%%%@  %%%%%@@@%%%%%%#                                                                
              +++++  %%%%%@@@%%%%%##                                                                
                      %%%%@@@@%%%%##                                                                
                      %%%%%@@@%%%%#                                                                 
                       %%%%@@@%%%%#                                                                 
                        %%%@@@%%%%#                                                                 
                        %%%%@@%%%#                                                                  
                        %%%%@@%%%#                                                                  
                         %%%@@%%%#                                                                  
                         %%%%%%%%%                                                                  
                         %%%%%%%%#                                                                  
                         %%%%%%%%                                                                   
                          #%%%%%%                                                                   
                          #%%%%%%                                                                   
                          %%%%%%%                                                                   
                          %%%%%%%                                                                   
                          ##%%%%%                                                                   
                          %%%%%%%                                                                   
                           %%@%%%                                                                   
                          ##%##%                                                                    
                        ##%%%%%#*                                                                   
                     #####%%%%###*+                                                                 
                    %%%%        ###*                                                                
          ''')
    print("I am Gru, do you want to rob the moon with me?")
    gru_choice = input("1. Yes, let's rob the moon.\n2. No, I have other plans.\nMake your choice: ")
    if gru_choice == "1":
        gru_help()
    elif gru_choice == "2":
        gru_no_help()
    else:
        print("Invalid input, Minion!\n")
        gru()
def gru_help():
    print("Gru is excited to have your help. Your first mission is to steal the shrink ray from Victor. Do you want to break into Victor's lab or disguise yourselves to infiltrate it?")
    gru_choice2 = input("1. Break into the lab.\n2. Disguise and infiltrate.\nMake your choice: ")
    if gru_choice2 == "1":
        gru_break_in()
    elif gru_choice2 == "2":
        gru_disguise()
    else:
        print("Invalid input, Minion!\n")
        gru_help()
def gru_break_in():
    print("You decide to break into Victor's lab. The security is tight, and you must avoid detection. Do you disable the security system or sneak past the guards?")
    gru_choice3 = input("1. Disable the security system.\n2. Sneak past the guards.\nMake your choice: ")
    if gru_choice3 == "1":
        gru_disable_security()
    elif gru_choice3 == "2":
        gru_sneak_past()
    else:
        print("Invalid input, Minion!\n")
        gru_break_in()
def gru_disable_security():
    print("You successfully disable the security system and steal the shrink ray from Victor. Now it's time to fly to the moon. Do you prepare the rocket yourself or ask Dr. Nefario for help?")
    gru_choice4 = input("1. Prepare the rocket yourself.\n2. Ask Dr. Nefario for help.\nMake your choice: ")
    if gru_choice4 == "1":
        gru_prepare_rocket()
    elif gru_choice4 == "2":
        gru_ask_nefario()
    else:
        print("Invalid input, Minion!\n")
        gru_disable_security()
def gru_sneak_past():
    print("You try to sneak past the guards, but you get caught and they KILL you. GAME OVER!!!")
    try_again_gru = input("Do you want to try again? ")
    if try_again_gru == "yes":
        gru()
    elif try_again_gru == "no":
        choose_a_date()
    else:
        print("Invalid input, Minion!\n")
        gru_sneak_past()
def gru_disguise():
    print("You disguise yourselves and manage to infiltrate Victor's lab. However, you encounter Victor. Do you confront him directly or use a distraction?")
    gru_choice3 = input("1. Confront him directly.\n2. Use a distraction.\nMake your choice: ")
    if gru_choice3 == "1":
        gru_confront_victor()
    elif gru_choice3 == "2":
        gru_distraction()
    else:
        print("Invalid input, Minion!\n")
        gru_disguise()
def gru_confront_victor():
    print("You confront Victor directly, but he overpowers you and you DIE. GAME OVER!!!")
    try_again_gru = input("Do you want to try again? ")
    if try_again_gru == "yes":
        gru()
    elif try_again_gru == "no":
        choose_a_date()
    else:
        print("Invalid input, Minion!\n")
        gru_confront_victor()
def gru_distraction():
    print("You use a distraction to steal the shrink ray from Victor. Now it's time to fly to the moon. Do you prepare the rocket yourself or ask Dr. Nefario for help?")
    gru_choice4 = input("1. Prepare the rocket yourself.\n2. Ask Dr. Nefario for help.\nMake your choice: ")
    if gru_choice4 == "1":
        gru_prepare_rocket()
    elif gru_choice4 == "2":
        gru_ask_nefario()
    else:
        print("Invalid input, Minion!\n")
        gru_distraction()
def gru_prepare_rocket():
    print("You decide to prepare the rocket yourself. Unfortunately, you make a critical error, and the rocket explodes during launch, KILLING you. GAME OVER!!!")
    try_again_gru = input("Do you want to try again? ")
    if try_again_gru == "yes":
        gru()
    elif try_again_gru == "no":
        choose_a_date()
    else:
        print("Invalid input, Minion!\n")
        gru_prepare_rocket()
def gru_ask_nefario():
    print("Dr. Nefario helps you prepare the rocket. The rocket is ready, and you launch it towards the moon. Do you land on the moon and shrink it or shrink it from space?")
    gru_choice5 = input("1. Land on the moon.\n2. Shrink it from space.\nMake your choice: ")
    if gru_choice5 == "1":
        gru_land_on_moon()
    elif gru_choice5 == "2":
        gru_shrink_from_space()
    else:
        print("Invalid input, Minion!\n")
        gru_ask_nefario()
def gru_land_on_moon():
    print("You land on the moon and use the shrink ray to shrink it. You successfully stealing the moon. You and Gru become the number #1 and #2 villians in the whole WORLD. YOU WIN!!! That's your date.")
    the_end_gru = input("Do you want to go back to the menu? ")
    if the_end_gru == "yes":
        choose_a_date()
    elif the_end_gru == "no":
        print("Bye Bye 🤫🧏‍!!!")
    else:
        print("Invalid input, Minion!\n")
        gru_land_on_moon()
def gru_shrink_from_space():
    print("You try to shrink the moon from space, but the shrink ray malfunctions and explodes, you and Gru DIED. GAME OVER!!!")
    try_again_gru = input("Do you want to try again? ")
    if try_again_gru == "yes":
        gru()
    elif try_again_gru == "no":
        choose_a_date()
    else:
        print("Invalid input, Minion!\n")
        gru_shrink_from_space()
def gru_no_help():
    print("You decide not to help Gru. Without your assistance, Gru's plan fails, and he ends up in jail. GAME OVER!!!")
    try_again_gru = input("Do you want to try again? ")
    if try_again_gru == "yes":
        gru()
    elif try_again_gru == "no":
        choose_a_date()
    else:
        print("Invalid input, Minion!\n")
        gru_no_help()
def senator_armstrong():
    print('''
                                      #%%%%%%%@@@@%%                                                
                                   @@%%%%@@@@@@@@@@@@%                                              
                                  %@@%@@@@@%%@@@%@@@@@%                                             
                                 %@@@@@%%*+=-:::-*@@@@%                                             
                                 @@@#*++==----::---*@@@@                                            
                                #@@%#*++===---------*@@%                                            
                                 @%###*+++===-------=%@@                                            
                                 %#####**++======---=#@@%                                           
                                 @######**+++++==---=+%@%*                                          
                                  %#%######*++=--=++=-+#+++                                         
                                  @%%%#*+**+++*%%###=**=+*++                                        
                                  %#%@@@@%**#%%%#**+#++==*++                                        
                                  %%##%%%%%*=+=======-+==++*                                        
                                  #%######%*==+#+======++++-=                                       
                                   ###%#%%%#+==+*##+====+#=---                                      
                                   ##*#%%%%%%##*+++*+===+-::::---                                   
                                    ##*%%%%%%%%#++*+*==++:::-:::::--                                
                                   ##%##%%%%%%@%#*+++++*-::--:--:::::--                             
                                   %@@%#%%%%#*++=-=++*=---:----:::::....:-                          
                                  %@@@@%##%##+**+++**-----==--::::........:-                        
                                 #@@@@@%%%%%%%%%%%%%%****+==----::::::......:-                      
                                %%@@@@@@%%%@%%%@@@@*=++*+==----------:------:::-                    
                               #%@@@@@@@@@%%%@@@%%+--=+===+--=======----:=++==-::::-                
                             ##%%@@@@@@@%%%%%%%%*=---+===++-==++==---:-=+-:-:.....::--=             
                          ##%%%%%@@@@@@%%%%%%%#-=---=+==+++==+++==---===++-:....:-----==            
                       ##%%%%%%%%@@@@@%%%%%#+=-=--=====++++==++======*+=::.............:-           
                     ##%%%%%%%%%%@@@@%##*+++=-==----===++++=++++++**+=--::...............:-         
                   #%%%%%%%%%%%%%@%%%*++++*+=====--======++=+*+++++===---:::..............:-        
                 ##%%%%%%%%%%%%#*###+++++*+++++++=--=====++=+*++++++==---:::..............:=        
               ###%%%%%%%%%%%##*+***+++++++++++++=++=--+==++*#****++++=---:::..............--       
               ##%%%%%%%%%%%#*#+=*****++++++==++=====+=++===+####**++++=---::::..::::........:      
              ####%%%%%###*+*#*==+++++++++++=====+==--===##++*#####**++++==--:----::::........:     
              ##########*+++**==*##*+++++++++++++++++--=**%%########***+++====--::::...........:    
              ########****##*+=*****##***+++++++++++++====*%%%%%%####**+++==-::...............-:    
              ########****#*+-+*###********++++++++++++++++*%%%%#####*+==---==--:::............:    
              **#######**##*==**##***********++++**##%######%@####**++++==--:::::...::..........    
              ***######*##*+=-*######***********+++++++*****%@@##%###*+==---:::--:::......:...:=+   
              *****#######*+=###############*****+++*##***#@@@%#####*+++====---::::...........+++   
              ******######*+*######%%%%%#####**%%%%%#%##%%%@@@#######*++===---::::......:::..=+++   
              **##***#####*=###*####%%%%%%%%%%%%%%%%%##*++*%%%#######*+++=----:--::.....:-:::===-   
              **###****###*++#%##*##%%%%%%%%%%%%%%*+=++++++%%%@#%%%###**+==-------:....::--::::::=  
              ###%%#**####*+**#%%########%%%%%%@@%#*+======%%%%%#######*++==--===--::::..:-::::::-  
             **#%%%%**###*+*#*##%%%%####%%%%#***+++*#@%*+++%%%%@%%%#####*++=====+==-:::..........:= 
             *#%%%%%#**##*+*###****#%%####%##**++++***+*#*#@@@@@@#*#######*++==+++=--::..........:- 
              *#%%%@%**##*+######****####%%#+=======++=+++#@%%@@@@%**#######*++++==-::::..........- 
             ***###%%#*##*+##+#%%%###***#####%%%%%#**###*#%@@@@@@@@@#**######*+++==--::..........:-=
             ***##%#%%*##**######%%%##************#*******#@@@@@@@@@@@#**######*++=--::..........::-
            ######%%%%###**#####**#%%%%#*++++***********++%%@@@@@@@@@@@@%#**###*+==---:::.......:::-
           **#####%%%%###**#######*+*#%%%%#*++========+**#%%@@@@@@@@@@@@@@@#**#*===++++=-.....::.::-
           ###%%%%%%%%%##*+*###%####+++**#%%%##*++*****+=+%%%%@@@@@@@@@@@@@%*#*++=+*+==-::.::::.::--
          ###%%%%%%%%%%###**####%%###*++=+**###*+++++====*%%%%%%%@@@@@@@@@%*##*++******+=::::...:--=
         *####%%%%%%%%%%#***##**##%##***+===+**+++++===--#%%%%%%%@@@@@@@@@#######**+==-::::...:::-==
        ###%%%%%%%%%%%%%%***#######%#****#*=======+====-=#%%%%%@@@@@@@@@@%#####*+==----:::::::::-== 
        *##%%%%%%%%%%%@@@%*######**#%#*+++*##*+==========*%%@@@@@@@@@@@@@#####*++==--------::..:==  
       +*##%%%%%%%%%%%@@@%*#####*#**##**+++===+++=-----=-=%%%%@@@@@@@@@@%#####*+==-----::::::::-=   
       *###%%%%%%%%%%%%@@%*####**##******+++=======----===#@@@@@@@@@@@@@@*##*+=---:::::::-------=   
       ###%%%%%%%%%%%%%%@%*##########*****+++++===+**##%###@@@@@@@@@@@@@@**+==--:::::-----===--==   
      %%%%%%%%%%%%%%%%%@@%*###########**##%%%@@%%%%%%%%@%%%%%@@@@@@@@@@@*#**++==----------===++++   
      ##%%%%%%%%%%%%%@@@@@%%#%%%%%%%%%%%@%%@@%%%%%%%%%%%@%%%%%@@@@@@@@@@*##**+===---------===++*    
      ###%%%%%%%%%%%@@@@@@@@@@%%#++**%%%@%%@%%%%%%%%%%%@@%%@%@@@@@@@@@@@*###*++=---:---=----=++     
      ####%%%%%%%%@@@@@@@@@@@@%@@%%#*#%%@@%@%%@@@@@@%%%%%###*%##@@@@@@@@@*##****+++++*#%%%@@%#+     
      *##%%%%%%%%@@@@@@@@@@@@@####**%@@@@@@@@%%%%%%%%%%%%###*#%%%@@@@@@@@%####==+===++++#*%@%*#     
      *###%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%##***###@@@@@@@@@##*+=====++++**%%%%       
       #%%%%%%%%@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%#%*#@@@@@@@@@%#*+======++++*##          
       #%%%%@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%####*%@@@@@@@@%#*+======+++*#            
       #%%%%@@@@@@@@@@ %%@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%####@@@@@@@@%##*++=====++++             
       #%%%@@@@@@@@    #%@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@***+=======++++             
      ##%%@@@@@@@@     #%@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%##@@@@@@@#+**++========+*              
      #%%%%%@@@@@      #%@@@@@@@@@@@@@@@@@%%%%%%%@@@@%%%%%%%###@@@@@%++++++++=======+*              
     #%%%@@@@@@@@      %%@@@@@@@@@@@@@@@@%%@@@@@@@%%%%%%%%%%%%#@@@%*+=+++++++========+              
    %%%%%@@@@@@@       #%@@@@@@@@@@@@@@@@@@@@@%%%@@%%%%%%%%###%@@@#+++*##*+++=====+=++              
   #%%%%@@@@@@@@       #@@@@@@@@@@@@@@@@@@@%@@@@%%%%%%%%%####@@@@%#****%%#*++++++++=++*             
  *#%%%%@@@@@@@@       #@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%@@@@%***#@%%%#+=++++++++++             
  *%%%%%@@@@@@@       ##@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%@@@%%**#@@@@%*+++*****+***             
 #%%%%%%@@@@@@        *%@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%@@@%%%#%@@@@#*++%***#*#***             
##%@%%%@@@@@@        *#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%@@@%%%%@@@@#**##**##*%#**             
*#%@%%@@@@@@         *%@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%@@@%#%%@@@@#**######%%**              
#%%@%%@@@@           #%@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%@@@@%@@@@@#**%###%##@%#*              
#%@@%%@@@@           #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%@@@@@@@@@#%%%%%%@%@@%##               
#%@%%%@@@@           #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%@@@@@@@@@@@%%%%@@@@@@@%                
#%@%%@@@@@          #%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@%%%%#                   
#%@@@@@@@@@%        #%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%@@@@@@@@@@@@@@#######                   
*%@@@@@@@@@@@       #%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%@@@@@@@@@@@@@@%#######                   
 #%@@%%%@@@         #%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%@@@@@@@@@@@@@@@########                   
 *#%@%              #%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@%#########                  
   #%               ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#########                  
                    ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#########                  
                     #%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##########                  
                     *%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##########                  
                     *#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#########                  
                     *#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%########                  
                      *%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%#######                  
                      *#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%######                  
                       #%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%######                  
                       #%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%######                  
                        #%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%#####                  
                        *%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%#####                  
                         #%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%#####                  
                         *%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%#####                  
                          #%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%#####                  
                          *%@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@%%%%%%############                 
                          *%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%###                 
                           #%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%###############                
                           *%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%###############               
                            #%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%###############               
                            *%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%################              
                            +#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%###############              
                             *%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%##############             
                             *%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%############             
                             *#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%###########             
                             *#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%############            
                              #%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%###########            
                              #%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%##########            
                              ##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%##########           
                               #%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%#########           
                               #%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%#######           
                                %@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@%%%%%%%%%%######           
                                %@@@@@@@@@@@@@@@@@@@@@@@@@  %@@@@@@@@@@@@@%%%%%%%%%%####%           
                                 @@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@%%%%%%%%%%%%%#            
                                 @@@@@@@@@@@@@@@@@@@@@@@@    %@@@@@@@@@@@@@%%%%%%%%%%%%%            
                                  @@@@@@@@@@@@@@@@@@@@@@@    %@@@@@@@@%@@@@%%%%%%%%%%%%%            
                                  @@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@%%@@@%%%%%%%%%%%%%            
                                  @@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@%%%%%%%%%%%%%%%%%%%           
                                  @@@@@@@@@@@@@@@@@@@@@@       @@@@@@@%%%%%%%%%%%%%%%%%%%           
                                  @@@@@@@@@@@@@@@@@@@@@@       @@@@@@@%%%#####%%%%%%%%%%%           
                                  @@@@@@@@@@@@@@@@@@@@@@       @@@@@@@%##########%%%%%%%%           
                                  @@@@@@@@@@@@@@@@@@@@@@        @@@@@@@%##########%%%%%%            
                                  %@@@@@@@@@@@@@@@@@@@@@        @@@@@@@@@%#########%%%%%            
                                  @@@@@@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@%#######%%%%            
                                   @@@@@@@@@@@@@@@@@@@@@         @@@@@@@@@@@@@########%             
                                  @@@@@@@@@@@@@@@@@@@@@@         @@@@@@@@@@@@%%#######%             
                                 @@@@@@@@@@@@@@@@@@@@@@@          @@@@@%%%%@%%%%%%####%             
                                 @@@@@@@@@@@@@@@@@@@@@@@           @@@@%%%%%######%%##%             
                                @@@@@@@@@@@@@@@@@@@@@@@@@           @@@@%%%%#######%%#%             
                                @@@@@@@@@@@@@@@@@@@@@@@@@          @@@@@%%%%#######%%%%             
                               @@@@@@@@@@@@@@@@@@@@@@@@@@         @@@@@@%%%%#######%%%              
                               @@@@@@@*+@@@@@@@@@@@@@@@@@         @@@@@@@@@@@%%@%%%%%%              
                             @@@@@@@@@@@@+=*@@@@@@@@@@@@@        @@@@@@@@@@%*=+%%@@%%%              
                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@         @@@@@@@@@@%%%%%@%@@@@              
                         @@@@@@@#=..-#@@@@@@@@@@@@@@@@           @@@@@@@@@%%%%%%%%%@@@              
                @@@@@@@@@@@@@@@#*+:=%@@@@@@@@@@@@@@@@@            @@@@@@@%%%%%%%%%%@@               
               @%%@@%##%@@@@@#=-=*%@@@@@@@@@@@@@@@@@@               @@@@%%%#-+%%%%%%                
              @@@@@@@@@@%*++##%@@@@@@@@@@@@                        @@@@@%%%@#=#%%%%%%               
               @@@@@@@@@@@@@@@@@@@@@@@@                            @%@@@@@@@@@@@@@@@@               
                                                                   %@@@@@@@@@@@@@@@@@               
          ''')
    print("I am Senator Armstrong, do you like nano machines son?")
    armstrong_choice = input("1. Yes, I want to learn about nano machines.\n2. No, I'm not interested.\nMake your choice: ")
    if armstrong_choice == "1":
        armstrong_learn()
    elif armstrong_choice == "2":
        armstrong_no_learn()
    else:
        print("Invalid input, Son!\n")
        senator_armstrong()
def armstrong_learn():
    print("Senator Armstrong is pleased with your interest. He offers you a chance to join his cause and learn about the power of nano machines. Do you accept his offer?")
    armstrong_choice2 = input("1. Yes, I accept.\n2. No, I refuse.\nMake your choice: ")
    if armstrong_choice2 == "1":
        armstrong_accept()
    elif armstrong_choice2 == "2":
        armstrong_refuse()
    else:
        print("Invalid input, Son!\n")
        armstrong_learn()
def armstrong_accept():
    print("You accept Armstrong's offer. He injects you with nano machines, and you feel a surge of power. With your new abilities, Armstrong assigns you to eliminate all rebels opposing his rule in the U.S. Do you carry out the mission?")
    armstrong_choice3 = input("1. Yes, I will eliminate the rebels.\n2. No, I can't do this.\nMake your choice: ")
    if armstrong_choice3 == "1":
        eliminate_rebels()
    elif armstrong_choice3 == "2":
        refuse_mission()
    else:
        print("Invalid input, Son!\n")
        armstrong_accept()
def eliminate_rebels():
    print("You use your enhanced abilities to eliminate all rebels opposing Armstrong's rule. The resistance is fierce, but you and Armstrong prevail. America falls under Armstrong's complete control. Now, Armstrong asks you to help him take over the world and spread the nano machines. Do you agree to his plan?")
    armstrong_choice4 = input("1. Yes, let's take over the world.\n2. No, this is going too far.\nMake your choice: ")
    if armstrong_choice4 == "1":
        world_domination()
    elif armstrong_choice4 == "2":
        refuse_world_domination()
    else:
        print("Invalid input, Son!\n")
        eliminate_rebels()
def refuse_mission():
    print("You refuse to carry out the mission. Armstrong sees you as a traitor and decides to eliminate you. YOU DIED. GAME OVER!!!")
    try_again_armstrong = input("Do you want to try again? ")
    if try_again_armstrong.lower() == "yes":
        senator_armstrong()
    elif try_again_armstrong.lower() == "no":
        choose_a_date()
    else:
        print("Invalid input, Son!\n")
        refuse_mission()
def refuse_world_domination():
    print("You refuse to help Armstrong take over the world. Armstrong sees your hesitation as a threat and decides to eliminate you. YOU DIED. GAME OVER!!!")
    try_again_armstrong = input("Do you want to try again? ")
    if try_again_armstrong.lower() == "yes":
        senator_armstrong()
    elif try_again_armstrong.lower() == "no":
        choose_a_date()
    else:
        print("Invalid input, Son!\n")
        refuse_world_domination()
def armstrong_no_learn():
    print("You decide not to learn about nano machines. Armstrong sees you as a weakling and decides to eliminate you. YOU DIED. GAME OVER!!!")
    try_again_armstrong = input("Do you want to try again? ")
    if try_again_armstrong.lower() == "yes":
        senator_armstrong()
    elif try_again_armstrong.lower() == "no":
        choose_a_date()
    else:
        print("Invalid input, Son!\n")
        armstrong_no_learn()
def armstrong_refuse():
    print("You refuse Armstrong's offer. He sees you as a threat and decides to eliminate you. YOU DIED. GAME OVER!!!")
    try_again_armstrong = input("Do you want to try again? ")
    if try_again_armstrong.lower() == "yes":
        senator_armstrong()
    elif try_again_armstrong.lower() == "no":
        choose_a_date()
    else:
        print("Invalid input, Son!\n")
        armstrong_refuse()
def world_domination():
    print("You agree to Armstrong's plan to take over the world. With the power of nano machines, you and Armstrong conquer nation after nation, spreading his rule and the influence of nano machines.")
    print("Now, Armstrong sends you on a critical mission to destroy Russia, one of the last strongholds resisting his rule. Do you infiltrate their defenses or launch a full-scale attack?")
    armstrong_choice5 = input("1. Infiltrate their defenses.\n2. Launch a full-scale attack.\nMake your choice: ")
    if armstrong_choice5 == "1":
        infiltrate_russia()
    elif armstrong_choice5 == "2":
        full_scale_attack()
    else:
        print("Invalid input, Son!\n")
        world_domination()
def infiltrate_russia():
    print("You decide to infiltrate Russia's defenses. Using your nano machine abilities, you successfully bypass their security and sabotage their military infrastructure. Russia falls, and Armstrong's rule spreads further.")
    print("Armstrong now controls the entire world, and you are his right hand. Together, you enforce a new order with the power of nano machines. YOU WIN!!!")
    the_end_armstrong = input("Do you want to go back to the menu? ")
    if the_end_armstrong.lower() == "yes":
        choose_a_date()
    elif the_end_armstrong.lower() == "no":
        print("Bye Bye 🤫🧏‍!!!")
    else:
        print("Invalid input, Son!\n")
        infiltrate_russia()
def full_scale_attack():
    print("You launch a full-scale attack on Russia. The battle is intense and devastating. Despite your abilities, the Russian forces are strong and well-prepared.")
    print("In the heat of battle, you are overwhelmed and killed. Armstrong's forces retreat, and his plan for world domination is halted. YOU DIED. GAME OVER!!!")
    try_again_armstrong = input("Do you want to try again? ")
    if try_again_armstrong.lower() == "yes":
        senator_armstrong()
    elif try_again_armstrong.lower() == "no":
        choose_a_date()
    else:
        print("Invalid input, Son!\n")
        full_scale_attack()
def doom_guy():
    print('''
                                                                         =++++                      
                                                                       =--=++++*                    
                                                                       +:*###++*                    
                                            .::-------                 =+%@@%****                   
                                         ::===========++=              ++%%%%##*                    
                                        :-=+*###*****+++=-=             *%+#*#%%                    
                                      ..:=*#%%%%%%%%##*+=-::             *##+=                      
                                     ::-=+*+#%%##*****=--==--       -=+*+#*=-                       
                                    :--=####*+===+=------**=-*     ++***+==--                       
                                    -==###%%##**+=====+**#*==-     -%###+++=                        
                                    ==*#%###%%%##***#*=+***=--    +*%#*+                            
                                    :+*#%%###%#####**+==**=-+=--  *#*+++                            
                                   .-*+##%%######++++==**+-=#++-- *%#*==                            
                                  ::-##+##%#%###*+++=*#*=:-*#*+==#%@%*===                           
                      .*%%*#**#-=--+*%@####%%%%##*++###+==##*++###%%**##*=                          
                     .#%@@@%%#++***##%@@%#%%%%%%###******#%*++#***%%@@#+++==#+                      
                  =:-+*%@@@%*=+*###%%@@@@%%%@%%%#****#@##@@#*#***#%%@%++++*+++=++                   
                 =+*==*%%%%%#*+**#*#%%@@@@%%@%%%%##**#%#%@@#####%%%%%*+=++++++#+=                   
                =::=+**#@%%%%###***##%%@@@@%@%%%%%##*###%%####%%%%%%#===+++++=-+#++                 
               *+*+***##@@%%%%##***###%@@@@@@@@@%%%%%%%%###**##%%%%%**=++**+++==+**                 
              *###*#####%@%%%%##**#*################*#####**##%%%%%#******+==+=-=+*=                
              =+#*#######%%#%%#******#%##*++++++++==+****####%%%%@%#*******#*=--====                
              =+**#***###%@%%%###**+++++*##****++++**#***++*+#%%@%#*****++++++=+++*=                
               +*#####*+##%%%%###***+++=+++++++++++++++*+====*#%%#*#*****++++*+++++*                
               #*#######%%@@%%######*++=++++++++++===**#*=----*%%*##*******++*+===+**               
               %#+*#####%%@%%######***++*********++++**++=----=*%@###**********++=+=                
                 **######%@@%%#######**+++++++++++++==+**+=--+++*%%###**#######*++##*               
                   ##*####%%%%%######*****####*#*++++++++==-=+++*%@%%%%#%#+===+*+=+##*              
                   ::+*****%%%%###%%###%%%######*###***++++==*++*#%@%###%*++++*#*++*+               
                   .-+*****%%%%%%%%%%%%###*******+**+*######***++*#@%#**++**+**+#+=+=               
                 -..=******%%########%%##********++==+*#**++*+===+#%%##***++==++*+++=-              
                =*--+*****#%%###%%%##%%%%#**#******+*#####*+==-=+=#@%##*+=-:::::=**++==             
              -=*#+=+******########%%%%%%%###****##*%#*+++++#**+=++%###*+=-:.::::+#=+++++           
            .:+###**********#@%#*#%%%%#***#+=====+++==+*###+-===+=*+ #***+=-::::=*++++++++          
          ::-###%#**##*****#%@ ###%%####%%##***+**+**+==**##+-=++*#    *****+==+#**+***+-=          
         :-=##%%%%#**#*****#@% %%%%%%###%###+===+=+=+#*+==+**+++++       **####*+#####+=+**#*++     
        :-=##%%%%%%%%######@%  #%%%%%#%%#####*++++*+=+**+**%#+*+++       ##%%%%%%###*+===#*##*+++   
        =+#%%%%%%%%%%%%%%%% ##%%%%%%%%%##%#*#**+**++**+=++******++       *#%%%%#####%**++#**#*++++  
       ++##%%%%%%%%%%%%%%%%*###%%#%%%###%#**+++==++==***++++=+++*#*+=    **#%%%%##***%*+++*#@%++*+++
      %###%%%%%%%%%%%%%%%####%%%%###%%%%####%######*+==+#%%#=-+****+***   *#%%%%%%#****++#*#@@*+**++
     *+###%%%%%%%%###### %##%###%%##%%%%#%%%*+++==-*##*+**#+--*%*+=*+**    ##%%%%#**###**%+#@*+++*%*
    #*###%%#####%%####   ##%#%##**####%%%###**###*+====****==*#*+*++***#    *%%%%####%#++#+#@**+++++
    *###%%%%%#####*##    ##%%%%#*#%###*#########*#+***+*++-+**%*+++***##    ##%%%%#*##*++++#@%*+++==
   #*###%#%%##%%#**      #%%%%####%%##*%%#*#%##**++##*++++-=*%%#******#      *####*###**#**#%%*++===
   *####%%#%#%#*         %%%%%%#%@@%%%%%%%**###***+#****####%@%%#****##      *#%%####%#%**#*%%*++===
  **##*%%%%%####           %@@@@@@%%%%%%%%%%###*****#**++****#%@@%@@#         ##%@%#*#*+=+*#@%*+++==
 *+*##%%%%##%%%#            ##%%%%%#*##%#%%%%###*************+****##       %##%%%%%##**#*=*#%#*+++==
#*****#%#%%%#%%#            ###%%%%#*#%###%%%###**+******+#*+***++*#*     %%%%%%%%##*###**##%@@+++= 
 #***###%%%%%%%#           **#*#%#%%*#%###%%%###***+***#**#**#%+++===+   %%%##%%%%#**#*+*+++*%@=-== 
  ##**##%%#%%%%#          **#**+#%#*#####%%%#####***++*****##*##*+==+==  %%#%%%%%%%#+%*+#***+#%+++  
  =+#**#%%%  %%#        **###**++%*#####%%%%#####******#****##*%*+=-==+*@@%%%@%%%%##*##***+#+**     
  ###*+%%@%@%%%#        #####**+*#*######%%%%#######*###****#%#%#*=-==+# @%%%  ####*%%##%#%#*       
   *##*#@@@%%%%        ######****##*####%%@%%%######*#%###**%##%##+=-==** %    %##**@#*%#*%*=       
    #%##%%@%%%#        #####******#######%@%%%%######%%%##*#%#%%##*+===+**     #%#*%@%#%@*#%+       
      ##%%#           **####***#*##*#####%%@%%%%%%%%%%%%%##%%%%%##*+====*+     ##**@@%#%%#*         
                      +*###****#**#*#####%%%%%%%%%@%@@%%%%##%%%%##*++==+*++    %%##@%#%%#*          
                     +*####***+++*#*#*####%%%%@@@@%@%%%%%%%%%%%%#**++==+#*++   %##%%##%#*           
                     +##%##****++*#*#*######%%    %%%%%%%%%%%%%%#**++==+*+=+       #                
                    +*#####******#%**##*###%%      %%%%@%%%%%%%%##**++++*===                        
                    +*##%%##*****+########%%        %%%%%%%%%%%%%%#*+++++====                       
                    *###%%##*****+++**####%          %%@@@%%%%%###%***+++====                       
                     *###%%%##***+++**####             %%%%%%%%#**###*++++==                        
                     *#%%%%%##*******####               %%%%%%%##*####***++=                        
                    =+##%%%%%###*****##                  %%%%%%%##%%%#*##*++=                       
                   +###%###***%##**####                   #%@%%%%%%%#*++++**+                       
                   +*=*##**+++*%######                     %%%@%%@%#**++=++===                      
                  #++*####***+***#####                     #%%%%%%%%#***#+====                      
                  +*###*****++++**###*                     *%%%%%%%#****+++++=                      
                  +*######*********###                      #%%%%%%%#****++++==                     
                  **#######*******###                        %%%%%%%%##****++=+#                    
                 #**######***+****#                           #%%%%%%%#*****+==:                    
               #@*#*####%##******##                           *#%%%%%%##***++==*###                 
              %**%##%%###*******##*#%%                      %%*#%%%%%###****%*=+++*                 
              ++*%##########+**######                        *#%%@%%%#%%***+++*+++=                 
              **#%%##%%##**########%##                      *%%%%@@%%%%####*++****+*                
             %##%%%%##%%#*#####**###%%                     #%%%%%#%%%%%%%##*+*#*##+##               
              *%%#%%%%########%##*##%%@                    @%%%%%%%%%%%%%###*%#=+#+                 
              *%*#%%%%%#%%%##%%%%####                        %%%%%@@@%#%%%%%#++++**                 
              %**%%%%##########%%##%#                        %%%%@@@%%%######***++*                 
              ###%%%%%#########%%##                           %%%@@%%%%%%###****++*                 
              -+#%%%%%###%#####%##                              %%@@%%%%%%###****++-                
              +*#%%%######*######                                %%%%%%%%####****+++                
             ==*#%%%%###########*                                 #%%%%%%%####+****+                
             **#%%%%%###########                                  #%%%%%%%####****+++               
            +++#%%%%###########                                    #%%%%%%%####***++=+              
            ++*#%%%############                                    *#%%%%%%%###*+++++=              
            ++#%%%%##**########*                                   #%%%%%%%%###*****+==             
           ++***###%###########                                    #%%%%%%%%%##***++++++            
           *#%%%%%##****######*                                     #%%%%%%########**+++            
          #*##########*#*#####*                                    ##%@@%%%%%####%#*#%*+*           
         %%=*%#*#%####***##%%%#                                     #%@@%%%%%%%#%####*+==           
         =+++++++*******######*                                     %%%%######********++==          
        ++=++++++++*****######                                      %%%%####*******+++++===         
        +*#######*****#########                                     **#%%##%%#####*****++++         
        *##*****+******########                                     %%%%######%%#**++++==+++        
       %######****#**#***######                                     %%%%%#####%%###***+++#***       
       %#####*****#**#**##*                                           %###%%%%%%##*+++++++#*#       
       %########*##**#*#*                                                 %%%#%%#*********#         
          ''')
    print("Kill Demons?")
    
choose_a_date()
