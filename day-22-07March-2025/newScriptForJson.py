import json

FILE_NAME = "data.json"

# Function to read JSON file
def read_json():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to write data to JSON file
def write_json(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# CRUD Operations

# 1️⃣ Create (Add a new record)
def create_record(new_data):
    data = read_json()
    new_data["id"] = max([item["id"] for item in data], default=0) + 1  # Auto-increment ID
    data.append(new_data)
    write_json(data)
    print("Record added successfully!")

# 2️⃣ Read (Display all records)
def read_records():
    data = read_json()
    for item in data:
        print(item)

# 3️⃣ Update (Modify an existing record)
def update_record(record_id, updated_data):
    data = read_json()
    for item in data:
        if item["id"] == record_id:
            item.update(updated_data)
            write_json(data)
            print("Record updated successfully!")
            return
    print("Record not found!")

# 4️⃣ Delete (Remove a record)
def delete_record(record_id):
    data = read_json()
    new_data = [item for item in data if item["id"] != record_id]
    
    if len(new_data) == len(data):
        print("Record not found!")
    else:
        write_json(new_data)
        print("Record deleted successfully!")

# Menu-driven program
if __name__ == "__main__":
    while True:
        print("\nCRUD Operations on JSON File")
        print("1. Add Record")
        print("2. View Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            city = input("Enter city: ")
            create_record({"name": name, "age": age, "city": city})
        
        elif choice == "2":
            print("\nRecords in JSON file:")
            read_records()
        
        elif choice == "3":
            record_id = int(input("Enter record ID to update: "))
            name = input("Enter new name (leave blank to keep current): ")
            age = input("Enter new age (leave blank to keep current): ")
            city = input("Enter new city (leave blank to keep current): ")

            updated_data = {}
            if name:
                updated_data["name"] = name
            if age:
                updated_data["age"] = int(age)
            if city:
                updated_data["city"] = city

            update_record(record_id, updated_data)
        
        elif choice == "4":
            record_id = int(input("Enter record ID to delete: "))
            delete_record(record_id)
        
        elif choice == "5":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice! Please try again.")
