# 1 write a python program for a basic hello python program using the print function
print ("Hello, Python")

# 2 write a python program to demonstrate different datatypes in python int float complex str bool

x= 20 #int
print(x)
print(type(x))
x=20.5 #float
print(x)
print (type(x))
x=1j #complex
print(x)
print (type(x))
#String
x="Go EduHub.com"
print(x)
print(type(x))
x=True #bool
print(x)
print (type(x))
x=b"Hello" #bytes
print(x)
print(type(x))

# 3 write a python porgram to check biggest on two numbers
a,b=2,5
#get maximum of a,b
max=a if a>b else b
print (max)
a,b=2,5
print('Python')if a>b else print ('Examples')
a,b,c=15,93,22
#nested ternary operator
max =a if a>b and a>c else b if b<c else c
print(max)

# 4 write a program to compute distance between two points taking input from the user

#2b
x1=int(input("enter x1:"))
x2=int(input("enter x2: "))
y1=int(input("enter y1: "))
y2=int(input("entery2: "))
Result=((((x2-x1)**2)+((y2-y1)**2))**0.5)
print("distance between ",(x1-x2)and(y1,y2))

# 5 find the output for the following
#   a==b,a!=b,a<b,a>b,a<b,a>=b,a<=b
#   &b, a\b,a^b,~a,~b,a<<2,a>>2
#   a and b, a or b, not (a and b )

a=20
b=30
#relational operator
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)
#2
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(~b)
print(a<<2)
print(a>>2)
#3
print(a and b)
print(a or b)
print(not(a and b))

# 6 write a program to find the area of rectangle area and perimeter of square

#Area of rectangle
l=float(input("Enter the length of rectangle:"))
b=float(input("Enter the breadth of rectangle:"))
area=l*b
print("Area of rectangle is:",area)
#Area of square
a=float(input("Enter the length of side of square:"))
s_area=a*a
s_perimeter=4*a
print("Area of square is:",s_area)
print("Perimeter of square is:",s_perimeter)

# 7 write a program to create concatenate and print a string and accesing substring from given string

a="Python"
b="Programming"
print(a)
print("Concatenation of a and b is:",a+b)
print("The substring of a is:",a[0:4])

# 8 write a program to swap the value of two numbers using the third variable and without the third variable

#with using third variable
num1=int(input("Enter the value of first number:"))
num2=int(input("Enter the value of second number:"))
temp=num1
num1=num2
num2=temp
print("Value of num1 after swapping:",num1)
print("Value of num2 after swapping:",num2)
#Without using third variable
x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
x,y=y,x
print("After swapping:")
print("Value of x=",x,"Value of y=",y)

# 9 write a python program to input marks of five subjects physics chemistry biology maths and computer, calculate percentage

print("Enter the marks of five subjects::")
subject_1 = float (input ())
subject_2 = float (input ())
subject_3 = float (input ())
subject_4 = float (input ())
subject_5 = float (input ())
total, average, percentage, grade = None, None, None, None
# It will calculate the Total, Average and Percentage
total = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
average = total / 5.0
percentage = (total / 500.0) * 100
if average >= 90:
  grade = 'A'
elif average >= 80 and average < 90:
  grade = 'B'
elif average >= 70 and average < 80:
  grade = 'C'
elif average >= 60 and average < 70:
  grade = 'D'
else:
  grade = 'E'
# It will produce the final output
print(percentage)
print(grade)
print(average)
# 10 write a python program to print the follwing pattern N=5:

n=int(input("enter rows"))
if n%2 ==0:
  n+=1
  print(n)
print(n)
for i in range(n):
  if i== n2//2:
    print("*"*7)
  else:
    print("   *   ")
 
# 11 write a program to demonstrate working with tuples in python     

#Creating tuples with college names
colleges=("SIIET","BHARAT","GNIT","AVN")
print("The lists in colleges tuple is",colleges)
print("We can't add or remove new elements in a tuple")
print("Length of the tuple colleges is:",len(colleges))
#Checking whether 'SIIET' is present in the tuple or not
if "SIIET" in colleges:
  print("Yes,'SIIET' is in the colleges tuple")


# 12 write a program to demonstrate working with dictionaries in python

# Creating a dictionary
college = {"name": "SIIET","code": "INDI","id": "x3"}
for SIIET in college:
  print(college)
#Adding items to dictionary
college["location"] = "IBP"
print(college)
#Changing values of a key
college["location"] = "sheriguda"
print(college)
# To remove items
college.pop("code")
print(college)
#Know the length using len()
print("length of college is:",len(college))
#To copy the same dictionary use copy()
mycollege= college.copy()
print(mycollege)
  
# 13 write a program to create a list and perform the following methods:
# 1) insert() 2) remove() 3)append() 4)len() 5)pop() 6)clear()

a=[1,3,5,6,7,[3,4,5],"hello"]
print(a)
a.insert(3,20)
print(a)
a.remove(7)
print(a)
a.append("hi")
print(a)
len(a)
print(a)
a.pop()
print(a)
a.pop(6)
print(a)
a.clear()
print(a)

# 14 write a pogram to create a menu with the following options:
#  1 to perform additon 2 to perform subtraction 3 to perform multiplication 4 to perform division

def add(a, b):
    return a + b

def sub(c, d):
    return c - d

def mul(b, h):
    return b * h

def div(g, h):
    return g / h

print("=================")
print("1. TO PERFORM ADDITION")
print("2. TO PERFORM SUBTRACTION")
print("3. TO PERFORM MULTIPLICATION")
print("4. TO PERFORM DIVISION")
print("=================")

choice = int(input("Enter Your choice: "))

if choice == 1:
    a = int(input("Enter the 1st value: "))
    b = int(input("Enter the 2nd value: "))
    print(add(a, b))
elif choice == 2:
    c = int(input("Enter the 1st value: "))
    d = int(input("Enter the 2nd value: "))
    print(sub(c, d))
elif choice == 3:
    e = int(input("Enter the 1st value: "))
    f = int(input("Enter the 2nd value: "))
    print(mul(e, f))
elif choice == 4:
    g = int(input("Enter the 1st value: "))
    h = int(input("Enter the 2nd value: "))
    print(div(g, h))
else:
    print("Wrong choice")


# 15 write a python program to concatenate the dataframes with two objects

my_dict={'c':3,'a':1,'d':4,'b':2}
sorted_dict=sorted([(value,key)for(key,value)in my_dict.items()])
print("Sorted dictionary is :")
print(sorted_dict)
