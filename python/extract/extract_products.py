import csv #built in module
file_path = "data/raw/products.csv" #storing the path in a var

#opens file in read mode
with open(file_path, mode="r") as file: 
#reads the file as a dict instead of a list
'''"DictReader automatically maps each column to its header, making the code more readable and less error-prone. Instead of remembering column positions like row[2], I can access values by meaningful names such as row['category']."'''
    reader = csv.DictReader(file)
    #loops iterates and prints
    for row in reader:
        print(row)

#print("------------")
#print(row["product_name"])
'''if we had to print just the product name we would have just placed this instead of row'''