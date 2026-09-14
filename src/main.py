motor_capacity = 12

motor_count = int(input("How many motors are carrying the packages? "))

total_package_weight = int(input("How many kg of packages do we expect? "))

total_capacity = motor_count * motor_capacity

if total_package_weight <= total_capacity:
    print("Yes! The conveyor belt can carry the packages.")
else:
    print("No. The conveyor belt cannot carry the packages.")