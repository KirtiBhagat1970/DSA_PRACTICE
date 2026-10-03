sentence=input("enter a sentence:")
words=sentence.split()
largest=words[0]
shortest=words[0]
for word in words:
    if len(word) > len(largest):
        largest=word
    if len(word) < len(shortest):
        shortest=word
print("largest word:",largest)
print("shortest word:",shortest)


sentence="my name is kirti"
words=sentence.split() it split the sentence into words
and it store in list format we can access it by index value
largest=words[0] = my 
shortest=words[0] = my
if 2 >2 false
if 2< 2 false

if 4 > 2 true largest=name 
if 4 < 2 false shortest=my 

if 2 > 4 false largest=name 
if 2 < 2 false shortest=my 

if 5 > 4 true largest=kirti
if 5 < 2 false shortest=my 



