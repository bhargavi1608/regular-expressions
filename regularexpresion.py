import re

# data = "sample data 9632587412 20/06/2024"
# pattern= re.compile(r"\d")    ''' give digits ''''

# res = re.finditer(pattern,data)

# for row in  res:
#     print(row)

#print(-------------------------------------------------------------------------------------)

# data = "sample data 9632587412 20/06/2024"
# pattern= re.compile(r"\D") ''' give other than digits ''''

# res = re.finditer(pattern,data)

# for row in  res:
#     print(row)

#print(-------------------------------------------------------------------------------------)

# data = "sample data 9632587412 20/06/2024"
# pattern= re.compile(r"\w") ''' give character but not space''''

# res = re.finditer(pattern,data)

# for row in  res:
#     print(row)

#print(-------------------------------------------------------------------------------------)

# data = "sample data 9632587412 20/06/2024"
# pattern= re.compile(r"\w+")    ''' select only word ''''

# res = re.finditer(pattern,data)

# for row in  res:
#     print(row)

#print(-------------------------------------------------------------------------------------)

# data = "sample data 9632587412 20/06/2024"
# pattern= re.compile(r"\W")  ''' other than char ''''

# res = re.finditer(pattern,data)

# for row in  res:
#     print(row)

#print(-------------------------------------------------------------------------------------)

# data = "sample data 9632587412 20/06/2024"
# pattern= re.compile(r"\s") ''' only spaces ''''

# res = re.finditer(pattern,data)

# for row in  res:
#     print(row)


#print(-------------------------------------------------------------------------------------)


# data = "sample data 9632587412 20/06/2024"
# pattern= re.compile(r"\S")    ''' except spaces ''''

# res = re.finditer(pattern,data)

# for row in  res:
#     print(row)

#print(-------------------------------------------------------------------------------------)

# data = "sample data 9632587412 20/06/2024" 
#  pattern= re.compile(r"\b")   #"check boundary"

# res = re.finditer(pattern,data)

# for row in  res:
#     print(row)

#print(-------------------------------------------------------------------------------------)

# data = "sample data " 
# pattern= re.compile(r"\B")    

# res = re.finditer(pattern,data)

# for row in  res:
#     print(row)

#print(-------------------------------------------------------------------------------------)

# data = "Sample data $ " 
# pattern= re.compile(r"[a-z]")    # Only small char

# res = re.finditer(pattern,data)

# for row in  res:
#     print(row)

#print(-------------------------------------------------------------------------------------)

# data = "Sample data $ " 
# pattern= re.compile(r"[A-Z]")    # Only Capital Character

# res = re.finditer(pattern,data)

# for row in  res:
#     print(row)

#print(-------------------------------------------------------------------------------------)


# data = "Sample data $ " 
# pattern= re.compile(r"[^A-Z]")    # other than capital letter

# res = re.finditer(pattern,data)

# for row in  res:
#     print(row)

#print(-------------------------------------------------------------------------------------)


# data = "Sample data $ " 
# pattern= re.compile(r"[^a-z]")    # other than small letter

# res = re.finditer(pattern,data)

# for row in  res:
#     print(row)


#print(-------------------------------------------------------------------------------------)

# data = "sample data 9632587412 "
# pattern= re.compile(r"\d\d")   # return one pair of numbers (96,32,58,74,12)

# res = re.finditer(pattern,data)

# for row in  res:
#     print(row)

#print(-------------------------------------------------------------------------------------)

# data = "sample data 9632587412 20/06/2024"
# pattern= re.compile(r"|") 

# res = re.finditer(pattern,data)

# for row in  res:
#     print(row)

#print(-------------------------------------------------------------------------------------)


# url validation
# file= open("example.txt","r")
# data=file.read()
# pattern= re.compile(r"(http|https)://[a-zA-Z0-9]{10}@iare.ac.in") 

# res = re.finditer(pattern,data)

# for row in  res:
#     print(row)



#print(-------------------------------------------------------------------------------------)


# file= open("example.txt","r")
# data=file.read()
# pattern= re.compile(r"[a-zA-Z0-9-_.]+@[a-z0-9]+\.[a-z.]+") 

# res = re.finditer(pattern,data)

# for row in  res:
#     print(row)

#print(-------------------------------------------------------------------------------------)

#  college rollno validation

# file= open("example.txt","r")
# data=file.read()
# pattern= re.compile(r"[0-9]{2}[0-9]{2}[0-9]{1}[A-Za-z]{1}[0-9]{2}[A-Z0-9a-z]{2}") 

# res = re.finditer(pattern,data)

# for row in  res:
#     print(row)


#print(-------------------------------------------------------------------------------------)

#Names Validation


# file= open("example.txt","r")
# data=file.read()
# pattern= re.compile(r"(Mrs|Mr|Ms)[. ]*\w+") 

# res = re.finditer(pattern,data)

# for row in  res:
#     print(row)

#print(-------------------------------------------------------------------------------------)

file= open("example.txt","r")
data=file.read()
pattern= re.compile(r"(?=[A-Z]+)(?=[a-z]+)(?=[0-9]+)(?=[!@#$%^&*(*)]+)") 

res = re.finditer(pattern,data)

for row in  res:
    print(row)