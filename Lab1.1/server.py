import socket
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
    question = question.lower().strip()
    return AARON_RESPONSES.get(question, "I am sorry, I don't understand your question?")

def start_server():
    host = '127.0.0.1'
    port = 54321

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server is listening on", host, port)

    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    while True:
        encrypted_message = conn.recv(1024).decode()
        if not encrypted_message:
            break

        print(f"Encrypted message from client: {encrypted_message}")
        decrypted_message = vigenere_decrypt(encrypted_message, KEY)
        print(f"Decrypted message from client: {decrypted_message}")

        # generate a response like siri which is predefined through my dictonary
        response = generate_response(decrypted_message)
        print(f"Siri response (plaintext): {response}")

        encrypted_response = vigenere_encrypt(response, KEY)
        conn.send(encrypted_response.encode())
        print(f"Encrypted response sent to client: {encrypted_response}")

    conn.close()

if __name__ == "__main__":
    start_server()
