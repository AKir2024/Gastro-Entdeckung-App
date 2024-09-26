---
title: Design Decisions
nav_order: 3
---

{: .label }
Alexey Kirchner

{: .no_toc }
# Design decisions

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: [Gastro-Entdeckung: Design Decisions]

--------------------------------------------------------------------------------------------------------------------
## Problem statement
Die Benutzer von der Gastro-Entdeckungs-WebApp sollen in der Lage sein, Restaurants in ihrer Nähe zu finden und verschiedene Filteroptionen wie Küche, Preis oder Essgewohnheit zu verwenden, um die Auswahl einzugrenzen. Es wird eine benutzerfreundliche Webanwendung benötigt, von jedem intuitiv bedient werden kann. Die Anwendung soll zudem eine interaktive Karte zur Visualisierung der Restaurants enthalten. Um dies zu erreichen, müssen mehrere Seiten (Startseite, Login, Registrierung, Karte, Suchfilter, und Listenausgabe) entworfen und ihre Funktionalität klar definiert werden.


### Problem Statement 1: Auswahl einer geeigneten Anmeldemethode:
Das Ziel ist es, eine benutzerfreundliche Methode zur Authentifizierung von Nutzern zu implementieren, die es ermöglicht, sich zu registrieren und einzuloggen, um Zugang zur App und ihren Funktionen wie der Restaurant-Suche, der Kartenansicht und den Filterfunktionen zu erhalten.

#### Benutzerfreundlichkeit: 
Die Methode sollte einfach und intuitiv sein, um eine breite Nutzerschaft zu erreichen und den Registrierungs- und Login-Prozess so reibungslos wie möglich zu gestalten.

#### Skalierbarkeit: 
Die gewählte Lösung sollte in der Lage sein, ohne probleme mit einer wachsenden Anzahl von Registrierungen zurecht zu kommen.

### Problem Statement 2: Datenbank
Das Ziel ist es, eine Datenbankstruktur für die Anwendung zu entwerfen, die eine effiziente Verwaltung von Nutzerdaten, Restaurants und Bewertungen ermöglicht. Die Datenbankstruktur sollte die folgenden Hauptentitäten und ihre Beziehungen abbilden:

#### Benutzerkonten: 
Speichern von Benutzerinformationen wie Name, Passwort, etc.

#### Restaurants:
Verwaltung von Restaurantdaten, einschließlich Name, Adresse, Küche und Bewertungen.

#### Favoriten: 
Speicherung von favorisierten Restaurants.

Die Datenbank muss gut genug sein, um zukünftige Erweiterungen zu unterstützen, z.B. das Hinzufügen von neuen Nutzern oder Favoritenlisten. Außerdem sollte sie eine effiziente Abfrage und Änderung der Daten ermöglichen, die auch bei wachsenden Datenmengen und einer steigenden Nutzeranzahl ohne Probleme funktioniert.

### Problem Statement 3: Frontend
Das Ziel ist es, geeignete Methoden für die Entwicklung der Benutzeroberfläche der Webanwendung auszuwählen. Die Herausforderung besteht darin, eine einfache und benutzerfreundliche Oberfläche zu erstellen. Es geht darum, sicherzustellen, dass die Website leicht zu bedienen ist und optisch ansprechend wirkt. Dies umfasst die Auswahl von Tools und Technologien, die die Entwicklung erleichtern und eine einfache Aktualisierung und Wartung der Website ermöglichen. Letztendlich soll sichergestellt werden, dass die Nutzer eine positive Erfahrung beim Besuch der Website haben und die Frontend-Entwicklung reibungslos verläuft.

--------------------------------------------------------------------------------------------------------------------
## Decision

### Design Decision 1: Auswahl der Anmeldemethode
#### Entscheidung:
Es wurde entschieden, eine benutzerfreundliche Anmeldemethode mit Hilfe von Flask und SQLite zu implementieren. Die Benutzerdaten werden sicher in der SQLite-Datenbank gespeichert. 

#### Begründung:
Flask ermöglicht eine einfache Integration der Anmeldemodule und ist leicht skalierbar, um eine wachsende Anzahl von Registrierungen zu unterstützen. SQLite wurde aufgrund seiner Einfachheit und der geringen administrativen Anforderungen gewählt. Für eine wachsende Nutzerbasis ist die Implementierung flexibel, zudem bietet Flask Erweiterungsmöglichkeiten, falls zukünftige Anforderungen dies verlangen.

### Design Decision 2: Datenbank
#### Entscheidung:
Die Datenbankstruktur wird in SQLite entworfen und umfasst die folgenden Tabellen: Benutzer, Restaurants, Bewertungen und Favoriten.

#### Begründung:
SQLite wurde aufgrund einer Empfehlung im Kurs gewählt, da es keine separate Server-Konfiguration erfordert. Die Struktur der Tabellen unterstützt eine Abfrage von Restaurants basierend auf verschiedenen Filterkriterien (wie Küche, Preis und Essgewohnheiten) und ermöglicht es Benutzern, ihre favorisierten Restaurants einfach zu speichern. 

### Design Decision 3: Frontend

#### Entscheidung:
Es wurde entschieden, das Frontend mit Bootstrap, HTML, CSS und Jinja zu entwickeln, um eine benutzerfreundliche Oberfläche zu schaffen. Jinja wird verwendet, um dynamische HTML-Inhalte in Flask zu rendern, wodurch die Verbindung zwischen Backend und Frontend vereinfacht wird.

#### Begründung:
Bootstrap wurde gewählt, um eine schnelle und einfache Entwicklung einer ansprechenden und funktionalen Benutzeroberfläche zu gewährleisten. Es bietet vorgefertigte Designkomponenten, die sicherstellen, dass die Anwendung einwandfrei funktioniert. 

--------------------------------------------------------------------------------------------------------------------
## Regarded options

### Design Decision 1: Auswahl der Anmeldemethode
#### Entscheidung:
Es wurde entschieden, eine benutzerfreundliche Authentifizierungsmethode mit Hilfe von Flask und SQLite zu implementieren. Die Benutzerdaten werden in der SQLite-Datenbank gespeichert.

| **Pros**                                                                                             | **Cons**                                                                                                                 |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| +Einfache Implementierung: Flask bietet einfache Methoden zur Anmeldung und Verwaltung von User-Sessions, was die Entwicklung vereinfacht. | -Begrenzte Skalierbarkeit von SQLite: Für eine sehr große Anwendung ist SQLite möglicherweise nicht ausreichend, da es keine gleichzeitigen Schreibzugriffe in großem Umfang unterstützt. |
| +Geringe Komplexität: SQLite erfordert keine komplexe Server-Konfiguration und kann lokal oder auf kleinen Servern betrieben werden. |                                                                                                                          |


### Design Decision 2: Datenbankstruktur

#### Entscheidung:
Die Datenbankstruktur wird in SQLite entworfen und umfasst die Tabellen: Benutzer, Restaurants, Bewertungen und Favoriten.

| **Pros**                                                                                                         | **Cons**                                                                                                                |
|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| + Einfache Implementierung: SQLite ist leicht zu integrieren und erfordert keine komplexe Server-Infrastruktur.   | - Keine fortgeschrittenen Features: SQLite bietet nicht die erweiterten Funktionen von Datenbanken wie z.B. erweiterte Abfragen oder integrierte Sicherheitsmechanismen. |
| + Schnelle Abfragen: SQLite eignet sich gut für kleinere bis mittelgroße Datenmengen, was für die anfängliche Größe des Projekts ideal ist. |                                                                                                                         |
| + Zukunftssicherheit: Die Datenbankstruktur kann mit wachsenden Anforderungen erweitert werden, z.B. durch das Hinzufügen weiterer Filteroptionen oder Bewertungen. |                                                                                                                         |
| + Leicht erweiterbar: Die Trennung der Daten in verschiedene Tabellen erleichtert das Hinzufügen neuer Funktionen wie zusätzliche Filter oder Benutzerfavoriten. |                                                                                                                         |

### Design Decision 3: Frontend-Technologie

#### Entscheidung:
Das Frontend wird mit Bootstrap, HTML, CSS und Jinja entwickelt. Bootstrap wird für das benutzerfreundliche Design genutzt, Jinja für die dynamische Generierung von HTML-Inhalten in Flask.

| **Pros**                                                                                                          | **Cons**                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| + Schnelle Entwicklung: Bootstrap bietet vorgefertigte Komponenten, die die Frontend-Entwicklung erheblich beschleunigen. | - Ähnliche Design Merkmale: Bootstrap kann, bei geringfügiger Anpassung, dazu führen, dass das Design der Website dem vieler anderer Bootstrap-basierter Seiten ähnelt. |
| + Leichte Integration mit Flask: Jinja arbeitet nahtlos mit Flask zusammen und ermöglicht die dynamische Generierung von HTML-Inhalten, was die Verbindung von Frontend und Backend vereinfacht. |                                                                                                                          |
| + Geringer Wartungsaufwand: Bootstrap und Jinja sind weit verbreitet und gut dokumentiert, was zukünftige Änderungen erleichtert. |                                                                                                                          |

## Zusammenfassung:
Für das "Gastro-Entdeckung"-Projekt werden folgende Design-Descisions getroffen, um eine benutzerfreundliche Anwendung zu schaffen. Flask wurde als Backend-Framework in Kombination mit SQLite gewählt, da diese eine einfache Implementierung und eine übersichtiliche Speicherung der Benutzerdaten bieten. SQLite ist dabei optimal für kleinere bis mittlere Datenmengen.

Im Frontend wird Bootstrap eingesetzt, um die Entwicklung durch vorgefertigte und responsive Komponenten zu beschleunigen. Jinja sorgt für eine Integration von dynamischen Inhalten in Flask, was die Verbindung von Backend und Frontend gewährt. Diese Kombination bietet eine schnelle- und überschauliche Entwicklung der Anwendung. Insgesamt ermöglichen diese Entscheidungen die Entwicklung einer benutzerfreundlichen und Funktionalen Web-App.

---
