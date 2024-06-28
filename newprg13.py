kg=int(input("Enter your weight : "))
mt=int(input("Enter your height : "))

bmi=kg/(mt*mt)

if bmi < 18.5:
    print("underweight ")
elif (bmi>18.5) and (bmi<24.9):
    print("Normal ")
elif (bmi>25) and (bmi<30):
    print("overweight ")
elif(bmi>30):
    print("obese")