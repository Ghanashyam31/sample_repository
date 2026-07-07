from datetime import datetime


dttime=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"Current date and time: {dttime}")
print("--------------------------")
for i in range(5):
    print("Value of i is: ", i)

print("--------------------------")    