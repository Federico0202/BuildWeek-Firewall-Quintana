import http.client

ip = input("IP del web server: ")
# per es. /phpMyAdmin/
path = input("Path: ")

verbi = ["GET", "POST", "PUT", "DELETE"]
abilitati = []

for verbo in verbi:
    conn = http.client.HTTPConnection(ip, 80, timeout=3)
    conn.request(verbo, path)
    risposta = conn.getresponse()
    print(verbo, risposta.status, risposta.reason)
    if risposta.status != 405:
         abilitati.append(verbo)
    conn.close()

print("Metodi abilitati:", abilitati)