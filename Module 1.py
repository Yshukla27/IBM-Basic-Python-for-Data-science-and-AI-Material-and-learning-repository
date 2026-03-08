print('Hello World!!\n This Is My first Professional Course!!!')
#What is the value of z where z = 2 + 15?
z=2+15
print(z)
#Typecasting and datat-type check
int("3.14")
float("433542.24352")
char(5.55454)
type(343)
type("Hello!!")
type(float("234343"))

# Store value into variable and uppend new info in the previosly created variable.

x = 43 + 60 + 16 + 41
print(x)
x=x/60
print(x)

x=55-5
x=x/10
x
#Strings
name='String is king'
print(name[0])
print(name[10])
print(name[-1])
print(name[-13])
name[0:4]
name[8:12]
name[::2]
name[0:5:2]
statement = name + " is the best album"
statement
e = 'clocrkr1e1c1t'
len(e)
e[0:13:2]
g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
g.find('snow')
g.replace('Mary','Bob')
import re
s3 = "House number- 1105"

result = re.search(r"\d", s3)

# Check if a match was found
if result:



    
    print("Digit found")
else:
    print("Digit not found.")
len("The BodyGuard")

## Practice codes.

a = "Sup chat, Im admin, this is me code"
print(a.upper())
print(a.lower())
print(len(a))
print(a.split())

a = "python"
print(a[0:3])


x=int(input("Please Enter your age:")) 
y=int(input("Please Enter the current year:")) 
age = y-x 
age2= x*365 
age3= age2*86400 
print(f"You were born in: {age}\n You have lived a total days:{age2} and a total this many seconds in this dod gamn planet:{age3}")


a = "Sup bud, Im yash, this is me code"
print(a.split())
print(a.replace('yash','****'))

word=str(input("Enter the string:")).lower()
if word==word[::-1]:
    print("Palindrome true")
else:
    print("Palindrome False")



