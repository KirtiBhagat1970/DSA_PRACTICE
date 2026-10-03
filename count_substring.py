str="hellohellohello"
substr="hello"
count=0
start=0
while True:
    start=str.find(substr,start)
    if start==-1:
        break
    count+=1
    start+=1 
print(f"total occurences of '{substr}':{count}")


