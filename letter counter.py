word=input("enter word:")
char=input("enter char:")
count=0
while count<=len(word):
    for char in word:
        if char==word[count]:
            count+=1
print(count)
            
        
        
    
