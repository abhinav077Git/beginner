# for i in range(1,13):
#     # print("No. {0} squared is {1} and cube is {2}".format(i,i**2,i**3))
#     print("No. {0:2} squared is {1:3} and cube is {2:4}".format(i,i**2,i**3))

name=input("what is your name: \n")
age=int(input("how old are you ,{0}:".format(name)))
if age>=18:
    print("Ok to vote!!")
else:
    print("please come in {0} years".format(18-age))