*** Settings ***
Resource  resource.robot
Test Setup  Setup App And Input Add Command

*** Test Cases ***
Add Book Tip With Valid Data
    Add Book Tip  book  writer  1-56619-909-3  2000
    Output Should Contain  Kirja lisätty
    Database Should Contain Book  book  writer  1-56619-909-3  2000

Add Book Tip With Invalid Name
    Add Book Tip  ${EMPTY}  writer  1-56619-909-3  2000
    Output Should Contain  Nimen pituus pitää olla 1-100 merkkiä
    Output Should Contain  Kirjan lisäys ei onnistunut

Add Book Tip With Invalid Author
    Add Book Tip  book  ${EMPTY}  1-56619-909-3  2000
    Output Should Contain  Nimen pituus pitää olla 1-100 merkkiä
    Output Should Contain  Kirjan lisäys ei onnistunut

Add Book Tip With Invalid ISBN
    Add Book Tip  book  writer  1-56619-test-3  2000
    Output Should Contain  ISBN pitää sisältää vain merkkejä 0-9 ja -
    Output Should Contain  Kirjan lisäys ei onnistunut

Add Book Tip With Too Long ISBN
    Add Book Tip  book  writer  12345-12345-12345-12345-12345  2000
    Output Should Contain  ISBN pituus pitää olla 1-20 merkkiä
    Output Should Contain  Kirjan lisäys ei onnistunut

Add Book Tip With Invalid Year
    Add Book Tip  book  writer  12345-12345-12345  test
    Output Should Contain  Vuosi pitää sisältää vain merkkejä 0-9
    Output Should Contain  Kirjan lisäys ei onnistunut

Add Book Tip With Too Large Year
    Add Book Tip  book  writer  12345-12345-12345  4000
    Output Should Contain  Vuosi pitää olla välillä 0-3000
    Output Should Contain  Kirjan lisäys ei onnistunut

*** Keywords ***
Setup App And Input Add Command
    Clear Database
    Setup App
    Input Command  a
    Input Command  k

Add Book Tip
    [Arguments]  ${name}  ${author}  ${isbn}  ${pub_year}
    Input Book Tip  ${name}  ${author}  ${isbn}  ${pub_year}
    Run And Quit Application
