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
    Output Should Contain  Title:${SPACE*2}${name}\nAuthor: ${author}\nISBN:${SPACE*3}${isbn}\nYear:${SPACE*3}${pub_year}\n

Run And Quit Application
    Input  q
    Run Application
