# Zadanie4\_mwierzbi

Rozwiązanie zadania czwartego



Projekt zawiera automatyczny generator kodu (serializacja/deserializacja binarna danych) napisany w Pythonie przy użyciu szablonów Jinja2. Zawiera również dwa programy (Klient-Serwer) komunikujące się przez TCP/IP za pomocą wygenerowanego kodu.



interface.json - definicja przesyłanych danych

template.j2 - szablon kodu

generator.py - skrypt generujący plik "generated\_proto.py"

server.py - program serwera odbierający dane

client.py - program klienta wysyłający dane



Wymagania:

Wymagana biblioteka Jinja2

