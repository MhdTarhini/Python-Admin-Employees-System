def adminMenu():#Menu of admin
  print("\n"
        "1. Display Statistics\n"
        "2. Add an Employee \n"
        "3. Display all Employees \n"
        "4. Change Employee's Salary \n"
        "5. Remove Employee \n"
        "6. Raise Employee's Salary \n"
        "7. Exit")

def userMenu(): #Menu of normal employee
  print("\n1. Check my Salary \n"
        "2. Exit ")

def dispStat(List):#O(N)-->N length of List 
  #display how many male and female in the file
  Nb_Male = 0 # Counter of Male
  Nb_Female = 0 # Counter of Female
  for i in range(len(List)):#O(N)
    if List[i][3].lower() == "male":
      Nb_Male += 1 # Counter + 1 each time List[i][3] = "male"
    elif List[i][3].lower() == "female":
      Nb_Female += 1 # Counter + 1 each time List[i][3] = "female"
  print("Number of Male =", Nb_Male)
  print("Number of Female =", Nb_Female)

def addEmployee(List):#O(N)-->N length of List
  # Add an new employee (name , gender , salary) and auto date and ID
  from datetime import date #import from class datetime the data function 
  # https://www.programiz.com/python-programming/datetime/current-datetime
  List1 = [] # empty list for append the new employee info
  Info = ["id", "name", "date", "gender", "salary"]
  for i in Info:#O(N)
    if i == "id":
      New_Id = int(List[-1][0][3:]) + 1 # take lat 3 digits in employee ID as integer (Example : 001 ,004) then add 1
      if len(str(New_Id))==3:#ID >= emp100
        a = ("emp" + str(New_Id))
      if len(str(New_Id))==2:#ID >= emp010
        a = ("emp0" + str(New_Id))
      if len(str(New_Id))==1:#ID <= emp009
        a = ("emp00" + str(New_Id))
      print("id : ", a)
    elif i == "date":
      a = str(date.today()).replace("-", "")#from yy-mm-dd to YYMMDD
      print("date : ", a)
    else:
      a = input(i + " : ") # append (name , gender , salary)
    List1.append(a)
  print("\nAdd New Employee : ", List1)
  from csv import writer # from csv class import writer function be abel to write and add into employees.csv
  # https://www.geeksforgeeks.org/how-to-append-a-new-row-to-an-existing-csv-file/
  with open('employees.csv', 'a') as AddFile: # 'a' for add new row in employees.csv
    Add = writer(AddFile)
    Add.writerow(List1)#add list as new row in file
    AddFile.close()#clos file to save change

def dispAllEmp(List):#O(N^2)-->N length of List
  #display show employees in order from to today to the old one bye date
  #using selection sort method
  for i in range (len(List)-1):#O(N) # if i=0 first row
    for j in range (i+1,len(List)):#O(N-1) # then j=i+1=1 second row
      if List[i][2] < List[j][2]: #compare between the date in row 1 (Ex at index 0 )and row 2 (Ex at index 1)
        temp= List[i] #save the value of List[i] in temp
        List[i]= List[j]# put the value of List[j] in List[i] 
        List[j] = temp # List[j]=temp=First value of List[i]
  import numpy as np # i use the numpy class only to change the display of the matrix (List) and be easier to read .
  # https://www.programiz.com/python-programming/matrix 
  print("Your sorted Employees : \n\n" ,np.array(List))

def changeSal(List):#O(N)-->N length of List
  #change employee salary by input employee ID
  Emp=input("Enter the employee ID : ")
  for i in range (len(List)):#O(N) #search for ID in employees.csv appended in List
    if List[i][0]==Emp: #when ID is founded
      print("The salary of" , List[i][0] ," is : " , List[i][4] )
      Sal_Change=input("Enter new salary : ")
      List[i][4]=Sal_Change # change the value of the old salary to the new input salary
      print("The new Salary of ", List[i][0] , " is ", Sal_Change)
      import pandas as pd #import from pandas class pd function to read/call the file (employees.csv)
      File = pd.read_csv('employees.csv',index_col='ID')#read only colum with index ID in file 'employees.csv'
      # https://thispointer.com/edit-cell-values-in-csv-files-using-pandas-in-python/ 
      File.loc[Emp, 'Salary'] = Sal_Change #change the salary value of "emp" (input ID)  in file 
      return File.to_csv('employees.csv') #save file
  print("Employee NOT FOUND")

def removeEmp (List):#O(N)-->N length of List
  # Remove employee by choosing ID
  Emp=input("Enter the employee ID : ")#input employee ID.
  for i in List:#O(N)
    if i[0]==Emp:  #when ID is founded.
      print(Emp , " is removed")
      import pandas as pd #import from pandas class pd function to read/call the file (employees.csv).
      Data = pd.read_csv('employees.csv',index_col="ID") #read only colum with index ID in file 'employees.csv'.
      Data.drop(Emp,inplace=True) #using drop() function to remove row from file ,
      # inplace is false by default (an original copy of the modified row will stay displayed) , so i called inplace=true to disable the original copy.
      # https://www.activestate.com/resources/quick-reads/how-to-delete-a-column-row-from-a-dataframe/
      Data_Frame= pd.DataFrame(Data)#change 'Data' to Data Frame .
      return Data_Frame.to_csv('employees.csv',',')# add Data_frame in employees.csv .
  print(Emp," NOT FOUND !")

def raiseSal(List):#O(N)-->N length of List
  # Raise employee salary by % by input employee ID
  Emp=input("Enter the employee ID : ")
  for i in range (len(List)):#O(N)
    if List[i][0].lower()==Emp:#when ID is founded.
      print("The salary of" , List[i][0] ," is : " , List[i][4] )
      Raise_per=eval(input("Enter raise percentage : "))
      Raise = int(List[i][4])*(Raise_per/100)# "/" as float not integer (example raise=1,5%)
      New_sal=int(List[i][4])+int(Raise) #salary*1.5%
      print("The new Salary of ", List[i][0] , " is ", New_sal)
      import pandas as pd #import from pandas class pd function to read/call the file (employees.csv)
      File = pd.read_csv('employees.csv',index_col='ID')#read only colum with index ID in file employees.csv
      File.loc[Emp, 'Salary'] = New_sal #change the salary value of "Emp" (input ID)  in file 
      return File.to_csv('employees.csv')#save file
  print("Employee NOT FOUND")

def checkSal(List,Name):#O(N)-->N length of List
  # let employee check his/her salary by taking his/her login name 
  for i in List:#O(N)
    if i[1]==Name: #if Name is founded in employees.csv
      print("\nYour Salary is : ", i[4]) #print his/her Salary
      break
def Logintime(Name):
  # Save employees login date and time by names
  from datetime import datetime #import from class datetime the data function and time function
  log=[]
  log.append(Name)#append employee name
  log.append(" was logged in ")
  log.append(datetime.now())#append date and time now (time of employee login)
  from csv import writer # import from csv class the writer function to write into file (Emp_login.csv)
  with open('empLogin.csv', 'a') as AddFile:#use 'a' to add into file (Emp_login.csv)
    Add = writer(AddFile)
    Add.writerow(log)#add new row (log)
    AddFile.close()#close and save file
    
def main():
  print("Welcome !! \n\nYOU ARE : \n\n_ Admin\n_ User")
  Type = input("\nPlease choose your log in type : ")
  while Type.lower() != "admin" and Type.lower() != "user":
    print("Invalid Type ,Try again ")
    Type = input("Please choose your log in type : ")
  if Type.lower() == "admin": # if user choose admin
    Attempts = 5 # attempts counter
    flag = True
    while Attempts != 0 and flag == True: #while attempts counter is !=0 and didn't enter the else statement (flag still true)
      User_Name = input("\nUsername  : ")
      Pass = input("Password : ")
      if User_Name != "admin" or Pass != "admin123123":
        print("Your USERNAME OR PASSWORD is INCORRECT, ",
              Attempts-1, " Attempts left")
        Attempts -= 1 # attempts counter - 1
      else:
        flag = False
    if flag == True:# if Attempts counter = 0 , and didn't enter the else (flag =false ) statements 
      print("\n^ ^ OUT OF ATTEMPTS ^ ^")
    else:
      adminMenu()
      choice = eval(input("\nEnter your choice : "))
      while choice != 7:
        # https://www.tutorialspoint.com/importing-data-in-python
        import csv # impsort csv class
        with open('employees.csv') as Emp: #open csv file (employees.csv)
          Rows = csv.reader(Emp)#read the csv file using Rows
          List = []
          for i in Rows:
            List.append(i)#append file rows in List
        if choice == 1:
          dispStat(List)
        elif choice == 2:
          addEmployee(List)
        elif choice==3:
          dispAllEmp(List)
        elif choice==4:
          changeSal(List)
        elif choice==5:
          removeEmp (List)
        elif choice==6:
          raiseSal(List)
        elif choice !=6:
          print("\nInvalid choice , Try again")
        adminMenu()
        choice = eval(input("\nEnter your choice : "))
      print("YOU EXIT")  

  elif Type.lower() == "user":
    import csv#import csv class
    with open('employees.csv') as Emp: #open csv file
      Rows = csv.reader(Emp)#read csv file
      List = []
      for i in Rows:
        List.append(i)#append 'employees.csv' rows in the List
    flag3=True
    while flag3==True :#while 'i' didn't enter the first if statement flag3==true
      Name=input("\nUsername (Name of employee): ")
      Password=input("Password: ")
      for i in List:
        if str(i[1])==Name.lower() and Password=="":
          flag3=False #change flag3 to false to exit while loop
          if i[3].lower()=="male":
            print("\nHi Mr." ,i[1])
            break
          elif i[3].lower()=="female":
            print("\nHi Ms." ,i[1]) 
            break
      if flag3==True:#after finished for loop and didn't found the name of employee and password isn't empty , print invalid
        print("\nYour USERNAME OR PASSWORD is INCORRECT , TRY AGAIN !")
    userMenu()
    choice = eval(input("\nEnter your choice : "))
    while choice != 2:
      if choice == 1:
        checkSal(List,Name)
      if choice != 1:
        print("\nInvalid choice , Try again")
      userMenu()
      choice = eval(input("\nEnter your choice : "))
    Logintime(Name)#save employee login time in Emp_login.csv file
    print("YOU EXIT ! ")

main()