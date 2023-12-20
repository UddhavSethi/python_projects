

string="chennai,Bangalore,gurgaon"
string2="vit,kit,iit"
x=string.split(",")
y=string2.split(",")
dict1={}
for i in x:
    for j in y:
        dict1[i]=j 
print(dict1)
        
    

    