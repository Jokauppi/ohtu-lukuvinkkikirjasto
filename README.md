# ohtu-lukuvinkkikirjasto
[![GitHub Actions](https://github.com/Jokauppi/ohtu-lukuvinkkikirjasto/workflows/CI/badge.svg)](https://github.com/Jokauppi/ohtu-lukuvinkkikirjasto/actions)
[![codecov](https://codecov.io/gh/Jokauppi/ohtu-lukuvinkkikirjasto/branch/main/graph/badge.svg?token=4EYTWGYKB4)](https://codecov.io/gh/Jokauppi/ohtu-lukuvinkkikirjasto)

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

Ohjelma toimii toistaiseksi vain paikallisesti,
tähän mennessä työstetyt ominaisuudet on listattu projektin backlogeissa sprintin 1 alle.
* Käyttäjä voi lisätä kirjavinkin
* Käyttäjä voi tulostaa kaikki vinkit

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
poetry run python3 src/index.py
```
Vaihtoehtoisesti voit siirtyä ensin virtuaaliympäristöön komennolla poetry shell 
ja tämän jälkeen suorittaa komennon python3 src/index.py.

### Käyttöliittymä

Ohjelman käynnistyttyä voit antaa komentoja ohjelmalle. 
Ohjeet komentojen käytöstä tulostuvat kun käynnistät ohjelman.
Komennot:
* "a" lisää vinkki, 
* "p" tulosta vinkkejä, 
* "r" merkitse vinkki luetuksi,
* "s" etsi vinkkejä,
* "q" poistu sovelluksesta.

#### Vinkin lisäys

Anna ohjelmalle komennoksi "a" ja paina enteriä.
Valitse seuraavaksi valikosta haluamasi vinkin tyyppi:
* "k" kirjavinkki,
* "b" blogivinkki,
* "v" videolinkki,
* "q" palaa päävalikkoon.

Ohjelma kysyy vinkin tyypistä riippuen erilaisia tietoja.
Syötä pyydetyt tiedot.
Vinkki on nyt lisätty tietokantaan.

#### Vinkkien tulostaminen

Anna ohjelmalle komennoksi "p" ja paina enteriä.
Valitse seuraavaksi valikosta minkä tyyppisiä vinkkejä haluat tulostaa:
* "k" kirjavinkit,
* "b" blogivinkit,
* "v" videovinkit,
* "r" luetut vinkit,
* "u" lukemattomat vinkit,
* "q" palaa päävalikkoon.

Ohjelma tulostaa vinkit ja niihin liittyvät tiedot.

#### Vinkin merkkaaminen luetuksi

Anna ohjelmalle komennoksi "r" ja paina enteriä.
Ohjelma listaa vinkit ja niiden tiedot mukaan lukien vinkkien id-numerot.

Syötä ohjelmalle luetuksi merkittävän vinkin id-numero.

#### Vinkkien etsiminen

Anna ohjelmalle komennoksi "s" ja paina enteriä.
Valitse seuraavaksi kriteeri, jonka perusteella haluat etsiä vinkkejä.
Ohjelma kysyy tarkempia tietoja valitun vinkkityypin perusteella.

Syötä pyydetyt tiedot.
Ohjelma listaa kaikki hakukriteerejä vastaavat tiedot.

## Lisenssi

This project is licensed under the terms of the MIT license.


