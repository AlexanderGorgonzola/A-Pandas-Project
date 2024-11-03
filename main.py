#imports
import pandas as pd
try:
    data = pd.read_csv("data.csv")
except pd.errors.EmptyDataError:
    data = pd.DataFrame({})

#settings
pd.set_option("display.max_columns", 30)
pd.set_option("display.max_rows", 30)

#main
print("Welcome to something were you can create your very own datatable!\nInput 'q' anytime to quit")
while True:
    user_input = input("Add row or column to datatable?: ")
    if user_input.lower() == "q":
        print("Thank you for trying this out!")
        break
    elif user_input.lower() == "row":
        if len(data.columns) == 0:
            print("Please add a column first")
    elif user_input.lower() == "column":
        while True:
            column_name = input("What is its name?: ")
            if column_name in data.columns:
                print("That name already exsists ;)")
                pass
            else:
                break
        data.insert(len(data), column_name, [])
        
    user_input = input("Would you like to view your data? (y/n): ")
    if user_input.lower() == "y":
        print(data)