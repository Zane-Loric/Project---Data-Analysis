#Append module
File_temp = [] #Temp file to add the data
Roll_N = [] 
Strg_Marks1 = []
Rank_HOl = []

Num_dat2 = int(input("Enter the number of data to be inserted in the data resource: "))
for i in range (1,Num_dat2+1):
    Name_1  = input("Name: ")
    File_temp.append(Name_1)
    Roll_No = input("Entrance Roll no: ")
    Roll_N.append(Roll_No)
    Obtained_Marks = int(input("Enter the successive marks: "))
    Strg_Marks1.append(Obtained_Marks)
    RankI = int(input("Rank: "))
    Rank_HOl.append(RankI)
Input_A = input("Do u want to save these changes?? ")
if Input_A in []:
    ###### addding data to the external file under dev 
    print("Data has been added! ")
elif Input_A in []:
    Roll_N.clear()
    File_temp.clear()
    Strg_Marks1.clear()
    Rank_HOl.clear()





