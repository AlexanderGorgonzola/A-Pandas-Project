#imports
import pandas as pd
import time
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
    user_input = input("\nAdd row or column to datatable?: ")
    if user_input.lower() == "q":
        print("\nThank you for trying this out!")
        break
    elif user_input.lower() == "row":
        if len(data.columns) == 0:
            print("\nPlease add a column first")
        else:
            print(f"\nThese are your current columns in order: {data.columns.tolist()}")
            print("\nplease specify the items you want in your rows (by columns)")
            items = []
            for names in data.columns:
                add = input(f"\n{names}: ")
                items.append(add)

            data.loc[len(data)] = items
            items = []

    elif user_input.lower() == "column":
        while True:
            column_name = input("\nWhat is its name?: ")
            if column_name in data.columns:
                print("\nThat name already exsists ;)")
                pass
            else:
                break
        if len(data) == 0:
            data.insert(len(data), column_name, [])
        else:
            hollow_purple = []
            for x in range(len(data)):
                hollow_purple.append("Nan")
            data.insert(len(data), column_name, hollow_purple)
            hollow_purple = []
            
    user_input = input("\nWould you like to view your data? (y/n): ")
    if user_input.lower() == "y":
        print(data.head())

    user_input = input("\nWould you like to save your data? (y/n): ")
    if user_input.lower() == "y":
        #make it look like its doing something
        print("Saving...")
        print("...")
        print("...")
        print("...")
        time.sleep(1)
        data.to_csv("data.csv", index=False)
        time.sleep(0.5)
        print("Leaving program...")
        time.sleep(0.5)
        break