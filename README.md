# ohtu-lukuvinkkikirjasto
![GitHub Actions](https://github.com/Jokauppi/ohtu-lukuvinkkikirjasto/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/Jokauppi/ohtu-lukuvinkkikirjasto/branch/main/graph/badge.svg?token=4EYTWGYKB4)](https://codecov.io/gh/Jokauppi/ohtu-lukuvinkkikirjasto)

## Definition of done
Scrumin mukaisesti projektissa toteutetaan backlogista löytyvät user storyt, 
joille on jokaiselle määritelty hyväksymiskriteerit.
Projektin product- ja sprint-backlogit ja siten myös hyväksymiskriteerit löytyvät tästä sheetistä: [backlogit](https://docs.google.com/spreadsheets/d/17mexdx3A8TU8_awobyIz68YoxxH1emHQaHv5W4zPq1w/edit#gid=124771927)

Hyväksymiskriteerit testataan käyttäen Robot-frameworkia.
Koodia testataan kattavasti myös unit testeillä.
Koodityyli noudattaa pylintin avulla määriteltyjä sääntöjä.

Asiakas voi seurata koodin ja testien tilannnetta CI-palvelusta: [codecov](https://app.codecov.io/gh/Jokauppi/ohtu-lukuvinkkikirjasto)

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

Ohjelma toimii toistaiseksi vain paikallisesti.

## Ohjelman käyttöohje

Ohjelma toimii komentoriviltä tekstikättöliittymällä.
Kloonaa koneellesi tämä repositorio ja siirry sen juurihakemistoon.

### Asennus ja käynnistys

Asenna projektin riippuvuudet suorittamalla sen juurihakemistossa komento poetry install.
Sovellus käynnistyy komennolla poetry run python3 src/index.py.
Vaihtoehtoisesti voit siirtyä ensin virtuaaliympäristöön komennolla poetry shell 
ja tämän jälkeen suorittaa komennon python3 src/index.py.

### Käyttöliittymä

Ohjelman käynnistyttyä voit antaa komentoja ohjelmalle. 
Kirjoita "q" poistuaksesi sovelluksesta, 
"a" lisätäksesi kirjavinkin, 
tai "p" tulostaaksesi lisätyt kirjavinkit.

#### Kirjavinkin lisäys

Anna ohjelmalle komennoksi "a" ja paina enteriä.
Ohjelma kysyy järjestyksessä 
kirjan nimen, kirjailijan nimen, ISBN-koodin, sekä julkaisuvuoden.
Syötä pyydetyt tiedot.
Tämän jälkeen näet lisätyn kirjavinkin komennolla "p", 
joka listaa kaikki lisätyt kirjavinkit tietoineen.

## Lisenssi

This project is licensed under the terms of the MIT license.


