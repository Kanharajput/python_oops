import re
'''
kanha="kon hai be tu"
tomar=re.findall("^\w",kanha) #^this is only for one character 
obeta=re.findall("\w",kanha) # it will separate th ewords if + sign is there then it run for htew whole string
abe=re.findall("\w+",kanha)
beta=re.findall("^\w+",kanha) # plus take all the characters of the first word
print(tomar)
print(obeta)
print(abe)
print(beta)


# AB BARI AATI HAI SPLIT KARKE DEKHNE KI SO HAVE YOU READY FOR IT

kanha="teri meri zindagi me hai fulo ki bagiya"
tomar=re.split("t",kanha)
kake=re.split("e",kanha)
print(tomar)   # after split it will add the forward words to the next word
print(kake)


#finding in a list 

kanha=["aaj din aasmani hai","aa kabhi haveli per","Aao yrrr who let the fuck of coming out"]
for element in kanha:
    tomar=re.match("(a\w+)",element)
    #tomar=re.match("(a\w+)\W(a\w+)",element)
    rajput=re.match("(A\w+)",element)
    print(tomar)
    print(rajput)

    #if tomar:
    #   print((tomar.groups()))

# using findall we can find what w want

kanha="knaharajput91@gmail.com, babukasona@chutiya.com"
emails = re.findall('[\w\.-]+@[\w\.-]+',kanha)

for email in emails:
    print(email)
'''

# using search it work on list
kanha=['harley davidson','bullet 350 cc']
tomar='harley davidson is good'

for like in kanha:
    print('looking for "%s" ->' % (kanha,tomar),end=' ')

    if re.search(kanha,tomar):
        print("found a match!")

    else :
        print("no match found")
