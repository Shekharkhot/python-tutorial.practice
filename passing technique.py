# passing technique is a phenomenon of providing the security to data while sending
# from one file to another file source to destination.
# there are 2 types Passing technique
# 1)json
# 2)pickle
# json is a passing technique which will keep the data securely by converting the original data in the form of string type.
# in this case we are going to make use of encryption process to convert data of one type to another type.
# syntax:
# import json
# variable = json.dumps(data)
# variable1 = json.loads(variable)

# encryption
import json

_fileopen = open('files3.txt', 'w')
data = (10, 20, 30, 40, 50)
encryption = json.dumps(data)
_fileopen.write(encryption)
_fileopen.close()

# decryption
import json

_fileopen = open('files3.txt', 'r')
result = _fileopen.read()
print(encryption)
output = json.loads(result)
print(output, type(output))
_fileopen.close()

# pickle is passing technique which is used to keep the data securely by converting the original data in the form of binary data
# in this case the original data will get encapsulated then we can send it to destination
# syntax
# import pickle
# variable_name = pickle.dumps(data)
# variable_name1 = pickle.loads(variable_name)

# encapsulation
import pickle

_fileopen = open('files4.txt', 'wb')
data = (10, 20, 30, 40, 50, 60, 70)
encapsulation = pickle.dumps(data)
_fileopen.write(encapsulation)
_fileopen.close()

# decapsulation
import pickle

_fileopen = open('files4.txt', 'rb')
encapsulation = _fileopen.read()
print(encapsulation)
result = pickle.loads(encapsulation)
print(result)
_fileopen.close()
