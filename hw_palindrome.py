s=input("Enter the string that you need to check:")
le=len(s)
if le%2==0:
    s1=s[:le//2]
    s2=s[-1:(le//2)-1:-1]
    print(s1,s2)
    if s1==s2:
        print("yes, given string is a palindrome")
    else:
        print("No, given string is not a palindrome")
else:
    s1=s[:le//2]
    s2=s[-1:le//2:-1]
    print(s1,s2)
    if s1==s2:
        print("yes, given string is a polindrome")
    else:
        print("No, given string is not a polndrome")
    
