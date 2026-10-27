import http.client
# inserisci l'ip di Metasploitable
ip = input("Inserisci l'IP del web server: ")
# inserisci il path della pagina da testare, quindi /phpMyAdmin/
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
    # se il codice non è compreso tra 405, 404, 403 o 501, considero il verbo abilitato
    if risposta.status not in [405, 404, 403, 501]:
        abilitati.append(verbo)
    conn.close()

print("Metodi abilitati:", abilitati)