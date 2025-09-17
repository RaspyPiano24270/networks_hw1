import socket, sys, select
from rawterm import RawTerminal

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <port>")
        sys.exit(1)
    listen_port = int(sys.argv[1])

    #create, bind, listen
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("0.0.0.0", listen_port))
    srv.listen(1)
    print(f"[server] listening on 0.0.0.0:{listen_port} ...")

    #accept one client for assignment
    conn, addr = srv.accept()
    print(f"[server] connected by {addr}")

    #event loop
    with RawTerminal(sys.stdin):
        inputs = [sys.stdin, conn]
        while True:
            readable, _, _ = select.select(inputs, [], [])
            for r in readable:
                if r is sys.stdin:
                    ch = sys.stdin.read(1) #read one char
                    # check if user doesc ctrl + c, if so, exit program
                    if ch == '\x03':
                        print("\nexiting program")
                        srv.close()
                        sys.exit(0)
                        break
                    if ch == '\r' or ch == '\n':
                        sys.stdout.write('\r\n')
                        sys.stdout.flush()
                    else:
                        sys.stdout.write(ch)
                        sys.stdout.flush()
                    conn.sendall(ch.encode("UTF-8"))
                else:
                    data = conn.recv(4096)
                    if not data:
                        print("\n[server] peer closed, exiting")
                        return
                    sys.stdout.write(data.decode("UTF-8"))
                    sys.stdout.flush()

if __name__ == "__main__":
    main()