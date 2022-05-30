
# num=int(input("ENter the number"))
# sum=0
# temp=num
# while temp>0:
#     breakpoint()
#     rem=temp%10
#     sum=sum+rem*rem*rem
#     temp=temp//10
# if sum==num:
#     print("Number is armstrong number")
# else:
#     print("not armstrong number")


# low=int(input("ENter lower limit"))
# upper=int(input("Enter upper limit"))

# for num in range(low,upper+1): 
#     temp=num
#     sum=0
#     while temp>0:
#         rem=temp%10
#         sum=sum+rem*rem*rem
#         temp=temp//10
#         if sum==num:
#             print(num," Is armstrong number")

###to Reverse a number
num=int(input("Enter a number to be reversed"))
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev,"Is reversed number")
        

