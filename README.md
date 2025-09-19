### Homework 1: Network Client / Server.

We are going to build a networked chat program. One user will run a chat program on one computer. Another user will run a chat program on a different computer. The two chat programs will connect and enable the two users to chat in real-time!


The assignment requires the implementation of a basic networked chat program using Python sockets.

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

https://github.com/user-attachments/assets/c325f10e-dd89-44d8-85a8-89e898fcbc4b




