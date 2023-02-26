# File Handling

# .txt file
import os

#txt_files = open("./my_files.txt", "w+")

#txt_files.write("Mi nombre es Brian\nMi apellido Almada\n 32 años\nY mi lenguaje favorito es Python")


#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())
#print(txt_file.readlines())
#for line in txt_file.readlines():
    #print(line)

#txt_files.write("\nAunque también me gusta JavaScript")
#print(txt_files.readlines())

#txt_files.close()
#os.remove("./my_files.txt")

# .json file

import json

json_file = open("./my_file.json", "w+")

json_test = {
    "name":"Brian",
    "surname":"Almada",
    "age": 32,
    "lenguge":["Python", "JavaScript", "PHP"]
}

json.dump(json_test, json_file, indent= 4)

json_file.close()

with open("./my_file.json") as my_other_file:
    for line in my_other_file.readline():
        print(line)

json_dict = json.load(open("./my_file.json"))
print(json_dict)
print(type(json_dict))

# .csv file
import csv

csv_file = open("./my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "languaje", "mail"])
csv_writer.writerow(["Brian", "Almada", 32, "Python", "brianalexisalmada84@gmail.com"])

csv_file.close()

whit open("./my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
    print(line)

