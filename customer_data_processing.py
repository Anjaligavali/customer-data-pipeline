# Read data from text file
with open("customer_data.txt", "r") as file:
    lines = file.readlines()

# Print raw data
print("Customer Data:\n")

for line in lines:
    print(line.strip())

print("\nProcessed Data:\n")



# Process records
for line in lines[1:]:
    
    data = line.strip().split(",")

    customer_id = data[0]
    customer_name = data[1]
    email = data[2]
    city = data[3].upper()
    membership = data[4]
    purchase_amount = int(data[5])

    # Calculate discount
    discount = purchase_amount * 0.10

    # Print transformed record
    print(
        f"{customer_id},{customer_name},{email},{city},{membership},{purchase_amount},{discount}"
    )
