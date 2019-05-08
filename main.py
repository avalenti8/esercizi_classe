import requests
a = requests.post("http://192.168.1.231:8080/accreditamento", json={"nome" :"Alessandro Valenti"})
print(a.json())
CO = 0
#1
a = requests.get("http://192.168.1.231:8080/esercizi/1",headers={"x-data":"true"})
body = a.json()
b = body["data"]
r = b.lower()
CO += 1
print(CO)
response = requests.post("http://192.168.1.231:8080/esercizi/1",json={"data":r})
print(response.json())

#2
a = requests.get("http://192.168.1.231:8080/esercizi/2",headers={"x-data":"true"})
body = a.json()
b = body["data"]
r = b*b
CO += 1
print(CO)
response = requests.post("http://192.168.1.231:8080/esercizi/2",json={"data":r})
print(response.json())

#3
a = requests.get("http://192.168.1.231:8080/esercizi/3",headers={"x-data":"true"})
body = a.json()
b = body["data"]
r = b["cognome"]
CO += 1
print(CO)
response = requests.post("http://192.168.1.231:8080/esercizi/3",json={"data":r})
print(response.json())

#4
a = requests.get("http://192.168.1.231:8080/esercizi/4",headers={"x-data":"true"})
body = a.json()
b = body["data"]
r = len(b)
CO += 1
print(CO)
response = requests.post("http://192.168.1.231:8080/esercizi/4",json={"data":r})
print(response.json())

#5
a = requests.get("http://192.168.1.231:8080/esercizi/5",headers={"x-data":"true"})
body = a.json()
b = body["data"]
r = []
for i in b:  
  t = i.upper()
  r.append(t)
CO += 1
print(CO)
response = requests.post("http://192.168.1.231:8080/esercizi/5",json={"data":r})
print(response.json())

#6
a = requests.get("http://192.168.1.231:8080/esercizi/6",headers={"x-data":"true"})
body = a.json()
b = body["data"]
r = 0
for i in b:
  r = r + i
CO += 1
print(CO)
response = requests.post("http://192.168.1.231:8080/esercizi/6",json={"data":r})
print(response.json())

#7
a = requests.get("http://192.168.1.231:8080/esercizi/7",headers={"x-data":"true"})
body = a.json()
b = body["data"]
r = 0
for i in b:
  if i > 5:
    r = r + i
CO += 1
print(CO)
response = requests.post("http://192.168.1.231:8080/esercizi/7",json={"data":r})
print(response.json())

#8
a = requests.get("http://192.168.1.231:8080/esercizi/8",headers={"x-data":"true"})
body = a.json()
b = body["data"]
r = 0
for i in range(len(b)):
  t = b[i]
  if i%2 == 0:
    r = r + t    
CO += 1
print(CO)
response = requests.post("http://192.168.1.231:8080/esercizi/8",json={"data":r})
print(response.json())

#9
a = requests.get("http://192.168.1.231:8080/esercizi/9",headers={"x-data":"true"})
body = a.json()
b = body["data"]
r = 0
for i in b:
  if i%2 != 0:
    r = r + i   
CO += 1
print(CO)
response = requests.post("http://192.168.1.231:8080/esercizi/9",json={"data":r})
print(response.json())

#10
a = requests.get("http://192.168.1.231:8080/esercizi/10",headers={"x-data":"true"})
body = a.json()
b = body["data"]
r = []
for i in b:
  r.append(i)
r.sort()
CO += 1
print(CO)
response = requests.post("http://192.168.1.231:8080/esercizi/10",json={"data":r})
print(response.json())

#11
a = requests.get("http://192.168.1.231:8080/esercizi/11",headers={"x-data":"true"})
body = a.json()
b = body["data"]
r = []
for i in b:
  r.append(i.lower())
r.sort()
CO += 1
print(CO)
response = requests.post("http://192.168.1.231:8080/esercizi/11",json={"data":r})
print(response.json())

#12
a = requests.get("http://192.168.1.231:8080/esercizi/12",headers={"x-data":"true"})
body = a.json()
b = body["data"]
r = []
for i in b:
  r.append(i-1)
CO += 1
print(CO)
response = requests.post("http://192.168.1.231:8080/esercizi/12",json={"data":r})
print(response.json())

#13
a = requests.get("http://192.168.1.231:8080/esercizi/13",headers={"x-data":"true"})
body = a.json()
b = body["data"]
r = []
for i in range(len(b)):
  if i != len(b)-1: 
    c = b[i] + b[i+1]
    r.append(c)
  else:
    r.append(b[i])
CO += 1
print(CO)
response = requests.post("http://192.168.1.231:8080/esercizi/13",json={"data":r})
print(response.json())

#14
a = requests.get("http://192.168.1.231:8080/esercizi/14",headers={"x-data":"true"})
body = a.json()
b = body["data"]
r = {
        "positivi":0,
        "negativi":0,
        "zeri":0
}
for i in b:
  if i > 0:
    r["positivi"] += 1
  elif i < 0:
    r["negativi"] += 1
  if i == 0:
    r["zeri"] += 1
CO += 1
print(CO)
response = requests.post("http://192.168.1.231:8080/esercizi/14",json={"data":r})
print(response.json())

#15
a = requests.get("http://192.168.1.231:8080/esercizi/15",headers={"x-data":"true"})
body = a.json()
b = body["data"]
r = []
for i in b:
  if len(i)%2 == 0:
    r.append(i.upper())
  else:
    r.append(i.lower())
CO += 1
print(CO)
response = requests.post("http://192.168.1.231:8080/esercizi/15",json={"data":r})
print(response.json())

#16
a = requests.get("http://192.168.1.231:8080/esercizi/16",headers={"x-data":"true"})
body = a.json()
b = body["data"]
r = ""
for i in b:
  if i != b[-1]:
    r = r + i + " "
  else:
    r = r + i
CO += 1
print(CO)
response = requests.post("http://192.168.1.231:8080/esercizi/16",json={"data":r})
print(response.json())

#17
a = requests.get("http://192.168.1.231:8080/esercizi/17",headers={"x-data":"true"})
body = a.json()
b = body["data"]
r = ""
for i in b:
  r = r + i[-1]
CO += 1
print(CO)
response = requests.post("http://192.168.1.231:8080/esercizi/17",json={"data":r})
print(response.json())

#18
a = requests.get("http://192.168.1.231:8080/esercizi/18",headers={"x-data":"true"})
body = a.json()
b = body["data"]
r = ""
for i in b:
  if len(i) > 4:
    r = r + i[0]
CO += 1
print(CO)
response = requests.post("http://192.168.1.231:8080/esercizi/18",json={"data":r})
print(response.json())

#19
a = requests.get("http://192.168.1.231:8080/esercizi/19",headers={"x-data":"true"})
body = a.json()
b = body["data"]
r = []
for i in range(b+1):
  if i!=0:
    if b%i == 0:
      r.append(i)
CO += 1
print(CO)
response = requests.post("http://192.168.1.231:8080/esercizi/19",json={"data":r})
print(response.json())

#20
a = requests.get("http://192.168.1.231:8080/esercizi/20",headers={"x-data":"true"})
body = a.json()
b = body["data"]
r = []
for i in b:
  r.append(len(i["figli"]))
CO += 1
print(CO)  
response = requests.post("http://192.168.1.231:8080/esercizi/20",json={"data":r})
print(response.json())

#21
a = requests.get("http://192.168.1.231:8080/esercizi/21",headers={"x-data":"true"})
body = a.json()
b = body["data"]
r = []
for i in b:
  if i <= 5:
    r.append(i)
CO += 1
print(CO)  
response = requests.post("http://192.168.1.231:8080/esercizi/21",json={"data":r})
print(response.json())

#22
a = requests.get("http://192.168.1.231:8080/esercizi/22",headers={"x-data":"true"})
body = a.json()
b = body["data"]
r = []
for i in b:
  if i > 2:
    if i < 7:
      r.append(i)
CO += 1
print(CO)  
response = requests.post("http://192.168.1.231:8080/esercizi/22",json={"data":r})
print(response.json())

#23
a = requests.get("http://192.168.1.231:8080/esercizi/23",headers={"x-data":"true"})
body = a.json()
b = body["data"]
r = 0
for i in b:
  r += i["anni"]
CO += 1
print(CO)
response = requests.post("http://192.168.1.231:8080/esercizi/23",json={"data":r})
print(response.json())