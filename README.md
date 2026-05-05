# Multi-threaded TCP Chat (Broadcast)

Acest proiect conține o implementare de tip Client-Server în Python, utilizând socket-uri TCP și multithreading. Sistemul permite conectarea mai multor clienți simultan la un server central care distribuie mesajele primite către toți participanții.

## 🛠️ Detalii Tehnice

Proiectul este compus din două module principale:

### 1. Server (`server.py`)
* **Detecție IP:** Utilizează un socket UDP temporar pentru a identifica adresa IP locală a mașinii.
* **Gestionare Clienți:** Folosește o listă (`lista_clienti`) și un mecanism de blocare (`threading.Lock`) pentru a gestiona conexiunile în siguranță.
* **Broadcast:** Mesajele primite de la un client sunt retransmise către toate socket-urile active din listă.
* **Logare Metadate:** Extrage și afișează IP-ul și portul sursă/destinație pentru fiecare pachet procesat folosind `getsockname()` și `getpeername()`.

### 2. Client (`client.py`)
* **Full-Duplex:** Folosește un thread separat (`primeste_mesaje`) pentru a asculta pachetele de la server în timp ce utilizatorul poate introduce text.
* **Interfață:** Rulează în consolă și permite trimiterea de mesaje până la introducerea comenzii `exit`.

## 🚀 Instrucțiuni de Rulare

1. **Porniți Serverul:**
   ```bash
   python3 server.py

   Introduceți portul pe care doriți să asculte serverul.

    Porniți Clienții:
   ```bash
   python3 client.py

   Introduceți același port configurat la server.

📊 Exemplu de Log (Consolă)
Când un client trimite un mesaj, serverul afișează:
Mesaj client 1: [mesaj] adresa ip sursa: [IP_CLIENT] adresa ip destinatie: [IP_SERVER] port sursa: [PORT_DINAMIC] port destinatie: [PORT_SERVER]   
Tehnologii: Python, Sockets, Multithreading (TCP/IP stack)
   
