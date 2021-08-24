import requests
import json
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
idd=var1[course_no-1]["id"]
url2=requests.get("http://api.merakilearn.org/courses/" +str(idd)+"/exercises")
var2=url2.json()
with open ("topic.json","w") as u:
    json.dump(var2,u,indent=5)    
list1=[]
list2=[]
s_no=1
for j in var2["course"]["exercises"]:
    serial=1
    if j["parent_exercise_id"]==None:
        print(s_no,j["name"])
        print("     ",serial,".",j["slug"])
        list1.append(j)
        s_no+=1
        continue  
    if j["id"]==j["parent_exercise_id"]:
        print(s_no,".",j["name"]) 
        list1.append(j) 
        s_no+=1
        s=1 
    for k in var2["course"]["exercises"]:
        if j["parent_exercise_id"]!=j["id"]: 
            print("     ",s,".",j["name"])
            list2.append(j)
            s+=1
            break
choice_no3=int(input("enter a topic"))
for c in list1:
    if c["id"]==c["parent_exercise_id"]:
        print(list1[choice_no3-1]["name"])
        com=list1[choice_no3-1]["id"]
        break
some=[]
next=[]
s_number=1
for d in list2:
    if d["parent_exercise_id"]==com:
        print("    ",s_number,d["name"])
        some.append(d["name"])
        next.append(d["content"])
        s_number+=1
point=int(input("enter a point"))
y=1
for f in range(0,len(some)):
    if point==y:
        print(some[f])
        print(next[f])
    y+=1

        
        


                  
    

    