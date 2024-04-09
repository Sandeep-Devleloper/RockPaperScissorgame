import random

print("to exit (e)")
keys=["rock","paper","scissor"]
userScore=0
systemScore=0
turn=1
while turn<6:
    print("\nTurn:",turn)
    userChoice=input("select:Rock or paper or scissor:").lower()
    systemChoice=random.choice(keys)
    
    if userChoice in keys or userChoice== "e":
        
        if userChoice=="e":
            exit()
            
        elif userChoice=="rock":
            if keys[systemChoice]=="scissor":
                print("your choice ",userChoice,",system choice ",keys[systemChoice],"\n paper wraps Rock so you won a point 😁\n")
                userScore+=1
            elif keys[systemChoice]=="paper":
                print("your choice ",userChoice,",system choice ",keys[systemChoice],"\n paper wraps Rock so system won point  😏\n")
                systemScore+=1
            elif keys[systemChoice]==userChoice:
                print("your choice ",userChoice,",system choice ",keys[systemChoice],":Draw🫂")
            print(f"you:{userScore}\nsystem:{systemScore}")
            
        elif userChoice=="paper":
            if keys[systemChoice]=="rock":
                print("your choice ",userChoice,",system choice ",keys[systemChoice],"\n paper wraps Rock so you won a point 😁\n")
                userScore+=1
            elif keys[systemChoice]=="scissor":
                print("your choice ",userChoice,",system choice ",keys[systemChoice],"\n paper wraps Rock so system won point  😏\n")
                systemScore+=1
            elif keys[systemChoice]==userChoice:
                print("your choice ",userChoice,",system choice ",keys[systemChoice],":Draw🫂")
            print(f"you:{userScore}\nsystem:{systemScore}")
            
        elif userChoice=="scissor":
            if keys[systemChoice]=="paper":
                userScore+=1
                print("your choice ",userChoice,",system choice ",keys[systemChoice],"\n paper wraps Rock so you won a point  😁\n")
            elif keys[systemChoice]=="rock":
                systemScore+=1
                print("your choice ",userChoice,",system choice ",keys[systemChoice],"\n paper wraps Rock so system won point 😏\n")
            elif keys[systemChoice]==userChoice:
                print("your choice ",userChoice,",system choice ",keys[systemChoice],":Draw🫂")
            print(f"you:{userScore}\nsystem:{systemScore}")
    else:
        print("you are not allowed to usee other things")
    
    if turn==5:
        if userScore > systemScore:
            print(f"You won with {userScore - systemScore} points")
        elif systemScore > userScore:
            print(f"System won with {systemScore - userScore} points")
        else:
            print("Draw")
    turn+=1
    