*** Settings ***
Resource  resource.robot
Test Setup  Setup Application

*** Test Cases ***
Comment Book Tip
    Add Book Tip To Service  book1  writer1  11111-11111-11111  2000
    Add Book Tip To Service  book2  writer2  22222-22222-22222  2001
    Input Command  c
    Input Command  1
    Input Command  c
    Input Command  kommentti
    Input Command  p
    Run And Quit Application

    Output Should Contain Book  book2  writer2  22222-22222-22222  2001  kommentti



*** Keywords ***
Setup Application
    Clear Database
    Setup App
