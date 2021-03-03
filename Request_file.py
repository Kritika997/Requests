import json
import requests
#geting the from saralurl in this we will get our courses lists:
Saral_Url = "http://saral.navgurukul.org/api/courses"
Calling_Api = requests.get(Saral_Url)
Data = Calling_Api.json()
with open("Saral_Data.json","w") as myfile:
    json.dump(Data,myfile,indent=4)
#printing the all courses which we have in our saral for showing how many courses with id we have in saral:
Data_List = Data["availableCourses"]
Courses_name = 0
while Courses_name<len(Data_List):
    print(Courses_name+1,":-",Data_List[Courses_name]["name"], "ID - ",Data_List[Courses_name]["id"])
    Courses_name +=1
#in this we will take one user input for printing specific course means user choice course will come and we will ask he wants to 
# change her/his course or not the we will go further :
user_choice_course = int(input("please choose your course: "))
print("#",Data_List[user_choice_course-1]["name"]) 
user_id = Data_List[user_choice_course-1]["id"]
#calling second api for calling the parents means in courses we are having inside topics name that's we are calling parents :
Saral_data = "http://saral.navgurukul.org/api/courses/"+str(user_id)+"/exercises"
call_to_api = requests.get(Saral_data)
Storing_Data = call_to_api .json()
with open("saral_second_api.json","w") as myfile_2:
    json.dump(Storing_Data,myfile_2,indent=4)
#in this whole parents will come with thier childs if they don't have childs then their slug will print :
Data_List_2 = Storing_Data["data"]
parents_name = 0
while parents_name<len(Data_List_2):
    print ("","*",parents_name+1,Data_List_2[parents_name]["name"])
    if Data_List_2[parents_name]["childExercises"]==[]:
        print("     1","-:",Data_List_2[parents_name]["slug"])
    else:
        child_name = 0
        while child_name<len(Storing_Data["data"][parents_name]["childExercises"]):
            print("  ","-:",child_name+1,Storing_Data["data"][parents_name]["childExercises"][child_name]["name"])
            child_name+=1
    parents_name+=1
Do_you_wants_to_continue = input("Do you want to continue with this course if yes say Yes if don't want than say No").lower()
if Do_you_wants_to_continue=="no":
    Data_List = Data["availableCourses"]
    Courses_name = 0
    while Courses_name<len(Data_List):
        print(Courses_name+1,":-",Data_List[Courses_name]["name"], "ID - ",Data_List[Courses_name]["id"])
        Courses_name +=1
    user_choice_course = int(input("please choose your course: "))
    print("#",Data_List[user_choice_course-1]["name"]) 
    user_id = Data_List[user_choice_course-1]["id"]
    Data_List_2 = Storing_Data["data"]


    parents_name = 0
    while parents_name<len(Data_List_2):
        print ("","*",parents_name+1,Data_List_2[parents_name]["name"])
        if Data_List_2[parents_name]["childExercises"]==[]:
            print("     1","-:",Data_List_2[parents_name]["slug"])
        else:
            child_name = 0
            while child_name<len(Storing_Data["data"][parents_name]["childExercises"]):
                print("  ","-:",child_name+1,Storing_Data["data"][parents_name]["childExercises"][child_name]["name"])
                child_name+=1
        parents_name+=1


user_choice_parents = int(input("please chose your parents which you wants: "))
user_choice_parents = user_choice_parents-1

if Data_List_2[user_choice_parents]["childExercises"]==[]:
    print(user_choice_parents+1,Storing_Data["data"][user_choice_parents]["name"])
    print("     1","-:",Data_List_2[user_choice_parents]["slug"]) 
else:
    print(user_choice_parents+1,Storing_Data["data"][user_choice_parents]["name"])
    i = 0
    my_list = []
    while i<len(Storing_Data["data"][user_choice_parents]["childExercises"]):
        print("  ",i+1,":-",Storing_Data["data"][user_choice_parents]["childExercises"][i]["name"])

        slug = Storing_Data["data"][user_choice_parents]["childExercises"][i]["slug"]
        child_slug_api = ("http://saral.navgurukul.org/api/courses/"+str(user_id)+"/exercise/getBySlug?slug="+slug)
        calling_child_api = requests.get(child_slug_api)
        storing_child_slug_data = calling_child_api.json()
        with open("saral_third_api.json","w") as myfile_3:
            json.dump(storing_child_slug_data,myfile_3,indent=4)
        Data_list_3 = storing_child_slug_data["content"]
        my_list.append(Data_list_3)
        i = i+1
    user_chose_question= int(input("enter your choosen question"))
    user_chose_question = user_chose_question-1
    print(my_list[user_chose_question])
    while user_chose_question>=0:
        user_wants_to_go_previous_ya_next= input("do you want to go to previous question ya next question say P ya N: ").lower()
        if user_wants_to_go_previous_ya_next=="p":
            print(my_list[user_chose_question])
            user_chose_question-=1
        elif user_wants_to_go_previous_ya_next=="n":
            if user_chose_question==len(my_list)-1:
                print("Page not Found")
                break
            user_chose_question+=1
            print(my_list[user_chose_question])
        else:
            print("input is not valid")
    else:
        print("page is finish")