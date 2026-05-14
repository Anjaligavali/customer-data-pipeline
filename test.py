import pandas as pd

data = {
    "customer_id": [1, 2, 3, 4],
    "name": ["Anjali", "Rahul", "Priya", "Amit"],
    "email": ["a@gmail.com", "r@yahoo.com", "p@outlook.com", "amit@gmail.com"],
    "age": [25, 30, None, 40],
    "city": ["Pune", "Mumbai", "Delhi", None]
}

# Create DataFrame
df = pd.DataFrame(data)

print("RAW DATA")
print(df)

# Data Cleaning 
df["age"] = df["age"].fillna(df["age"].mean())
df["city"] = df["city"].fillna("Unknown")

# Transform Step
df["email_domain"] = df["email"].apply(lambda x: x.split("@")[1])


print(df)

#output layer
df.to_csv("customer_output.csv", index=False)

print("\nPipeline Completed Successfully")