pin="0805"
pin2=input("Enter the PIN code: ")
i=1
while pin2!=pin and i<3:
    print("Incorrect")
    pin2=input("Enter the PIN code: ")
    i=i+1;
    if i==3:
        print("Sorry, your payment card has been blocked.")
