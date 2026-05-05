import socket
import threading

client_count = 0
client_lock = threading.Lock()

def gaseste_ip_local():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        ip_local = s.getsockname()[0]
    except Exception:
        ip_local = '127.0.0.1'
    finally:
        s.close()
    return ip_local

def handle_client(conn, addr, client_number):
    try:
        conn.send("SERVER: Conexiune confirmata.".encode('utf-8'))

        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break

            srv_ip, srv_port = conn.getsockname()  # Datele serverului (ex: 8080)
            cli_ip, cli_port = conn.getpeername()  # Datele clientului (ex: 51797)

            # 1. În consola SERVERULUI: Afișăm pachetul de intrare (Sursa e Clientul)
            mesaj_server_consola = (f"{data} adresa ip sursa: {cli_ip} adresa ip destinatie: {srv_ip} "
                                    f"port sursa: {cli_port} port destinatie: {srv_port}")
            print(f"Mesaj client {client_number}: {mesaj_server_consola}")

            # 2. Pe ecranul CLIENTULUI: Afișăm pachetul de ieșire (Sursa devine Serverul)
            mesaj_pentru_client = (f"{data} adresa ip sursa: {srv_ip} adresa ip destinatie: {cli_ip} "
                                   f"port sursa: {srv_port} port destinatie: {cli_port}")

            raspuns_final = f"Mesaj server: {mesaj_pentru_client}"

            # 3. TRIMITERE UNICAST (Doar către acest client)
            try:
                conn.sendall(raspuns_final.encode('utf-8'))
            except Exception as e:
                print(f"Eroare la trimitere catre clientul {client_number}: {e}")
                break
    finally:
        # Scoatem clientul din evidență la deconectare
        conn.close()

def start_server():
    global client_count

    ip_automat = gaseste_ip_local()
    port_ales = int(input(f"Server pe {ip_automat}. Introdu portul: "))

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((ip_automat, port_ales))
    server.listen(5)
    print(f"SERVER: Ruleaza pe portul {port_ales}.")

    while True:
        conn, addr = server.accept()

        with client_lock:
            client_count += 1
            this_client_id = client_count

        thread = threading.Thread(target=handle_client, args=(conn, addr, this_client_id))
        thread.start()

if __name__ == "__main__":
    start_server()