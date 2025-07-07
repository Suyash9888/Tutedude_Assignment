try:
    with open("sample.txt", "r") as file:
        print("Reading file content :")
        count=1
        for line in file:
            print("Line",count ,":",line)
            count = count + 1
except FileNotFoundError:
    print("Error : The file 'sample txt' not found.")