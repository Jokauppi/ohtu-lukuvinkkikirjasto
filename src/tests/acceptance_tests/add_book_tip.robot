*** Settings ***
Resource  resource.robot
Test Setup  Setup Service And Input Add Command

*** Test Cases ***
Add Book Tip
    Input Book Tip  book  writer  1-56619-909-3  2000
    Run And Quit Application
    Output Should Contain  Kirja lisätty

*** Keywords ***
Setup Service And Input Add Command
    Clear Database
    Setup Service
    Input Command  l