def what_to_wear(temp, rain):
    if temp < 50:
        print("Wear a coat, hat, scarf, and gloves")
    elif (temp >= 50 and temp <= 70) and rain == False:
        print("Wear a sweater or a light Jacket")
    elif (temp >= 50 and temp <= 70) and rain == True:
        print("Wear a rain Jacket and boots")
    elif (temp > 70) and rain == False:
        print("Wear a T-shirt and Shorts")
    elif (temp > 70) and rain == True:
        print("Wear a light jacket and rain boots")
