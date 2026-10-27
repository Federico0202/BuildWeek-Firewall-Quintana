import http.client
# inserisci l'ip di Metasploitable
ip = input("Inserisci l'IP del web server: ")
# inserisci il path della pagina da testare, per esempio /phpMyAdmin/
path = input("Inserisci il Path: ")
# lista dei verbi da provare
verbi = ["GET", "POST", "PUT", "DELETE"]
# lista vuota dove metteremo i verbi che il server accetta
abilitati = []
# ciclo for (ripetizione per ogni verbo della lista)
for verbo in verbi:
    # apro una connessione IP verso la porta 80, con attesa massima di 5 secondi
    conn = http.client.HTTPConnection(ip, 80, timeout=5)
    # mando al server la richiesta con il verbo
    conn.request(verbo, path)
    risposta = conn.getresponse()
    print(verbo, risposta.status, risposta.reason)
    # se il codice è compreso tra 200 e 299, considera i verbi abilitati (Il server ha accettato la richiesta e non ha dato errore)
    if 200 <= risposta.status < 300:
        abilitati.append(verbo)
    conn.close()

print("Metodi abilitati:", abilitati)