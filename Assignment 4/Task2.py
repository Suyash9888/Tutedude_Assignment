file_name="output.txt"
with open(file_name,"w") as file1:
    written_text=input("Enter text to write to the file :")
    if file1.write(written_text):
        print("Data successfully written to",file_name,"\n")

with open(file_name ,"a") as file2:
    append_text=input("Enter additional text to append:")
    if file2.write("\n"+append_text):
        print("Data successfully appended.\n")

with open(file_name,"r+") as file3:
    print("Final content of",file_name,":")
    for line in file3:
        print(line.replace("\n", ""))