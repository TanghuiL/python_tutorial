#!/usr/bin/python3
import math
# n = 600851475143
n=int(input("Enter an integer:"))
print("Factors are:")
i=1
while(i<=math.ceil(n**0.5)):
    k=0
    if(n%i==0):
        j=1
        while(j<=i):
            if(i%j==0):
                k=k+1
            j=j+1
        if(k==2):
            print(i)
    i=i+1