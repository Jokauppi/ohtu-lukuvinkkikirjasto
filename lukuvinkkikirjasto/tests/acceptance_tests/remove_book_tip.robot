*** Settings ***
Resource  resource.robot
Test Setup  Setup App And Input Add Book Command

*** Test Cases ***
Remove Existing Book Tip
    Add Book Tip To Service  Name  Author  1234  1994
    Input Command  c
    Input Command  0
    Input Command  d
    Run And Quit Application
    
    Database Should Not Contain Book  Name  Author  1234  1994

Remove Wrong Id Book Tip
    Add Book Tip To Service  Name  Author  1234  1994
    Input Command  c
    Input Command  1
    Input Command  0
    Input Command  d
    Run And Quit Application
    
    Database Should Not Contain Book  Name  Author  1234  1994

*** Keywords ***
Setup App And Input Add Book Command
    Clear Database
    Setup App

Add Book Tip
    [Arguments]  ${name}  ${author}  ${isbn}  ${pub_year}
    Input Book Tip  ${name}  ${author}  ${isbn}  ${pub_year}
    Run And Quit Application
