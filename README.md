# Persoonlijk Project: Auto Website

Dit project is een interactieve auto-verkoopwebsite, ontworpen met HTML, CSS (Tailwind), en ondersteund door een eenvoudige Go-webserver. De website biedt een moderne interface met een zoekfunctionaliteit, filteropties en een responsief ontwerp. 

## Inhoudsopgave

- [Overzicht](#overzicht)
- [Kenmerken](#kenmerken)
- [Installatie](#installatie)
- [Gebruik](#gebruik)
- [Bestandsstructuur](#bestandsstructuur)
- [Aanpassingen](#aanpassingen)
- [Gebruikte Technologieën](#gebruikte-technologieën)
- [Licentie](#licentie)

---

## Overzicht

De website is ontworpen om een gebruiksvriendelijke interface te bieden voor het zoeken, bekijken en filteren van auto's. Met Tailwind CSS voor styling en een Go-webserver voor hosting is het een modern en efficiënt project voor autoverkoop.

De website bevat:
1. **Zoekfunctionaliteit**: Gebruikers kunnen zoeken naar auto's, merken en modellen.
2. **Filteropties**: Gebruikers kunnen auto's filteren op basis van merk, model, bouwjaar en prijs.
3. **Responsief ontwerp**: De website werkt goed op zowel desktop- als mobiele apparaten.

---

## Kenmerken

- **Interactieve zoekbalk**:
  - Zoek naar auto's, merken of modellen via een gebruiksvriendelijke interface.
- **Filtersysteem**:
  - Filter auto's op basis van verschillende parameters zoals merk, model, jaar en prijs.
- **Autoweergave**:
  - Toont afbeeldingen en details van verschillende auto's.
- **Responsief ontwerp**:
  - Geschikt voor zowel desktop- als mobiele apparaten.
- **Ondersteuning door Go-server**:
  - Een eenvoudige Go-server verzorgt de hosting van de website.

---

## Installatie

### Vereisten
- [Go](https://golang.org/doc/install) (Go 1.16 of hoger)
- Een moderne browser (bijvoorbeeld Chrome, Firefox of Edge)

### Stappen

1. **Clone de repository**:
   ```bash
   git clone <repository-url>
   cd <repository-map>

2. Bestanden voorbereiden: Zorg ervoor dat alle bestanden in de juiste mappen staan. De HTML moet zich bevinden in een map genaamd templates/.

3. Start de server: Gebruik het Go-script om de webserver te starten:
   ```bash
   go run main.go

4. Open de website: Ga naar http://localhost:8080/ in je browser.


Hier is een gedetailleerde README voor jouw project:

markdown
Code kopiëren
# Persoonlijk Project: Auto Website

Dit project is een interactieve auto-verkoopwebsite, ontworpen met HTML, CSS (Tailwind), en ondersteund door een eenvoudige Go-webserver. De website biedt een moderne interface met een zoekfunctionaliteit, filteropties en een responsief ontwerp. 

## Inhoudsopgave

- [Overzicht](#overzicht)
- [Kenmerken](#kenmerken)
- [Installatie](#installatie)
- [Gebruik](#gebruik)
- [Bestandsstructuur](#bestandsstructuur)
- [Aanpassingen](#aanpassingen)
- [Gebruikte Technologieën](#gebruikte-technologieën)
- [Licentie](#licentie)

---

## Overzicht

De website is ontworpen om een gebruiksvriendelijke interface te bieden voor het zoeken, bekijken en filteren van auto's. Met Tailwind CSS voor styling en een Go-webserver voor hosting is het een modern en efficiënt project voor autoverkoop.

De website bevat:
1. **Zoekfunctionaliteit**: Gebruikers kunnen zoeken naar auto's, merken en modellen.
2. **Filteropties**: Gebruikers kunnen auto's filteren op basis van merk, model, bouwjaar en prijs.
3. **Responsief ontwerp**: De website werkt goed op zowel desktop- als mobiele apparaten.

---

## Kenmerken

- **Interactieve zoekbalk**:
  - Zoek naar auto's, merken of modellen via een gebruiksvriendelijke interface.
- **Filtersysteem**:
  - Filter auto's op basis van verschillende parameters zoals merk, model, jaar en prijs.
- **Autoweergave**:
  - Toont afbeeldingen en details van verschillende auto's.
- **Responsief ontwerp**:
  - Geschikt voor zowel desktop- als mobiele apparaten.
- **Ondersteuning door Go-server**:
  - Een eenvoudige Go-server verzorgt de hosting van de website.

---

## Installatie

### Vereisten
- [Go](https://golang.org/doc/install) (Go 1.16 of hoger)
- Een moderne browser (bijvoorbeeld Chrome, Firefox of Edge)

### Stappen

1. **Clone de repository**:
   ```bash
   git clone <repository-url>
   cd <repository-map>
   
2. Bestanden voorbereiden: Zorg ervoor dat alle bestanden in de juiste mappen staan. De HTML moet zich bevinden in een map genaamd templates/.

3. Start de server: Gebruik het Go-script om de webserver te starten:

  ```bash
  go run main.go

4. Open de website: Ga naar http://localhost:8080/ in je browser.

Gebruik
Open de website in een browser.
Zoek naar auto's met de zoekbalk of filteropties.
Bekijk de details en prijzen van beschikbare auto's.
Gebruik de navigatie onderaan de pagina om te schakelen tussen "Home", "Cars", "Sell", en "Account".

Bestanddstructuur 

project-root/
├── templates/
│   └── index.html        # HTML-bestand voor de hoofdpagina
├── main.go               # Go-webserver script
└── README.md             # Documentatie

Gebruikte Technologieën
HTML & Tailwind CSS:
Voor een eenvoudige maar krachtige front-end styling.
Go:
Voor het hosten van de website via een eenvoudige HTTP-server.

Toekomstige Verbeteringen
Database-integratie:
Voeg een database toe (zoals PostgreSQL of MongoDB) om auto's dynamisch op te halen.
Backend-filters:
Implementeer filters aan de serverkant voor betere zoekfunctionaliteit.
Authenticatie:
Voeg gebruikersregistratie en -login toe.

