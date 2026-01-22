count = 0
with open(r"C:\Users\HP\Desktop\STUDENTS.txt", "r") as f1:
    for line in f1:
        count += 1
        print("numbers of students:", count)