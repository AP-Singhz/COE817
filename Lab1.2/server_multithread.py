import socket
import threading
from cipher import vigenere_encrypt, vigenere_decrypt

KEY = "TMU"

# dictionary of responses that i created
AARON_RESPONSES = {
    "hello": "Hello. How can I assist you today?",
    "what is your name": "I am AaronAI your friendly assistant.",
    "how are you": "I am just a program created by Aaron, but I'm functioning as expected!!!",
    "bye": "Goodbye!!!!!!!!! Have a great day",
}

def generate_response(question):
    question = question.lower().strip()  # Normalize question
    return AARON_RESPONSES.get(question, "I am sorry, I don't understand your question?")

def handle_client(conn, addr):
    print(f"Connection established with {addr}")

    while True:
        try:
            encrypted_message = conn.recv(1024).decode()
            if not encrypted_message:
                break

            print(f"Encrypted message from client {addr}: {encrypted_message}")
            decrypted_message = vigenere_decrypt(encrypted_message, KEY)
            print(f"Decrypted message from client {addr}: {decrypted_message}")

            response = generate_response(decrypted_message)
            print(f"Siri response for client {addr} (plaintext): {response}")

            encrypted_response = vigenere_encrypt(response, KEY)
            conn.send(encrypted_response.encode())
            print(f"Encrypted response sent to client {addr}: {encrypted_response}")

        except ConnectionResetError:
            print(f"Connection lost with client {addr}")
            break

    conn.close()
    print(f"Connection closed with {addr}")

def start_server():
    host = '127.0.0.1'
    port = 22345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Only allows upto 5 clients at one time due to requirements for the lab and no need to have more than 5 clients to show concurrency
    print(f"Server is listening on {host}:{port}")

    # where I use threading in order to handle different clients at the same time without messing up responses

    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

if __name__ == "__main__":
    start_server()
