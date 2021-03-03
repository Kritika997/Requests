import json
import requests

with open("Saral_Data.json") as myfile:
    Data=json.load(myfile)

Data_List = Data["availableCourses"]
Courses_name = 0
while Courses_name<len(Data_List):
    print(Courses_name+1,":-",Data_List[Courses_name]["name"], "ID - ",Data_List[Courses_name]["id"])
    Courses_name +=1

user_choice_course = int(input("please choose your course: "))
print("#",Data_List[user_choice_course-1]["name"]) 
user_id = Data_List[user_choice_course-1]["id"]

parent_name=open("saral_second_api.json")
Data_List_2=json.load(parent_name)

my_file=open("saral_second_api.json")
Storing_Data=json.load(my_file)


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
        i=i+1

        
my_file=open("saral_third_api.json")
Storing_child_slug_data=json.load(my_file)
print(Storing_child_slug_data)

