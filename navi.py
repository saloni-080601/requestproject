
import requests
import json
import pprint
url1=requests.get("https://api.merakilearn.org/courses")
var1=url1.json()
with open ("course.json","w") as f:
    json.dump(var1,f,indent=5)
serial_no=0
for i in var1:   
    print(serial_no+1,i["name"],i["id"])
    serial_no+=1
course_no=int(input("enter a serial no"))
print(var1[course_no-1]["name"])
navi=input("do you want p/n")
if navi=="p":
    for i in var1:
        print(serial_no+1,i["name"],i["id"])
        serial_no+=1
else:
    idd=var1[course_no-1]["id"]
    url2=requests.get("http://api.merakilearn.org/courses/" +str(idd)+"/exercises")
    var2=url2.json()
    with open ("topic.json","w") as u:
        json.dump(var2,u,indent=5)    
    list1=[]
    list2=[]
    for j in var2["course"]["exercises"]:
        if j["parent_exercise_id"]==None:
            list1.append(j)
            continue
        if j["id"]==j["parent_exercise_id"]:
            list1.append(j)
        
        for k in var2["course"]["exercises"]:
            if j["parent_exercise_id"]!=j["id"]:    
                list2.append(j)
                break
    with open ("inner.json","w") as f:
        json.dump(list1,f,indent=5)
    serial=1
    s_no=1
    for a in list1:
        if a["parent_exercise_id"]==None:
            print(s_no,a["name"])
            print("     ",serial,".",a["slug"])
            serial+=1
            s_no+=1
        if a["id"]==a["parent_exercise_id"]:
            print(s_no,".",a["name"]) 
            s_no+=1  
        with open ("under.json","w") as f:
            json.dump(list2,f,indent=5)
        s=1 
        for b in list2:
            if b["parent_exercise_id"]==a["id"]:    
                print("     ",s,".",b["name"])
                s+=1
    choice_no3=int(input("enter a topic"))
    navi=input("what you want n/p")
    if navi=="p":
        for a in list1:
            if a["parent_exercise_id"]==None:
                print(s_no,a["name"])
                print("     ",serial,".",a["slug"])
                serial+=1
                s_no+=1
            if a["id"]==a["parent_exercise_id"]:
                print(s_no,".",a["name"]) 
                s_no+=1  
            with open ("under.json","w") as f:
                json.dump(list2,f,indent=5)
            s=1 
            for b in list2:
                if b["parent_exercise_id"]==a["id"]:    
                    print("     ",s,".",b["name"])
                    s+=1
    else:
        for c in list1:
            if list1["parent_exercise_id"]==None:
                print(list1[choice_no3-1]["content"])
                if c["id"]==c["parent_exercise_id"]:
                    print(list1[choice_no3-1]["name"])
                    print(list1[choice_no3-1]["content"])
                    com=list1[choice_no3-1]["id"]
                    break
        s_na=1
        some=[]
        next=[]
        for d in list2:

            if d["parent_exercise_id"]==com:
                print("    ",s_na,d["name"])
                some.append(d["name"])
                next.append(d["content"])

                s_na+=1
        point=int(input("enter a point"))
        navi=input("what you want p/n")
        if navi=="p":
            for c in list1:
                if c["id"]==c["parent_exercise_id"]:
                    print(list1[choice_no3-1]["name"])
                    print(list1[choice_no3-1]["content"])
                    com=list1[choice_no3-1]["id"]
                    break
            s_na=1
            some=[]
            next=[]
            for d in list2:
                if d["parent_exercise_id"]==com:
                    print("    ",s_na,d["name"])
                    some.append(d["name"])
                    next.append(d["content"])

                    s_na+=1
        else:
            y=1
            for f in range(0,len(some)):
                if point==y:
                    print(some[f])
                    print(next[f])
                    print()
                y+=1

        
        


                  
    

    