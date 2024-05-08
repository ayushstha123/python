# an exception is an error that occurs during the execution of a program. When an exception occurs, Python raises an exception object, which can be caught and handled by code.
# try:
#     print(x)
# except:
#     print("There is an error")

#Name error
# an exception is an error that occurs during the execution of a program. When an exception occurs, Python raises an exception object, which can be caught and handled by code.
# try:
#     print(x)
# except NameError:
#     print("Name error means something is probably undefined")

#division by zero error
# x=0
# try:
#     # print(x/1)
#     if not type(x) is str:
#         raise TypeError("Only Strings are allowed")
# except NameError:
#     print("Name error means something is probably undefined")
# except ZeroDivisionError:
#     print("Please do not divide by zero")
# except Exception as error:
#     print(error)
# #lets say there is no error
# else:
#     print("No Error!")
# #finally (j garey ni run hunne error aye ni run na aye ni run huncha)
# finally:
#     print("Im going to print with or without an error")


#custom exception
class JustNotCoolError(Exception):
    pass
x=0
try:
    # print(x/1)
    # if not type(x) is str:
    #     raise TypeError("Only Strings are allowed")
    # raise Exception("Im a custom exception")
    raise JustNotCoolError("This is not cool Myan")
except NameError:
    print("Name error means something is probably undefined")
except ZeroDivisionError:
    print("Please do not divide by zero")
except Exception as error:
    print(error)
#lets say there is no error
else:
    print("No Error!")
#finally (j garey ni run hunne error aye ni run na aye ni run huncha)
finally:
    print("Im going to print with or without an error")
