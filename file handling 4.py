#with open (r"C:\Users\HP\Desktop\STUDENTS.txt", "r") as f1:
#    content = f1.read()
  #SS  print(content)

# question 3
#with open (r"C:\Users\HP\Desktop\STUDENTS.txt", "r") as f1:
 #   content = f1.readline()
  #  print(content)

# question 4
#with open (r"C:\Users\HP\Desktop\STUDENTS.txt", "r") as f1:
 #   content = f1.readlines()
  #  print(content)

# question 5
#with open(r"C:\Users\HP\Desktop\STUDENTS.txt", "r") as f1:
 #   for line in f1:
  #      print(line.strip())

# question 6
# # with open (r"C:\Users\HP\Desktop\STUDENTS.txt", "r") as f1:
#     count = 0
#     for line in f1:
#         count += 1
#     print("Total number of lines:", count)
    
# question 7
# with open (r"C:\Users\HP\Desktop\STUDENTS.txt", "r") as f1:
#     for line in f1:
#         data = line.split(",")
#     print(data[1].strip())

# question 9
# with open(r"C:\Users\HP\Desktop\STUDENTS.txt", "r") as f1:
#     for line in f1:
#         parts = line.strip().split(",")
#         price = int(parts[2])
#         if price > 10000:
#             print(line.strip())

# Question 10 
# file = open("C:\\Users\\HP\\Desktop\\STUDENTS.txt", "r")
# print(file.read())
# file.close()

#question 11
# file = open(r"C:\Users\HP\Desktop\STUDENTS.txt", "a")
# file.write("P204, Fan, 3500, Electronics\n")
# file.close()

# question 12
# file = open(r"C:\Users\HP\Desktop\STUDENTS.txt", "r")
# print(file.read())
# file.close()

#question 13
# file = open(r"C:\Users\HP\Desktop\STUDENTS.txt", "r+")
# data = file.read()
# data = data.replace("Mouse", "Wireless Mouse")

# file.seek(0)
# file.write(data)
# file.truncate()
# file.close()

# question 14
# file = open(r"C:\Users\HP\Desktop\STUDENTS.txt", "r+")
# file.seek(0, 2)   # move cursor to end
# file.write("\nP205, Bed, 45000, Furniture")
# file.close()

# file = open(r"C:\Users\HP\Desktop\STUDENTS.txt", "r")
# count = 0

# for line in file:
#     data = line.strip().split(",")
#     if data[3].strip() == "Electronics":
#         count += 1

# print("Total Electronics products:", count)
# file.close()

# question 15
source = open(r"C:\Users\HP\Desktop\STUDENTS.txt", "r")
target = open(r"C:\Users\HP\Desktop\expensive_products.txt", "w")

for line in source:
    data = line.strip().split(",")
    if int(data[2]) > 20000:
        target.write(line)

source.close()
target.close()
