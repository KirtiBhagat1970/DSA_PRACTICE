str="Hello1234_"
vowels=consonent=digits=special=0
vowel_set=set('aeiouAEIOUE')
for char in str:
    if char.isalpha():
        if char in vowel_set:
            vowels+=1
        else:
            consonent+=1    
    elif char.isdigit():
        digits+=1
    elif not char.isspace():
        special+=1

print("vowels:",vowels)
print("consonent:",consonent)
print("digits:",digits)
print("special character:",special)

        