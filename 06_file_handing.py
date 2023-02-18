# File Handling

# .txt file
import os

txt_files = open("./my_files.txt", "w+")

txt_files.write("Mi nombre es Brian\nMi apellido Almada\n 32 años\nY mi lenguaje favorito es Python")


#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())
#print(txt_file.readlines())
#for line in txt_file.readlines():
    #print(line)

txt_files.write("\nAunque también me gusta JavaScript")
print(txt_files.readlines())

txt_files.close()
os.remove("./my_files.txt")