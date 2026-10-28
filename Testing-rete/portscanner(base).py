# importa il modulo socket (modulo che da accesso all'interfaccia BSD)
import socket

# chiede IP all'utente
target = input("Inserire IP da scansionare: ")

while True:
    portrange = input("Inserire range di porte da scansionare (es: 6-7): ")
    # ricava le porte dall'input utente e le converte in numeri
    try:
    # int aggiunta necessaria per far accettare i numeri, 
    # dato che python converte in stringhe altrimenti
        lowport, highport = (int(portnmbr) for portnmbr in portrange.split("-"))
    # se input non valido, torna a while
    except ValueError:
        print("Input non valido, usare ad esempio 6-7.")
        continue
    # ricorda all' utente quali porte sono valide
    if not (1 <= lowport <= highport <= 65535) :
        print("Le porte valide sono 1-65535")
        continue
    #input valido, fine ciclo while
    break

# autoesplicativo
print(f"Sto scansionando {target} dalla porta {lowport} alla porta {highport}...")

for port in range((lowport), (highport) + 1):
    # crea un socket (ipv4,TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # non aspettare all'infinito (utile caso firewall), attesa 1s
    s.settimeout(1)
    # tenta la connessione al socket dell'ip, ritorna 0 se l'operazione ha successo
    status = s.connect_ex((target, port))
    # chiude il socket
    s.close()
    # controlla la situazione della porta confrontando gli errori (nr errori)
    # 1o nr linux, 2o nr windows
    if status == 0:
        result = "aperta"
    elif status in (111, 10061):
        result = "chiusa"
    elif status in (11, 10035):
        result = "timeout, forse filtrata dal firewall"
    else:
        result = f"Connessione fallita con codice: {status}"

    # stampa esito dello scan della porta
    print(f"Lo stato della porta {port} è: {result}.")