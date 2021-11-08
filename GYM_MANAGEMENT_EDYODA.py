Member_detail = {}
Regimen_for_All_Member = {}


class Member:
    @classmethod
    def Add_Member(cls):
        Person = {}
        Name = input("Enter Member Name:")
        Age = input("Enter Member Age:")
        Gender = input("Enter Member Gender:")
        Mobile_no = input("Enter Member Mobile no:")
        Password = input("Enter password: ")
        Email = input("Enter Member Email:")
        BMI = int(input("Enter Member BMI(Body Mass Index) Between 0 to 35:"))
        Month = int(input("Enter Membership Duration Months 1,3,6 and 12:"))
            
        Person["Name"] = Name
        Person["Age"] = Age
        Person["Gender"] = Gender
        Person["Mobile_no"] = Mobile_no
        Person["Password"] = Password
        Person["Email"] = Email
        Person["BMI"] = BMI
        Person["Duration of Membership Month"] = Month
        Member_detail[Mobile_no] = Person
        Regimen_for_All_Member[Mobile_no] = Member.Regimens(BMI)

    @classmethod
    def Details(cls, number):
        if number in Member_detail:
            user = Member_detail[number]
            print("Name: ", user["Name"])
            print("Age: ", user["Age"])
            print("Gender: ", user["Gender"])
            print("Mobile no: ", user["Mobile_no"])
            print("Email: ", user["Email"])
            print("BMI: ", user["BMI"])
            print("Duration of Membership month: ", user["Duration of Membership Month"])

    @classmethod
    def DeleteMember(cls, x):
        del Member_detail[x]

    @classmethod
    def Regimens(cls, BMI):
        if int(BMI) <= 18.5:
            regimens_details = {"Mon": "Chest", "Tue": "Biceps", "Wed": "Rest",
                                "Thu": "Back", "Fri": "Triceps", "Sat": "Rest", "Sun": "Rest"}
        elif 18<int(BMI)<= 25:
            regimens_details = {"Mon": "Chest", "Tue": "Biceps", "Wed": "Cardio/Abs",
                                "Thu": "Back", "Fri": "Triceps", "Sat": "Legs", "Sun": "Rest"}
        elif 25< int(BMI)<= 30:
            regimens_details = {"Mon": "Chest", "Tue": "Biceps", "Wed": "Abs/Cardio",
                                "Thu": "Back", "Fri": "Triceps", "Sat": "Legs", "Sun": "Cardio"}
        else:
            30< int(BMI)<=35
            regimens_details = {"Mon": "Chest", "Tue": "Biceps", "Wed": "Cardio",
                                "Thu": "Back", "Fri": "Triceps", "Sat": "Cardio", "Sun": "Cardio"}
        return regimens_details
    @classmethod
    def update_user_profile(cls,mobile_no):
        while True:
            edit_choose=input("Press 1 for edit name\nPress 2 for edit age\nPress 3 for edit gender\nPress 5 for edit email\nPress 0 for exit")
            if edit_choose=='1':
                Member_detail[mobile_no]["Name"]=input("Enter name")
            elif edit_choose=='2':
                Member_detail[mobile_no]["Age"]=input("Enter age")
            elif edit_choose=='3':
                Member_detail[mobile_no]["Gender"]=input("Enter gender")
            elif edit_choose=='4':
                Member_detail[mobile_no]["Email"]=input("Enter email")
            elif edit_choose=='0':
                break


while True:
    x = input("Press 1 for SUPER-USER: \nPress 2 for Member: \nEnter your option:")
    choose_option = 100
    if x == "1":
        print("*SUPER-USER Active*")
        while choose_option != "0":
            choose_option = input("Press 1 to Create a Member: \nPress 2 to View Member: "
                                  "\nPress 3 to Delete a Member: \nPress 4 to Update Member: "
                                  "\nPress 5 to Create Regimen: \nPress 6 to View Regimen: "
                                  "\nPress 7 to Delete Regimen: \nPress 8 to Update Regimen: \n"
                                  "Press 0 for Logout:\nEnter your choice:")
            if choose_option == "1":
                Member.Add_Member()
                for_pass = input("Press 'Enter' for next - ")

            elif choose_option == "2":
                mobile_number = input("Enter Member Mobile no-\n--")
                if mobile_number in Member_detail:
                    Member.Details(mobile_number)
                else:
                    print("Details not found!!!")
                for_pass = input("Press 'Enter' for next - ")

            elif choose_option == "3":
                Enter_no_to_delete = input("Enter Mobile Number to Delete Member Details-\n--")
                if Enter_no_to_delete in Member_detail:
                    Member.DeleteMember(Enter_no_to_delete)
                    del Regimen_for_All_Member[Enter_no_to_delete]
                    print("Member details were deleted...")
                else:
                    print("Mobile Not Present in Database...")
                for_pass = input("Press 'Enter' for next: ")

            elif choose_option == "4":
                process = input("0 for update details \n1 for Extend Member \n2 for Delete Member-\n--")
                number = input("Enter Member Mobile Number -\nEnter your choice:")
                if process == "0":
                    input1 = input("What you want to update: Name, Age, Gender, Email, BMI, Month [case sensitive]\n"
                                   "mobile number would not be changed*\n--")
                    Member_detail[number][input1] = input("Enter changes:\n--")
                elif process == "1":
                    Member.Add_Member()

                elif process == "2":
                    if number in Member_detail:
                        conform = input("Enter yes to delete:\nEnter details here:")
                        if conform == "yes":
                            Member.DeleteMember(number)
                            print("Details of Member was DELETED ...")
                        else:
                            print("Member Details not be DELETED !!!")
                    else:
                        print("Invalid Mobile Number Enter by You")
                else:
                    print("YOU CHOOSE INVALID OPTION !!!")
                for_pass = input("Press 'Enter' for next:")

            elif choose_option == "5":
                dict_day = {}
                Enter_number = input("Enter Mobile Number of Member:")
                list_of_day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
                if Enter_number in Regimen_for_All_Member:
                    for i in list_of_day:
                        for j in range(1, 2):
                            dict_day[i] = input(f"{i} Regimen - ")
                else:
                    print("This number don't have Membership!!!")
                Regimen_for_All_Member[Enter_number] = dict_day
                for_pass = input("Press 'Enter' for next - ")

            elif choose_option == "6":
                Input = input("Enter Member Mobile Number-\n--")
                if Input in Regimen_for_All_Member:
                    for key in Regimen_for_All_Member[Input]:
                        print(key, "-", Regimen_for_All_Member[Input][key])
                else:
                    print("Regimen not found for this member")
                for_pass = input("Press 'Enter' for next - ")

            elif choose_option == "7":
                Input2 = input("Enter Member Mobile Number -\n--")
                if Input2 in Regimen_for_All_Member:
                    del Regimen_for_All_Member[Input2]
                    print("Regimen is DELETED for this Member")
                else:
                    print("Regimen is Not present in Database")
                for_pass = input("Press 'Enter' for next - ")

            elif choose_option == "8":
                Input3 = input("Enter Member Mobile Number-\n--")
                if Input3 in Regimen_for_All_Member:
                    Input4 = int(input("Enter Total Number of day you want to change Regimen -\n--"))
                    for i in range(1, (Input4 + 1)):
                        q = input("Enter day as like Sun, Mon, Tue, Wed, Thu, Fri, Sat - \n--")
                        r = input(f"Enter Regimen for {q} day -\n")
                        Regimen_for_All_Member[Input3][q] = r
                else:
                    print("Regimen not found (you delete it or not have Membership)")
                for_pass = input("Press 'Enter' for next:")

            else:
                if choose_option != "0":
                    print("Invalid Input!!!")
                else:
                    print("Logged Out")
            print()

    elif x == "2":
        print("*MEMBER Active*")
        number = input("Enter your Mobile Number -\n--")
        Password = input('Enter your Password -\n--')
        if number in Member_detail:
            if Member_detail[number]['Password']==Password:
        
        
                while choose_option != "0":
                    choose_option = input("Press 1 for My Regimen \nPress 2 for My Profile\nPress 3 for Update Profile \n"
                                          "\nPress 0 for Log Out \n--")
                    if choose_option == "1":
                        if number in Regimen_for_All_Member:
                            
                            for key in Regimen_for_All_Member[number]:
                                print(key, "-", Regimen_for_All_Member[number][key])
                        else:
                            print("Regimen Not Found For You please enter valid details")
                        for_pass = input("Press 'Enter' for next - ")



                    elif choose_option == "2":
                        if number in Member_detail:
                            Member.Details(number)
                        else:
                            print("Member Details Not Found.")
                        for_pass = input("Press 'Enter' for next - ")
                        
                      
                    
                    elif choose_option == "3":
                        number = input("Enter Member Mobile Number:")
                        if number in Member_detail:
                            Member.update_user_profile(number)
                        else:
                            print("Invalid Mobile Number Enter by You")

                    elif choose_option == "0":
                        print("Logged Out")
                    else:
                        print("Invalid Input Entered By You")
                    print()
                    for_pass = input("Press 'Enter' for next:")

            else:
                print("Invalid Input!!")
                
    else:
        print("Invalid Input!!")