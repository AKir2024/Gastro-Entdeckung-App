---
title: App Behavior
parent: Technical Docs
nav_order: 2
---

{: .label }


# App Behavior

## 1.	Benutzerregistrierung und Authentifizierung:
-	Neue Benutzer können sich über das Registrierungsformular anmelden, indem sie eine E-Mail-Adresse, ein Passwort sowie Wohnortinformationen angeben. Die Passwörter werden verschlüsselt gespeichert (Bcrypt).
-	Bereits registrierte Benutzer können sich über ein Login-Formular anmelden.
-	Authentifizierte Benutzer haben Zugang zu geschützten Bereichen der App (z. B. Einstellungen der Benutzerpräferenzen).
-	Ein Logout-Mechanismus ermöglicht es den Benutzern, sich sicher aus der App abzumelden.

## 2.	Restaurant-Tipps hinzufügen:
-	Angemeldete Benutzer können neue Restaurant-Tipps hinzufügen. Diese Informationen beinhalten Angaben zu Restaurants und eventuell persönliche Bewertungen oder Empfehlungen (Tipps).
-	Es gibt eine Funktion, um eine Restaurantbewertung oder einen Tipp in die Datenbank hinzuzufügen.

## 3.	Homepage mit Tipps anzeigen:
- Die Startseite der App zeigt eine Übersicht der vorhandenen Restaurant-Tipps, die von allen Benutzern eingereicht wurden.
-	Es gibt eine Suchfunktion, die den Benutzern ermöglicht, nach Restaurants basierend auf verschiedenen Filtern (Küche, Preisklasse, Ort usw.) zu suchen. Die Ergebnisse der Suche werden dynamisch angezeigt.

## 4.	Benutzerpräferenzen speichern und anzeigen:
-	Benutzer können ihre Essenspräferenzen (Küche, Preisklasse, Atmosphäre, Land, Stadt) in einem speziellen Bereich der App speichern.
-	Wenn die Präferenzen bereits gespeichert wurden, können sie auch nachträglich bearbeitet und aktualisiert werden.
-	Die gespeicherten Vorlieben beeinflussen wahrscheinlich die Suchergebnisse oder Empfehlungen für den Benutzer.

## 5.	Details zu Restaurant-Tipps anzeigen:
-	Benutzer können die Details eines spezifischen Restaurant-Tipps anzeigen lassen, indem sie auf den entsprechenden Link klicken. Diese Seite zeigt wahrscheinlich eine detaillierte Ansicht des Restaurants und die zugehörigen Tipps an.

## 6.	Interaktion mit Yelp-API:
-	Die App integriert die Yelp-API, um zusätzliche Informationen über Restaurants zu erhalten. Das könnte bedeuten, dass die App Echtzeit-Daten zu Restaurants (wie Bewertungen, Preise, Fotos, usw.) abruft und dem Benutzer präsentiert.

## 7.	Sicherheitsmechanismen:
-	Die App verwendet einen geheimen Schlüssel, um sensible Daten zu schützen, und setzt verschlüsselte Passwörter ein, um die Benutzerkonten zu sichern.
-	Zugriff auf bestimmte Bereiche der App, wie z. B. die Verwaltung von Präferenzen, ist nur für angemeldete Benutzer möglich (Login erforderlich).


# Additional Documentation

## 1.	Verwendete Technologien:
-	Flask (Python-Framework): Das Backend der Anwendung ist mit Flask implementiert. Flask stellt eine einfache, leichtgewichtige Struktur zur Verfügung, um Webanwendungen zu erstellen und verschiedene Routen (z.B. für Registrierung, Login, Suche, usw.) zu definieren.
-	WTForms: Diese Bibliothek wird verwendet, um Formulare zu erstellen und Validierungen durchzuführen. Es gibt Formulare für die Benutzerregistrierung, das Login und die Suche nach Restaurants.
-	Flask-Bcrypt: Diese Erweiterung wird genutzt, um Passwörter der Benutzer sicher zu verschlüsseln, bevor sie in der Datenbank gespeichert werden.
-	Flask-Login: Diese Erweiterung wird genutzt, um die Benutzeranmeldungen zu verwalten und den Zugriff auf geschützte Routen zu sichern.
-	Flask-WTF: Flask-WTF kombiniert Flask und WTForms und fügt nützliche Funktionen wie CSRF-Schutz (Cross-Site Request Forgery) hinzu.
-	SQLAlchemy: Die App verwendet SQLAlchemy als ORM (Object-Relational Mapper), um Daten in einer SQLite-Datenbank zu speichern und abzufragen. Es gibt mehrere Datenbankmodelle, darunter Benutzer, Tipps (Restaurantbewertungen), und Präferenzen der Benutzer.

## 2.	API-Integration:
-	Yelp API: Die App integriert die Yelp API, um Restaurantinformationen zu suchen und anzuzeigen. Benutzer können nach verschiedenen Kriterien wie Küche, Preisklasse und Ort filtern. Die Yelp API ermöglicht es der Anwendung, auf Informationen wie Restaurantnamen, Bewertungen, Standorte und weitere Details in Echtzeit zuzugreifen.
https://docs.developer.yelp.com/docs/fusion-intro

## 3.	Templating (Jinja2):
-	Der Code verwendet Flask's Templating-Engine Jinja2. Dies erlaubt es, HTML-Templates dynamisch mit Daten vom Server zu rendern. Die Benutzerformulare (Login, Registrierung, Präferenzen, Suche) und Restaurant-Tipps werden in diesen Templates dargestellt.

## 4.	Sicherheit:
-	CSRF-Schutz: WTForms und Flask-WTF integrieren einen Cross-Site Request Forgery Schutz, um sicherzustellen, dass Formular-Post-Anfragen nur von autorisierten Quellen kommen.
-	Login-Schutz: Routen wie die Präferenzverwaltung sind durch Flask-Login gesichert, sodass nur authentifizierte Benutzer Zugriff haben.

## 5. Javaskript Integration: 

- Formularvalidierung: Bevor die Benutzerdaten an den Server gesendet werden, überprüft JavaScript, ob die erforderlichen Felder korrekt ausgefüllt sind. Dies reduziert serverseitige Fehler und sorgt für eine schnellere Rückmeldung an den Benutzer.

- Dynamische Inhalte: JavaScript ermöglicht die dynamische Aktualisierung von Inhalten auf der Webseite, z. B. das Ein- und Ausblenden von Filtern oder die Anzeige von Suchergebnissen, ohne die Seite komplett neu zu laden. Dies bietet den Benutzern eine reibungslose Interaktion.

- Die Integration von JavaScript in diese Anwendung trägt wesentlich dazu bei, eine moderne, responsive und benutzerfreundliche Webanwendung zu bieten.
