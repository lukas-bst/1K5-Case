# 1Komma5° - Tech Case

## Beantwortung der Tech Case durch: Lukas Bauerschmidt
## Datum: 11.04.2023
## Verwendete Programmiersprache: Python

## Vorgehensweise:

1. Ergänzung des main.py Skripts mit Sandbox Zugangsdaten
   - Klone das GitHub Repository
   - Öffne die main.py Datei und ergänze die Zugangsdaten zur "Entwickler Sandbox OneCRM" (client_id, client_secret, refresh_token) in Zeile 8, 14, 15, 45, 46
   - Speichere die Datei ab

2. Überprüfung der Funktionalität des Skripts:
   - Navigiere über das Terminal zum Pfad des main.py Skripts: `$ cd pfad_zu_main.py`
   - Führe das Skript über das Terminal aus: `$ python main.py`
   - Ein neuer Lead sollte nun angelegt sein. Überprüfe dies in der "Entwickler Sandbox OneCRM"

3. Festlegung der täglich automatisierten Ausführung des main.py Skripts:
   1. Erstelle einen neuen Cronjob via Terminal (MacOS-Version):
      - Gebe hierzu folgenden Befehl im Terminal ein und ersetze unten stehende Paramter: `Minuten Stunde * * * pfad_zu_python_interpreter pfad_zu_main.py`
        - Lege die gewünschte tägliche Ausführungszeit (Format: Minuten Stunde * * *) fest, zu der die Leads in die "Entwickler Sandbox OneCRM" übertragen werden sollen: `30 9 * * *`
        - Ersetze "pfad_zu_python_interpreter" durch den eigenen Python Interpreter-Pfad
        - Ersetze "pfad_zu_main.py" durch den eigenen Pfad zur main.py-Datei
      - Beispiel Cronjob: `30 9 * * * /usr/bin/python3 /Users/Benutzer/Documents/main.py`
      - Nach der Ausführung des Befehls sollte zukünftig ein neuer Lead täglich um 9.30 Uhr in der "Entwickler Sandbox OneCRM" angelegt werden
   2. Hinweis: Stelle sicher, dass der Cronjob die erforderlichen Berechtigungen hat, um auf alle Dateien oder Verzeichnisse zuzugreifen, die vom Skript benötigt werden