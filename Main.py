#Interface module -- User Visual --
#module1
Code_1 = 121212
E_roll = 9842    
_Marks = 80
Rank_ = 12
#under dev




User_Input1 = input("").upper()

if User_Input1 in ["VIEW","SEE","CHECK","YES"]:
    User_Input2 = int(input("Please Enter your Entrance Roll.No: "))
    #if User_input2 in kl
    if User_Input2 == E_roll:     #Kl be any type of data file where data is kept
        if(User_Input2>80):
            print(f"Congratulation🎉 for having scolorship for achieving {_Marks} and securing {Rank_} rank in ****** You are now eligible for admission!")
        elif(User_Input2<80 and User_Input2>60):
            print(f"Congratulation achieving {_Marks} and securing {Rank_:>3}th rank in ****** You are now eligible for admission!")
        else:
            print("Better Luck next time(Better prompt later ):: ")
        exit()
elif User_Input1 in ["YES","CHANGE",]:
    Ask_Valid = int("Please Enter the passcode to proceed: ")
    if(Ask_Valid == Code_1):
       pass
    #module 2 >>>>