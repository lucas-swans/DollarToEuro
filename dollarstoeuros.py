# Dollars to Euros
print("Dollars to Euros V1")
print("This program asks for a dollar input and converts it to Euros.")
print("Programmer: Lucas Swanstrom")

while True:
    #find out if user wants to convert again
    convert = input("would you like to convert: ")
    if convert == "yes":
        #find dollar amount and convert to euro
        dollar = float(input("Enter dollar amount to be converted "))
        euros = dollar * 0.9540

        print("Euros: €" + str(euros))
    #end loop if dont want to convert
    elif convert == "no":
        break