import socket
import threading

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

def primeste_mesaje(client_socket):
    while True:
        try:
            raspuns = client_socket.recv(4096).decode('utf-8')
            if not raspuns:
                break

            print(f"\n{raspuns}")

            print("Introdu mesajul: ", end="", flush=True)
        except:
            break

def start_client():
    ip_detectat = gaseste_ip_local()
    server_port = int(input(f"Conectare la {ip_detectat}. Introdu portul serverului: "))

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((ip_detectat, server_port))



        welcome = client.recv(1024).decode('utf-8')
        print(welcome)


        thread_receptie = threading.Thread(target=primeste_mesaje, args=(client,), daemon=True)
        thread_receptie.start()


        while True:
            mesaj = input("Introdu mesajul: ")
            if mesaj:
                client.sendall(mesaj.encode('utf-8'))
            if mesaj.lower() == 'exit':
                break

    except Exception as e:
        print(f"Eroare: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    start_client()


