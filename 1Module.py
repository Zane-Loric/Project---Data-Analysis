#Interface module -- User Visual --
pass_set = 9842
kl = 9824
pp = 12 
Marks = 80    
#under dev
User_Input1 = input("Would you like to view the data?").upper()

if User_Input1 in ["VIEW","SEE","CHECK","YES"]:
    User_Input2 = int(input("Please Enter your Entrance Roll.No: "))
    #if User_input2 in kl
    if User_Input2 == kl:     #Kl be any type of data file where data is kept
        if(User_Input2>80):
            print(f"Congratulation🎉 for having scolorship for achieving {kl} and securing {pp} rank in ****** You are now eligible for admission!")
        elif(User_Input2<80 and User_Input2>60):
            print(f"Congratulation achieving {kl} and securing {Marks:>3}th rank in ****** You are now eligible for admission!")
        else:
            print("Better Luck next time(Better prompt later ):: ")
            

        
    pass
elif User_Input1 in ["YES","CHANGE",]:
    Ask_Valid = int("Please Enter the passcode to proceed: ")
    if(Ask_Valid == pass_set):
       pass