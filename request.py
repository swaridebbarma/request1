import json
import requests


a = requests.get("http://saral.navgurukul.org/api/courses")
b = a.json()
with open("swari.json","w") as c:
    json.dump(b,c,indent=4)

# print(b)

n = 0
id = []
for i in b["availableCourses"]:
    print(n, i["name"],":", i["id"])
    id.append(i["id"])
    n += 1
    # print(id)

user = int(input("enter your serial number:"))
d = 0
e = requests.get("http://saral.navgurukul.org/api/courses/"+id[user]+"/exercises")
f = e.json()
g = []
for i in f["data"]:
    print(d,i["slug"])
    g.append(i["slug"])
    d += 1

user2 = int(input("enter the slug number:"))

h = requests.get("http://saral.navgurukul.org/api/courses/"+str(user)+"/exercise/getBySlug?slug=" +g[user2])
i = h.json()
print(i)