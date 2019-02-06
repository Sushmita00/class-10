
#write a program that produces 3 different error and write handler for these error

try:
    number = input("enter the number")
    multi = number * a
    print("multi")
except NameError:
    print("a is not define")
except:
   print("define a")

try:
    name = input("enter the name")
    if name <= 3:
        print("enter the name again")
    else:
        print("name:", name)
except TypeError:
    print("'<=' not supported between instances of 'str' and 'int'")
except:
    print("convert 'str' into 'int'")

try:
    n = input("enter the number")
    if n % 2 == 0:
            print("numbers are even")
    else:
        print("numbers are odd")
except IndentationError:
    print("expected an indented block")
except:
    print("poblem with indentation")




#write a program that produces an error on name length less than 3
name=input("enter the name")
if len(name)<3:
    raise NameError
else:
    print("accepted")

#write a program that copies contant of one file to other file.

f=open('file.text','w')
f.writelines('python homework')
f.close()


#write a program that corrects this text
#Hello-this-is-a-text-file
name="Hello-this-is-a-text-file"
replace=name.replace("-"," ")
print(replace)

