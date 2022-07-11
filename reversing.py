number = input("Enter a number")

a = 200
b = 0

a = a/2
a = a-7
a += 1

b += 1
b = b*70
b = b+12
b -= 1

m = "FLAG:"
q = "MUcH"
w = "Le$$"
e = "shHsH"
r = "ReAd"
t = "wAtcH"
y = "NoT"
u = "tV"
i = "f1lm"
o = "B0oK"
p = "d0"
s = "pWd"
d = "C0mPuTeR"
f = "12345"
g = "54321"
h = "AbCdE"
j = "..."

if b < number < a:
    if number % 2 == 0:
        if number == 88:
            word = j+f+d+u+e
            print j+f+d+u+e
        elif number == 84:
            word = s+r+o+j+g
            print s+r+o+j+g
        elif number == 90:
            word = t+h+d+i+y
            print t+h+d+i+y
        else:
            word = q+w+e+r+t
            print q+w+e+r+t
    else:
        if number == 93:
            word =  y+s+h+o+e
            print y+s+h+o+e
        elif number == 87:
            word = m+r+w+u+e
            print m+r+w+u+e
        elif number == 91:
            word = t+h+d+i+y
            print t+h+d+i+y
        else:
            word = q+w+e+r+t
            print q+w+e+r+t
else:
    print "Nice try, but you have failed"
