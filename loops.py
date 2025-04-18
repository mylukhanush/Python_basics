#  execute the same set of logics multiple times like while loop or for loop
#
#(break, continue)
#For loop : is used to iterate over the elements of sequence like string, list, tuple, range etc

#syntax : for variable in sequence:
#            statement
#lets print numbers between 50-70 using for loop

#will print numbers between 50 to 70, range always exclude the upper limit
# for x in range(50,70):
#    print(x)

#stepping we elemenate every second step using stepping here#
# for x in range(50,71,2):
#    print(x)


# p=[1,2,3,4,5]
# product=1
#
# for x in p:
#     product*=x
# print(product)
#
# #multiplication of number:
#
#
# x=int(input("which number you want to multiple:"))
# for i in range(1,21):
#     print(i*x)
#
#
# x=int(input("which number you want to multiple:"))
# for i in range(1,21):
    # print(x,"X",i,"=",x*i)

#break statement: if the given value is in the sequence then it will break the loop else it continue

# z=[1,2,3,4,5,6,7,8]
# for i in z:
#     print(i)


# z = [1,2,3,4,5,6,7,8]  #we will use break only with condition
# for i in z:
#     if (i == 6):
#         break
#     print(i)


# While Loop

#while loop:
#syntax
#while condition :    #it will print until the condition is true , it will stop once condition is false
#    statement        #you can have multiple statements

#display 1 to 20 using while:

#odd number using while loop:

# m=int(input("enter min number:"))
# n=int(input("enter max number:"))
# while m<=n:
#     print(m)
    # m+=2


# m=int(input("enter min number:"))
# n=int(input("enter max number:"))
# i=m
# if i%2==0: i=m+1    # this condition will find m is even or odd and if m is evenit will add even number +1
# while i<=n:
#     print(i)
#     i+=2

#continue : is used to skip the value and print

# x=0
# while x<20:
#   x+=1
#   if x%3==0:
#     continue   #continue will skip that particular loop
#   print(x)