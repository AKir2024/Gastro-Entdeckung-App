---
title: App Structure
parent: Technical Docs
nav_order: 1
---

{: .label }

# App-Structure

{: .attention }


## 1.	instance
### restaurant_tips.db: 
Dies ist die SQLite-Datenbank-Datei, in der alle Daten für die Anwendung gespeichert werden. Unter anderem Informationen zu Benutzern, Präferenzen und Tipps zu Restaurants. 

## 2.	static
### logo.png: 
Eine Bilddatei, das Logo der Anwendung, die in den HTML-Seiten eingebettet wird.

### style.css: 
Eine CSS-Datei, die das Design (Styling) der Anwendung steuert. Sie enthält Regeln, wie die verschiedenen HTML-Elemente (Farben, Layouts, Schriften) auf den Webseiten angezeigt werden.

## 3.	templates
### add_tip.html: 
Ein HTML-Template für die Seite, auf der Benutzer einen neuen Restaurant-Tipp hinzufügen können.

### base.html: 
Eine wiederverwendbare Vorlage, die das Grundgerüst der Website enthält (wie Header, Footer etc.). Andere Templates erben von dieser Vorlage.

### index.html: 
Das Haupt-Template für die Startseite der Anwendung.

### login.html: 
Ein Template für die Login-Seite, auf der Benutzer ihre Anmeldedaten eingeben.

### preferences.html: 
Eine Seite, auf der Benutzer ihre Präferenzen (wie Restaurant-Vorlieben) festlegen oder ändern können.

### register.html:
Ein Template für die Registrierung neuer Benutzer.

### restaurant.html:
Diese Seite zeigt wahrscheinlich Details zu einem bestimmten Restaurant, das in der App gefunden wurde.

### search_tip.html: 
Eine Seite, die eine Suchfunktion bietet, um nach Restaurant-Tipps zu suchen.

## 4.	app.py
Diese Datei ist das Herzstück der Flask-Anwendung. Sie enthält den Code, der die App startet, die Routen definiert (welche Seiten aufgerufen werden), und die Backend-Logik der App steuert.

## 5.	models.py
In dieser Datei befinden sich die Definitionen der Datenbankmodelle. Im Bild, das du zuvor geteilt hast, sind die User, Tip, und Preference-Modelle definiert, die die Datenstruktur der Anwendung darstellen.


