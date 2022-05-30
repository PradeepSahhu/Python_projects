# learning to open and write in the files of the system


data = input("Enter your words here for the file \n")
file = open(r"C:\Users\speci\Desktop\Python\second.txt", "a+")  # Absolute path
file.write(data)
file.flush()
file.seek(0)  # move the file pointer to the beginning of the file.
file_data = file.read(10)
print(file_data)

file.close()

