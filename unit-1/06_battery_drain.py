#battery = 100
#minute = 0
#while battery>20:
    #minute += 1
    #print(f"low-battery alert after {minute} minutes({battery}%)")
    #break
#print("Alert")

while True:
    text = input("Enter battery%(0-100): ")
    value = float(text)
    if 0<=value<=100:
        break
    print("out of range, try again")
print("accepted :",value)
