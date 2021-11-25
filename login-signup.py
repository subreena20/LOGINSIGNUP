import json
import re
import os.path
print("***Welcome to my login-signup***")
user=input("Do you want to \n1.)signup\n2.)login: ")
file_exists=os.path.exists("login.json")
def dump(obj):
    with open("login.json","w") as f:
        json.dump(obj,f,indent=2)
if user=="signup":
    username=input("Enter your username: ")
    print("Create a strong password Use specail characters.")
    password1=input("Enter ur password: ")
    if re.search ("[a-z A-Z]",password1) and re.search ("[@%$#!]",password1) and re.search ("[0-9]",password1) :
        password2=input("Enter your password agian: ")
    
        if password1==password2:
            print("Matching")
            date_of_birth=input("enter your date of birth: ")
            gender=input("entere your gender\n1.)F\n2.)M\n3.)others: ")
            hobbies=("enter your hobbies: ")
            description=input("Enter your bio: ")
            contact=int(input("Enter your moblie number: "))
            dic={"username":username,"password":password1,"re_password":password2,"date_of_birth":date_of_birth,
                "gender":gender,"hobbies":hobbies,"description":description,"contact":contact}
            if file_exists==False:
                with open("login.json","w") as file:
                    d=file.read()
                    p=json.loads(d)
                    p.append(dic)
                    dump(p)
            else:
                with open ("login.json","w") as file:
                    json.dump([dic],file,indent=4)
        else:
            print("password not matching")
    else:
        print("weak password please use specail charcters")
else:
    if user=="login":
        username=input("enter your nusername: ")
        password=input("enter your password: ")
        with open("login.json","r") as file1:
            a=file1.read()
            b=json.loads(a)
            for i in b:
                if i["username"]==username:
                    if i["password"]==password:
                        print("login successfull")
                    else :
                        print("Wrong password")
                else:
                    print("wrong username")
    else:
        print("Wrong id")
              
