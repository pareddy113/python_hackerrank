#Avinash Reddy Penugonda
#Richie Rich Problem from Hackerrank
#!/bin/python3
import sys
n=int(input("Number of digits in the number="))
k=int(input("Maximum number of digits that can be altered="))
number=int(input("Enter the string of numbers="))
b=n//2
c=n/2
def strtoarray(n):		#converting a number string into array
    b=str(n);
    a=[];
    for i in b:
        a.append(i);
    return a;

def arraytoint(n):		#converting an array to number string
    string='';
    for j in n:
        string=string+j;
    return int(string);
def palindrome(a):		#check if the array is a palindorme or not
    count=0;
    for i in range(len(a)//2):
        if(a[i]!=a[-i-1]):
            count=count+1;
    return count;

v1=strtoarray(number);          #convert number to array
v=palindrome(v1);               #check the number of indices that differ to be a palindrome
array=(strtoarray(number));     #convert string to array

if(k>=n):	                #condition for number of digits to be altered greater the size of the number
    string='';						
    for i1 in range(0,n):
        string=string+'9';      #all digits must be 9
        k=k-1;
    print (int(string));
elif (k>=v):                    #Condition for number of digits to be altered is greater than count from paldindrome
    for i in range(0,b):
        pal=palindrome(array[i:n-i]);
        if(k>pal and k>0):
            if(pal==0 and k==1):		
                break;
            elif((array[i]=='9' or array[-i-1]=='9') and ((array[i] and array[-i-1]!='9'))):
                array[i]=array[-i-1]='9';
                k-=1;
            elif((array[i]!='9' and array[-i-1]!='9') and palindrome(array[i+1:n-i-1])<=k-2):
                array[i]=array[-i-1]='9';
                k-=2;
        elif((k==pal) and k>0):     #Condition for number of digits to be altered is equal to count from paldindrome
            if array[i]!=array[-i-1]:
                y=max(array[i],array[-i-1]);
                array[i]=array[-i-1]=y;
                k-=1;
    if((k==1 and n%2!=0)):          
           array[b]='9'
           print(array)
    print(arraytoint(array))
else:				#print -1 if all the above conditions fail (if largest number not possible)
    print ("-1")
        
