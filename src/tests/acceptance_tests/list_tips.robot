*** Settings ***
Resource  resource.robot
Test Setup  Setup Application

*** Test Cases ***
List All Book Tips
    Add Book Tip To Service  book1  writer1  11111-11111-11111  2000
    Add Book Tip To Service  book2  writer2  22222-22222-22222  2001
    Input Command  p
    Run And Quit Application

    Output Should Contain Book  book1  writer1  11111-11111-11111  2000
    Output Should Contain Book  book2  writer2  22222-22222-22222  2001

*** Keywords ***
Setup Application
    Clear Database
    Setup App
