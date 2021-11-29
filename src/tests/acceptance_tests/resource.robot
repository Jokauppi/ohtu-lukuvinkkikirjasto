*** Settings ***
Library  ../../AppLibrary.py

*** Keywords ***
Input Command
    [Arguments]  ${command}
    Input  ${command}

Input Book Tip
    [Arguments]  ${name}  ${author}  ${isbn}  ${pub_year}
    Input  ${name}
    Input  ${author}
    Input  ${isbn}
    Input  ${pub_year}

Output Should Contain Book
    [Arguments]  ${name}  ${author}  ${isbn}  ${pub_year}
    Output Should Contain  Book name: ${name}\nAuthor: ${author}\nISBN: ${isbn}\nPublication year: ${pub_year}

Run And Quit Application
    Input  q
    Run Application
