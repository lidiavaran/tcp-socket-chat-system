# Multi-threaded TCP Chat (Broadcast System)

Acest proiect conține o implementare de tip Client-Server în Python, utilizând socket-uri TCP și multithreading. Sistemul permite conectarea mai multor clienți simultan la un server central care distribuie mesajele primite către toți participanții în timp real.

## 🛠️ Detalii Tehnice

Proiectul este compus din două module principale care gestionează fluxul de date:

### 1. Server (`server.py`)
* **Detecție IP:** Identifică automat adresa IP locală a mașinii pentru a facilita conexiunea în rețeaua locală.
* **Gestionare Clienți:** Folosește o listă (`lista_clienti`) și un mecanism de sincronizare (`threading.Lock`) pentru a gestiona conexiunile simultane în siguranță și a evita conflictele de memorie.
* **Logare Metadate:** Extrage și afișează IP-ul și portul sursă/destinație pentru fiecare pachet procesat folosind metodele `getsockname()` și `getpeername()`.

### 2. Client (`client.py`)
* **Full-Duplex Communication:** Implementează un thread separat (`primeste_mesaje`) dedicat recepției de date, permițând utilizatorului să vadă mesajele noi de la ceilalți membri în timp ce introduce text propriu.
* **Interfață:** Rulează în terminal și gestionează fluxul de date asincron până la închiderea conexiunii prin comanda `exit`.

## 🚀 Instrucțiuni de Rulare

1. **Pornire Server:**
   - Deschideți un terminal și rulați:
     ```bash
     python3 server.py
     ```
   - Introduceți portul dorit (ex: `8080`).

2. **Pornire Clienți:**
   - Deschideți terminale noi (unul pentru fiecare client) și rulați:
     ```bash
     python3 client.py
     ```
   - Introduceți același port configurat la server.

## 📊 Exemplu de Output în Consolă

### Ce apare pe Server (Pachetul primit de la client):
```text
Mesaj client 1: salut adresa ip sursa: 192.168.1.5 adresa ip destinatie: 192.168.1.5 port sursa: 51794 port destinatie: 8080
```
### Ce văd Clienții (Pachetul redistribuit de server):
```text
Mesaj server: salut adresa ip sursa: 192.168.1.5 adresa ip destinatie: 192.168.1.5 port sursa: 8080 port destinatie: 51794
```


