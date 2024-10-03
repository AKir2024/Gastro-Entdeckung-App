---
title: Reference
parent: Technical Docs
nav_order: 3
---

{: .label }
[Jane Dane]

{: .no_toc }
# Reference documentation

{: .attention }

 1.	register(): /register – POST 
    a.	Registriert einen neuen Benutzer
   	
    <img width="289" alt="image" src="https://github.com/user-attachments/assets/9371218f-2668-4703-a5d2-5baaa54ab655">

2.	login(): /login – POST
    a.	Loggt einen Benutzer ein.
  	
    ![image](https://github.com/user-attachments/assets/19d18415-1e1d-4be0-994a-55d604695c7e)

3.	logout(): /logout – GET
    a.	Loggt einen Benutzer aus.
  	
4.	add_tip(): /add_tip – POST
    a.	Fügt einen Restaurant-Tipp hinzu
  	
    ![image](https://github.com/user-attachments/assets/8503db03-8eb0-42d7-b68c-877aeed887b8)


6.	index(): / (Startseite) – GET
    a.	Zeigt die Startseite mit Restaurant-Tipps an.
7.	search_tip(): /search_tip - GET, POST
    a.	Ermöglicht Benutzern, nach Restaurants basierend auf Filtern wie Küche, Preisklasse und Standort     zu suchen.
  	
   <img width="814" alt="image" src="https://github.com/user-attachments/assets/6fb86d88-e756-445f-a972-44af445b743b">

  	
7.	preferences(): /preferences - GET, POST
    a.	Ermöglicht Benutzern, ihre Vorlieben anzuzeigen und zu aktualisieren.
  	
  	![image](https://github.com/user-attachments/assets/5bd243ea-7abb-432e-8dfc-3081f61f3cb3)

8.	restaurant(id): /restaurant/<int:id> - GET
    a.	Zeigt die Details eines spezifischen Restaurant-Tipps anhand seiner ID an.
  	
  	![image](https://github.com/user-attachments/assets/8d30421f-1ebf-488a-9cda-de3d84f72400)


