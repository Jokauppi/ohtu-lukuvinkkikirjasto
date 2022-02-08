# ohtu-lukuvinkkikirjasto
[![GitHub Actions](https://github.com/Jokauppi/ohtu-lukuvinkkikirjasto/workflows/CI/badge.svg)](https://github.com/Jokauppi/ohtu-lukuvinkkikirjasto/actions)
[![codecov](https://codecov.io/gh/Jokauppi/ohtu-lukuvinkkikirjasto/branch/main/graph/badge.svg?token=4EYTWGYKB4)](https://codecov.io/gh/Jokauppi/ohtu-lukuvinkkikirjasto)

## Loppuraportti
Projektin [loppuraportti](https://docs.google.com/document/d/16KTcSnFrjN0c-OsDVLTBKsz4J8ry3wZw927VJghYaa0/edit?usp=sharing) on luettavissa linkin takaa.

## Definition of done
Scrumin mukaisesti projektissa toteutetaan backlogista löytyvät user storyt, 
joille on jokaiselle määritelty hyväksymiskriteerit.
Projektin product- ja sprint-backlogit ja siten myös hyväksymiskriteerit löytyvät tästä sheetistä: [backlogit](https://docs.google.com/spreadsheets/d/17mexdx3A8TU8_awobyIz68YoxxH1emHQaHv5W4zPq1w/edit#gid=124771927)

Hyväksymiskriteerit testataan käyttäen Robot-frameworkia.
Koodia testataan kattavasti myös unit testeillä.
Koodityyli noudattaa pylintin avulla määriteltyjä sääntöjä.

Asiakas voi seurata koodin ja testien tilannetta CI-palvelusta: [codecov](https://app.codecov.io/gh/Jokauppi/ohtu-lukuvinkkikirjasto)

Koodin arkkitehtuuri on suunniteltua ja perusteltua,
pyrkimyksenä on mahdollisimman hyvä ylläpidettävyys pitämällä koodi selkeänä.

### Tarkistuslista User Storylle
* Tuotettu koodia suunnitelluille toiminnallisuuksille
* User storyn vaatimuksiin vastattu
* Projekti käynnistyy ilman virheitä
* Unit testit kirjoitettu ja läpäisty
* Toiminnallisuus on testattu hyväksymistesteillä
* Refraktorointi on valmis
* Product ownerin mielestä toiminnallisuus on valmis

### Tarkistuslista Sprintille
* Definition of done sprintin user storyille täytetty
* Kaikki unit testit läpäisty
* Linttaus läpäisty
* Backlog on päivitetty
* Kaikki bugit on korjattu
* Sprintin toteutettu toiminallisuus käyty läpi Product Ownerin kanssa
* Sprinttiin liittyvät "to do" asiat valmiita

### Tarkistuslista viimeiselle Releaselle
* Koodi on valmista
* Kaikki testit läpäisevät
* Kaikki hyväksymiskriteerit täyttyvät
* Ryhmä on hyväksynyt releasen
* Ei keskeneräistä työtä releasen mukana
* Kaikki DoD asetetut vaatimukset täyttyvät

## Ohjelman viimeisin versio

Ohjelma toimii paikallisesti,
tähän mennessä valmiit ominaisuudet on listattu projektin backlogeissa.

## Ohjelman käyttöohje

Ohjelma toimii komentoriviltä tekstikättöliittymällä.
Kloonaa koneellesi tämä repositorio ja siirry sen juurihakemistoon.

### Asennus ja käynnistys

Asenna projektin riippuvuudet suorittamalla sen juurihakemistossa komento
```
poetry install
```
Sovellus käynnistyy komennolla
```
poetry run python3 lukuvinkkikirjasto/index.py
```
Vaihtoehtoisesti voit siirtyä ensin virtuaaliympäristöön komennolla poetry shell 
ja tämän jälkeen suorittaa komennon python3 lukuvinkkikirjasto/index.py.

### Käyttöliittymä

Ohjelman käynnistyttyä voit antaa komentoja ohjelmalle. 
Ohjeet komentojen käytöstä tulostuvat kun käynnistät ohjelman.
Komennot:
* "a" Lisää vinkki, 
* "p" Tarkastele vinkkejä, 
* "f" Muokkaa suodattimia,
* "c" Muokkaa vinkkiä,
* "q" Poistu sovelluksesta.

Lisää vinkki komennon avulla voit lisätä tietokantaan blogi, video ja kirja tyyppisiä vinkkejä.
Tarkastele vinkkejä tulostaa oletuksena kaikki tietokantaan lisätyt vinkit.
Mikäli haluat rajata mitä tulostetaan, se onnistuu muokkaamalla suodattimia.
Yksittäisten vinkkien muokkaaminen, mm kommentointi ja poistaminen tapahtuu komennon muokkaa vinkkiä avulla.
Lisäksi voit lisätä vinkeille tageja tai merkata ne luetuiksi.


## Lisenssi

This project is licensed under the terms of the MIT license.




