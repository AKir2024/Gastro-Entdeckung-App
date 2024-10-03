---
title: Data Model
parent: Technical Docs
nav_order: 3
---

{: .label }


# Data Model

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

<img width="643" alt="image" src="https://github.com/user-attachments/assets/61f1f1b7-8bb7-47e8-ac3a-563f33a07b33">


## Benutzer-Modell:
  - Benutzer (User)
  
    -	id: Integer (Primärschlüssel)
    -	email: String (max. 150 Zeichen darf nicht Null sein)
    -	password: String (max. 150 Zeichen darf nicht Null sein)
    -	country: String (max. 100 Zeichen darf nicht Null sein)
    -	city: String (max. 100 Zeichen darf nicht Null sein)
    -	preferences: Beziehung mit dem Modell Preference (Eins-zu-Viele)

## Tipp-Modell:
  -	Tipp (Tip)
    -	id: Integer (Primärschlüssel)
    -	name: String (max. 100 Zeichen darf nicht Null sein)
    - cuisine: String (max. 50 Zeichen darf nicht Null sein)
    -	price_range: String (max. 20 Zeichen darf nicht Null sein)
    -	atmosphere: String (max. 50 Zeichen darf nicht Null sein)
    -	tip_content: String (max. 500 Zeichen darf nicht Null sein)
    -	country: String (max. 100 Zeichen darf nicht Null sein)
    -	city: String (max. 100 Zeichen darf nicht Null sein)
    -	user_id: Fremdschlüssel (User.id, Nicht Null) — Verknüpfung mit User (Viele-zu-Eins Beziehung)

## Präferenz-Modell:
  -	Präferenz (Preference)
    -	id: Integer (Primärschlüssel)
    -	cuisine: String (max. 50 Zeichen darf nicht Null sein)
    -	price_range: String (max. 20 Zeichen darf nicht Null sein)
    -	atmosphere: String (max. 50 Zeichen darf nicht Null sein)
    -	country: String (max. 100 Zeichen darf nicht Null sein)
    -	city: String (max. 100 Zeichen darf nicht Null sein)
    -	user_id: Fremdschlüssel (User.id, Nicht Null) — Verknüpfung mit User (Viele-zu-Eins Beziehung)

## Beziehungen:
-	Benutzer zu Präferenz: Eins-zu-Viele (User kann viele Preferences haben)
-	Benutzer zu Tipp: Eins-zu-Viele (User kann viele Tips abgeben)


