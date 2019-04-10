import requests
#a = requests.post("http://192.168.1.231:8080/accreditamento", json={"nome" :"Alessandro Valenti"})
#print(a.json())

#1
        #a = requests.get("http://192.168.1.231:8080/esercizi/1",headers={"x-data":"true"})
        #body = a.json()
        #print(body["message"])
        #b = body["data"]
        #r = b.lower()
        #response = requests.post("http://192.168.1.231:8080/esercizi/1",json={"data":r})
        #print(response.json())

#2
        #a = requests.get("http://192.168.1.231:8080/esercizi/2",headers={"x-data":"true"})
        #body = a.json()
        #print(body["message"])
        #b = body["data"]
        #r = b*b
        #response = requests.post("http://192.168.1.231:8080/esercizi/2",json={"data":r})
        #print(response.json())

#3
        #a = requests.get("http://192.168.1.231:8080/esercizi/3",headers={"x-data":"true"})
        #body = a.json()
        #print(body["message"])
        #b = body["data"]
        #r = b["cognome"]
        #response = requests.post("http://192.168.1.231:8080/esercizi/3",json={"data":r})
        #print(response.json())

#4
        #a = requests.get("http://192.168.1.231:8080/esercizi/4",headers={"x-data":"true"})
        #body = a.json()
        #print(body["message"])
        #b = body["data"]
        #r = len(b)
        #response = requests.post("http://192.168.1.231:8080/esercizi/4",json={"data":r})
        #print(response.json())

#5
        #a = requests.get("http://192.168.1.231:8080/esercizi/5",headers={"x-data":"true"})
        #body = a.json()
        #print(body["message"])
        #b = body["data"]
        #r = []
        #for i in b:  
        #  t = i.upper()
        #  r.append(t)
        #response = requests.post("http://192.168.1.231:8080/esercizi/5",json={"data":r})
        #print(response.json())

#6
        #a = requests.get("http://192.168.1.231:8080/esercizi/6",headers={"x-data":"true"})
        #body = a.json()
        #print(body["message"])
        #b = body["data"]
        #r = 0
        #for i in b:
        #  r = r + i
        #response = requests.post("http://192.168.1.231:8080/esercizi/6",json={"data":r})
        #print(response.json())

#7
        #a = requests.get("http://192.168.1.231:8080/esercizi/7",headers={"x-data":"true"})
        #body = a.json()
        #print(body["message"])
        #b = body["data"]
        #r = 0
        #for i in b:
        #  if i > 5:
        #    r = r + i
        #response = requests.post("http://192.168.1.231:8080/esercizi/7",json={"data":r})
        #print(response.json())

#8
        #a = requests.get("http://192.168.1.231:8080/esercizi/8",headers={"x-data":"true"})
        #body = a.json()
        #print(body["message"])
        #b = body["data"]
        #r = 0
        #for i in range(len(b)):
        #  t = b[i]
        #  if i%2 == 0:
        #    r = r + t    
        #response = requests.post("http://192.168.1.231:8080/esercizi/8",json={"data":r})
        #print(response.json())

#9
        #a = requests.get("http://192.168.1.231:8080/esercizi/9",headers={"x-data":"true"})
        #body = a.json()
        #print(body["message"])
        #b = body["data"]
        #r = 0
        #for i in b:
        #  if i%2 != 0:
        #    r = r + i    
        #response = requests.post("http://192.168.1.231:8080/esercizi/9",json={"data":r})
        #print(response.json())

#10
a = requests.get("http://192.168.1.231:8080/esercizi/10",headers={"x-data":"true"})
body = a.json()
print(body["message"])
b = body["data"]
r = []
for i in b:
  r.append(i)
r.sort()    
response = requests.post("http://192.168.1.231:8080/esercizi/10",json={"data":r})
print(response.json())