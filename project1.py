                                                                               #Building a calculator in python
#************************************************************************************************************************************************************************************
                                                            # Making sure Imputs are FLoats or returning Error and asking for a valid input till we get it.
while True:
    firstNumber = input("Enter a number: ")
    try:
        firstNumber = float(firstNumber)
        break
    except:
     print("Invalid Input! Try again")

while True:
    secondNumber = input("Enter a number: ")
    try:
        secondNumber = float(secondNumber)
        break
    except:
     print("Invalid Input! Try again")
     
#************************************************************************************************************************************************************************************
                                                                                 # Return error if the operation input is invalid 
while True:
     operation = input("Choose an Operation (Sum/Div/mul/Sub) : ").lower()
     if operation in ("sum", "div", "mul", "div"):
        break
     else:
         print("Invalid operation Try Again!")

#************************************************************************************************************************************************************************************
                                                                                        #defining operations
if operation == "sum":
     Result = firstNumber + secondNumber


elif operation == "sub":
        Result = firstNumber - secondNumber
   
elif operation == "div":
    # Handling div by Zero Error 
        if secondNumber != 0:
            Result = firstNumber / secondNumber
        else:
            print("∞")

elif operation == "mul":
        Result = firstNumber * secondNumber


#************************************************************************************************************************************************************************************
                                                                                        #Printing Result
if Result is not None:
    print("Result is: ", Result) 