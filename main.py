# myfile = open("test.txt", 'r')
# print(myfile)
# myfile.close()

# try:
#     somefile = open("test.txt", "w")
#     try:
#         somefile.write("hello ulan")
#     except Exception as e:
#         print(e)
#     finally:
#         somefile.close()
#         print("finally")
# except Exception as ex:
#     print(ex)

# with open("test.txt", "a")as somefile:
#     # somefile.write("\thello world")
#     print("hello, world", file=somefile)

# with open("test.txt", "r") as file:
    # for line in file:
    #     print(line, end="")
    # str1 = file.readline()
    # print(str1, end="")
    # str2 = file.readline()
    # print(str2, end="")
    # line = file.readline()
    # while line:
    #     print(line, end="")
    #     line = file.readline()
    # content = file.read()
    # print(content)
    # content = file.readlines()
    # print(content[1])
    # file = file.read()
    # print(text)

# filename = "msg.txt"
# msgs = []
# for i in range(4):
#     msg = input(f"enter srtring {i}:")
#     msgs.append(msg + "\n")
#
# print(msgs)
#
# with open(filename, "a") as file:
#     for msg in msgs:
#         file.write(msg)
#
# with open(filename) as file:
#     for msg in file:
#         print(msg, end="")

import csv

filename = "users.csv"
users = [
    ["tom", 28],
    ["alice", 23],
    ["bob", 34]
]
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)

with open(filename, "a", newline="")as file:
    user = ["sam", 31]
    writer = csv.writer(file)
    writer.writerow(user)


with open(filename, "r", newline="")as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"{row[0]} - {row[1]}")

