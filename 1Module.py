#Interface module -- User Visual --
#module1
Code_1 = 121212
E_roll = 9842    
_Marks = 80
Rank_ = 12
#under dev
Decision1 = input('''
        1) Press View to check your performance in entrance exam
        2) Press Change to change the data 'Authorized personel only'
      ''').upper()
if Decision1 in ["VIEW","Check","SEE"]:
    User_Input1 = input("Would you like to view the data?").upper()
    if User_Input1 in ["YE","YES","Y","YUP"]:
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
    elif User_Input1 in ["YES","CHANGE"]:
        Ask_Valid = int("Please Enter the passcode to proceed: ")
        if(Ask_Valid == Code_1):
            pass
    else:
        print("Something went wrong!Try again later!")
    #module 2 >>>>