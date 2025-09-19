### Homework 1: Network Client / Server.

People responsible for making this possible 
- Julian
- Eric
- Alvaro
- Ben


We are going to build a networked chat program. One user will run a chat program on one computer. Another user will run a chat program on a different computer. The two chat programs will connect and enable the two users to chat in real-time!


The assignment requires implementing a basic networked chat program using Python sockets.

---

### Files

* `chat_server.py`: The server program.
* `chat_client.py`: The client program.

---

You will need two separate terminal windows to run both the server and the client.

1.  **Run the server:**
    ```
    python chat_server.py <listen_port>
    ```
    Replace `<listen_port>` with the port number you want the server to listen on.

2.  **Run the client:**
    ```
    python chat_client.py <server_ip> <server_port>
    ```
    Replace `<server_ip>` with the IP address of the machine running the server and `<server_port>` with the port number the server is listening on.

---

Small GIF showing server and client communicating with each other

https://github.com/user-attachments/assets/92d0e970-be2c-4736-ba8e-500bc5f5946e

