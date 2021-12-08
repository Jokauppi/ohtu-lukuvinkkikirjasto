*** Settings ***
Resource  resource.robot
Test Setup  Setup App And Input Add Book Command

*** Test Cases ***
Remove Existing Book Tip
    Add Book Tip  Name  Author  1234  1994
    Delete Book Tip  Name  Author  1234  1994
    
    Database Should Not Contain Book  Name  Author  1234  1994

Remove Nonexisting Book Tip
    Delete Book Tip  Name  Author  1234  1994
    
    Database Should Not Contain Book  Name  Author  1234  1994

*** Keywords ***
Setup App And Input Add Book Command
    Clear Database
    Setup App
    Input Command  a
    Input Command  k

Add Book Tip
    [Arguments]  ${name}  ${author}  ${isbn}  ${pub_year}
    Input Book Tip  ${name}  ${author}  ${isbn}  ${pub_year}
    Run And Quit Application
