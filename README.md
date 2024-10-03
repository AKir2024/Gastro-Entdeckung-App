# Gastro-Entdeckung-App
Bars/Restaurants finden die ihren speziellen Bedürfnissen entsprechen

by Alexey Kirchner 

Kurs: Entwicklung von Web-Anwendungen bei Herrn Prof. Dr Alexander Eck

Dokumentation: https://akir2024.github.io/Gastro-Entdeckung-App/

Dies ist eine auf Flask basierende Webanwendung, die es regelmäßigen Restaurantbesuchern ermöglicht, Restauranttipps zu teilen und nach ihnen zu suchen. Die Anwendung umfasst Funktionen wie Benutzerregistrierung, Login, das Hinzufügen von Tipps, das Suchen nach Tipps anhand spezifischer Kriterien und das Festlegen von Präferenzen.

## Funktionen

- Benutzerregistrierung und Login
- Hinzufügen von Restauranttipps mit Details (Name, Küche, Preisklasse, Atmosphäre)
- Suche nach Tipps mit mehreren Kriterien
- Festlegen und Aktualisieren von Präferenzen 
- Anzeige detaillierter Informationen zu jedem Restauranttipp

## Voraussetzungen

- Python 3.7+
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- Flask-Bcrypt
- Flask-Login

## Installation

1. Dieses Repository klonen:
   ```
   git clone https://github.com/AKir2024/Gastro-Entdeckung-App
   cd Gastro-Entdeckung-App

   ```

2. Erstellen und Aktivieren einer virtuellen Umgebung:
   ```
   python -m venv venv
   source venv/bin/activate  # Unter Windows: `venv\Scripts\activate`
   ```

3. Installieren der erforderlichen Pakete:
   ```
   pip install flask flask-sqlalchemy flask-wtf flask-bcrypt flask-login
   ```
4. Installiere das Modul requests:
   ```
   pip install requests
   ```
5. Installiere Paket:
  ```
   pip install email_validator
   ```
   
## Ausführen der Anwendung

1. Flask-Anwendung festlegen:
   ```
   export FLASK_APP=app.py  # Unter Windows: `set FLASK_APP=app.py`
   ```

2. Anwendung starten:
   ```
   flask run
   ```

3. Einen Webbrowser öffnen und zu `http://127.0.0.1:5000/` navigieren.

## Nutzung

1. Ein neues Konto registrieren (ACHTUNG: mit einer wahlweise fiktiven email Bsp. ..@gmx.com) oder sich anmelden, wenn bereits ein Konto besteht.
2. Restauranttipps hinzufügen, indem man im Navigationsmenü auf "Add Tip" klickt.
3. Nach Tipps suchen, indem man das Suchformular verwendet, welches Filter nach Küche, Preisklasse und Atmosphäre ermöglicht.
4. Präferenzen/Favoriten festlegen.
5. Detaillierte Informationen zu jedem Restaurant anzeigen, indem man auf dessen Namen in der Tipp-Liste klickt.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert.
