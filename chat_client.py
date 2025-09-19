import socket, sys, select
from rawterm import RawTerminal

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <server_ip> <server_port>")
        sys.exit(1)
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])

    #connect
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_ip, server_port))
    print(f"[client] connected to {server_ip}:{server_port}")

    #event loop
    with RawTerminal(sys.stdin):
        inputs = [sys.stdin, sock]
        message_buffer = "" # characters typed in terminal will be added to message buffer
        while True:
            readable, _, _= select.select(inputs, [], [])
            for r in readable:
                if r is sys.stdin:
                    ch = sys.stdin.read(1) #read one char
                    # check if user does ctrl + c, if so, exit program
                    if ch == '\x03':
                        print("\nexiting program")
                        sys.exit(1)
                        break
                    # check if user does enter, if so, send message to client
                    if ch == '\r' or ch == '\n':
                        if message_buffer.strip(): # [client]: message
                            labeled_message = f"[client]: {message_buffer}\r\n"
                            sock.sendall(labeled_message.encode("UTF-8"))
                        sys.stdout.write('\r\n')
                        sys.stdout.flush()
                    else:
                        sys.stdout.write(ch)
                        sys.stdout.flush()
                    
                    sock.sendall(ch.encode("UTF-8"))
                else:
                    data = sock.recv(4096)
                    if not data:
                        print("\n[client] server closed, exiting")
                        return
                    sys.stdout.write(data.decode("UTF-8").replace('\n', '\r\n'))
                    sys.stdout.flush()

if __name__ == "__main__":
    main()