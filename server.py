import socket
import random
import pickle

N = 4

M = 9

arr = []

# def allZeros(arr)
def checkWinner(arr):
    for num in arr:
        if num != 0:
            return False
    return True


def generate(num):
    r = random.randint(0, num)
    return r
def generateArray():
    for i in range(N):
        r = random.randint(1, M)
        arr.append(r)

def pop(arr, N, indexClient, valueClient):
    if indexClient < 0 or indexClient > N:
        print("Index Error")
    if valueClient > arr[indexClient] or valueClient < 0:
        print("It Is Impossible to subtract less value ")
    else:
        arr[indexClient] = arr[indexClient] - valueClient
ss = socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM)

print("Server Started...")

IP_ADDRESS = "127.0.0.1"

PORT = 9000

ss.bind((IP_ADDRESS, PORT))

ss.listen(5)

connection, address  = ss.accept()
print(f"Client Connected With Address {address[0]} And Port Number {address[1]}")

data = connection.recv(1024).decode()
print("Message From Client: ", data)

msg = input("Message To Client: ")
connection.send(msg.encode("ascii"))

generateArray()
print(arr)
data_array = pickle.dumps(arr)
connection.send(data_array)
while True:
 indexClient = connection.recv(1024).decode()
 indexClient = int(indexClient)
 valueClient = connection.recv(1024).decode()
 valueClient = int(valueClient)

 indexServer = generate(3)
 valueServer = generate(4)

# print(indexServer)

 print(f"Index Client {indexClient} and Value Client {valueClient}")
 print(f"Index Server {indexServer} and Value Server {valueServer}")

 pop(arr, N, indexClient, valueClient)
 winner = checkWinner(arr)
 if winner == True:
     print("Client Wins")
     break
 print("Array Game After Deduction Of Client: ", arr)
 data_arr = pickle.dumps(arr)
 connection.send(data_arr)
 pop(arr, N, indexServer, valueServer)
 winner = checkWinner(arr)
 if winner == True:
     print("Server Wins")
     break
 print("Array Game After Deduction Of Server: ", arr)
 data_arr = pickle.dumps(arr)
 connection.send(data_arr)