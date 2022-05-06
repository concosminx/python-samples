#break and continue

cars = ["ok", "ok", "ok", "faulty", "ok"]

for status in cars:
    if (status == "faulty"):
        print("Stopping here!")
        break
    print(f"This car is {status}.")
    print("Shipping new car to customer!")

print("-------------------")

for status in cars:
    if (status == "faulty"):
        print("Skipping here, faulty!")
        continue
    print(f"This car is {status}.")
    print("Shipping new car to customer!")


print("-------------------")


#the else keyword with loops
cars = ["ok", "ok", "ok", "ok"]
for status in cars:
    if (status == "faulty"):
        print("Skipping here, faulty!")
        break
    print(f"This car is {status}.")
    print("Shipping new car to customer!")
else:
    print("All cars build successfully. No faulty cars!")