import socket
import pickle

cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

print("Client Started...")

IP_ADDRESS = "127.0.0.1"
PORT = 9000

cs.connect((IP_ADDRESS, PORT))

msg = input("Message To Server: ")
cs.send(msg.encode("ascii"))

data = cs.recv(1024).decode()
print("Message From Server: ", data)

data = cs.recv(1024)
data_array = pickle.loads(data)
print(data_array)

index = input("Enter index bw 0-3: ")
while index.lower().strip() != "bye":
    cs.send(index.encode("ascii"))
    value = input("Enter Value Between 1 -9: ")
    cs.send(value.encode("ascii"))

    data = cs.recv(1024)
    try:
        winner_message = data.decode()
        print(winner_message)
        break
    except UnicodeDecodeError:
        data_array = pickle.loads(data)
        print(f"Array Game After Client Deduction: {data_array}")

    data = cs.recv(1024)
    try:
        winner_message = data.decode()
        print(winner_message)
        break
    except UnicodeDecodeError:
        data_array = pickle.loads(data)
        print(f"Array Game After Server Deduction: {data_array}")

    index = input("Enter index bw 0-3 or type bye to end: ")

cs.close()
print("Client Closed...")
