from os import access
import requests
import array as content


r = requests.get('http://www.uietkanpur.com/')
content = r.text

i=0
while(i<len(content)):
    
    if content[i] == "<":
    #removing CSS element
        if content[i+1] == "s" and content[i+2] == "t" and content[i+3] == "y" and content[i+4] == "l" and content[i+5] == "e":         
            i = i + 6
            while(content[i] != "e" or content[i+1] != ">"):
                    i = i + 1
    #removing JS element
        elif content[i+1] == "s" and content[i+2] == "c" and content[i+3] == "r" and content[i+4] == "i" and content[i+5] == "p" and content[i+6] == "t":
            i = i + 7
            while(content[i] != "t" or content[i+1] != ">"):
                    i = i+1
    #removing HTML/CSS comments
        elif content[i+1] == "!" and content[i+2] == "-" and content[i+3] == "-":
            i = i + 4
            while(content[i] != ">"):
                    i = i+1
    #removing HTML element
        else:
            while(content[i] != ">"):
                i=i+1

    #removing Js Comments
    elif content[i] == "/" and content[i+1] == "*":
            i = i + 3
            while(content[i] != "/"):
                    i = i+1
        
    else:
        if ord(content[i]) < 65 and ord(content[i]) > 90 and ord(content[i]) < 97 and  ord(content[i]) > 122 :
            content[i] = " "
        #print(content[i], end="")
        f = open("uietCsjmu.txt", "a")
        f.write(content[i])

    i=i+1

access
f = open("uietCsjmu.txt", "r")
access = f.read()
i = 0
#removing unwanting characters
while(i<len(access)):
    if (ord(access[i]) >= 65 and ord(access[i]) <= 90) or (ord(access[i]) >= 97 and  ord(access[i]) <= 122) :
        pass
    else:
        replacement = " "
        access = access[0:i] + replacement + access[i+1: ]
       
    i = i + 1
#print(access)
world_list = access.split(" ")
# print(world_list)

world_list2 =  []

for i in world_list:
    if i not in world_list2:  
        world_list2.append(i) 

for i in range(0, len(world_list2)):  
        print('Frequency of', world_list2[i], 'is :', world_list.count(world_list2[i]))   
              
