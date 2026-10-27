import http.client
# inserisci l'ip di Metasploitable
ip = input("IP del web server: ")
# inserisci il path della porta 80, quindi /phpMyAdmin/
path = input("Path: ")
# lista dei verbi da provare
verbi = ["GET", "POST", "PUT", "DELETE"]
# lista vuota dove metteremo i verbi che il server accetta
abilitati = []
# ciclo for (ripetizione per ogni verbo della lista)
for verbo in verbi:
    # apro una connessione IP vero la porta 80, con attesa di 5 secondi
    conn = http.client.HTTPConnection(ip, 80, timeout=5)
    # mando al server la richiesta con il verbo
    conn.request(verbo, path)
    risposta = conn.getresponse()
    print(verbo, risposta.status, risposta.reason)
    # se il codice è diverso da 405, considero il verbo abilitato
    if risposta.status != 405:
         abilitati.append(verbo)
    conn.close()

print("Metodi abilitati:", abilitati)