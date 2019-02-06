'''
#try:
a = int(input("enter the number"))
div = a / 0
print(div)
#except ZeroDivisionError:
   # print("nothing can be divided by zero")
#except:
   # print("some problem with your input")



    #creat error

age=int(input("enter the age"))
if age<18:
    raise ValueError
else:
    print("accepted")


    #user define error

class LowAgeError(Exception):
    def __init__(self):
      super(LowAgeError,self).__init__("Age should be greater than 18")
age=int(input("enter the age"))
if age<18:
    raise LowAgeError
else:
    print("accepted")



    #file handling
'''

f=open('File.txt','w')
f.writelines('IM \n SUSHMITA')
f.close()


with open("File.txt","r") as f:
    text= f.read()
print(text)

f=open('File.txt','a')
f.writelines("\n appended text")
f.close()
