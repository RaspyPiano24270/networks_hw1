import socket, sys, select

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
    inputs = [sys.stdin, sock]
    while True:
        readable, _, _ = select.select(inputs, [], [])
        for r in readable:
            if r is sys.stdin:
                line = sys.stdin.readlinn()
                if not line: #EOF
                    print("[client] stdin closed, exiting")
                    sock.shutdown(socket.SHUT_RDWR)
                    sock.close()
                    return
                sock.sendall(line.encode("UTF-8"))
            else:
                data = sock.recv(4096)
                if not data:
                    print("[client] server closed, exiting")
                    return
                #show what client typed
                sys.stdout.write(data.decode("UTF-8"))
                sys.stdout.flush()
if __name__ == "__main__":
    main()