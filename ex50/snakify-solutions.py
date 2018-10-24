#UNIT 1

#-------------------

#Sum of three numbers
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

#Hi John
name = input() 
print('Hi ' + name )

#Square
a = int(input())
b = (a ** 2)
print(b)

#Area of right-angled triangle
a = int(input())
b = int(input())
c = ((a * b)/2)
print(c)

#Hello, Harry!
name = input()
print("Hello, " + name + "!")

#Apple sharing
n = int(input())
k = int(input())
print(k // n)
print(k % n)

#Previous and next
a = int(input())
b = str(a + 1)
c = str(a - 1)
print("The next number for the number", a, "is " + b + ".")
print("The previous number for the number", a, "is " + c + ".")

#Two timestamps
a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = int(input())
z = int(input())
s = ((a*3600) + (b*60) + (c))
t = ((x*3600) + (y*60) + (z))
print(t - s)

#School desks
a = int(input())
b = int(input())
c = int(input())
print(a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)

#UNIT 2

#-------------------

#Last digit of interger
x = int(input())
print(x%10)

#Tens digit
a = int(input())
b = (a % 100)
c = (a % 10)
print((b-c)/10)

#Sum of digits
a = int(input())
b = (a % 1000)
c = (a % 100)
d = (a % 10)
x = ((b-c)/100)
y = ((c-d)/10)
z = (a%10)
print(x + y + z)

#Fractional part
a = float(input())
print(a % 1)

#First digit after decimal point

#Car route

#Digital clock

#Total cost

#Clock face - 1

#Clock face - 2

#UNIT 3

#-------------------

#Minimum of two numbers
a = int(input())
b = int(input())
if a < b:
    print(a)
else:
    print(b)
    
#Sign function
a = int(input())
if a > 0:
    print(1)
elif a < 0:
    print(-1)
if a == 0:
    print(0)

#Minimum of three numbers
a = int(input())
b = int(input())
c = int(input())
if b >= a <= c:
    print(a)
elif a >= b <= c:
    print(b)
else:
    print(c)

#Equal numbers
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)

#Rook move
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')

#Chess board - same color

#King move

#Bishop move

#Queen move

#Knight move

#Chocolate bar

#Leap year


