dict ={
    "Alice":85,
    "jon":67,
    "sam":87,
    "rohit":97
}
name=input("Enter the student's name:")
if name in dict:
    print(f"{name}'s marks : {dict[name]} ")
else:
    print("student not found")
