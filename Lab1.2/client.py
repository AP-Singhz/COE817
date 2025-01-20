import socket
from cipher import vigenere_encrypt, vigenere_decrypt

KEY = "TMU"

def start_client():
    host = '127.0.0.1'
    port = 22345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to server")

    while True:
        message = input("Enter your question for AaronAI (or type 'exit' to quit): ")
        if message.lower() == "exit":
            break

        # block of code below is used to get the function from the cipher.py file and encrypt the message
        encrypted_message = vigenere_encrypt(message, KEY)
        client_socket.send(encrypted_message.encode())
        print(f"Encrypted message sent: {encrypted_message}")

        # block of code below is used to get the function from the cipher.py file which will decrypt the encrypted message
        encrypted_response = client_socket.recv(1024).decode()
        print(f"Encrypted response from server: {encrypted_response}")
        decrypted_response = vigenere_decrypt(encrypted_response, KEY)
        print(f"Decrypted response from server: {decrypted_response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
