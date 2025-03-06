my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

for key,value in my_vehicle.items():
    print(f"{key}: {value}")
    
    
vehicle2=my_vehicle
vehicle2["number_of_tires"]=4

vehicle2.pop("mileage")
print(vehicle2)



    
    