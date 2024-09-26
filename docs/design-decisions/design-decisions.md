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


### Decision

[Describe **which** design decision was taken for **what reason** and by **whom**.]

### Regarded options

[Describe any possible design decision that will solve the problem. Assess these options, e.g., via a simple pro/con list.]

---

## [Example, delete this section] 01: How to access the database - SQL or SQLAlchemy 

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 30-Jun-2024

### Problem statement

Should we perform database CRUD (create, read, update, delete) operations by writing plain SQL or by using SQLAlchemy as object-relational mapper?

Our web application is written in Python with Flask and connects to an SQLite database. To complete the current project, this setup is sufficient.

We intend to scale up the application later on, since we see substantial business value in it.



Therefore, we will likely:
Therefore, we will likely:
Therefore, we will likely:

+ Change the database schema multiple times along the way, and
+ Switch to a more capable database system at some point.

### Decision

We stick with plain SQL.

Our team still has to come to grips with various technologies new to us, like Python and CSS. Adding another element to our stack will slow us down at the moment.

Also, it is likely we will completely re-write the app after MVP validation. This will create the opportunity to revise tech choices in roughly 4-6 months from now.
*Decision was taken by:* github.com/joe, github.com/jane, github.com/maxi

### Regarded options

We regarded two alternative options:

+ Plain SQL
+ SQLAlchemy

| Criterion | Plain SQL | SQLAlchemy |
| --- | --- | --- |
| **Know-how** | ✔️ We know how to write SQL | ❌ We must learn ORM concept & SQLAlchemy |
| **Change DB schema** | ❌ SQL scattered across code | ❔ Good: classes, bad: need Alembic on top |
| **Switch DB engine** | ❌ Different SQL dialect | ✔️ Abstracts away DB engine |

---
