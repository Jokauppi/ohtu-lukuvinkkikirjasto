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

Input Blog Tip
    [Arguments]  ${name}  ${author}  ${url}
    Input  ${name}
    Input  ${author}
    Input  ${url}

Input Video Tip
    [Arguments]  ${title}  ${url}
    Input  ${title}
    Input  ${url}

Output Should Contain Book
    [Arguments]  ${name}  ${author}  ${isbn}  ${pub_year}
    Output Should Contain  Title:${SPACE*2}${name}\nAuthor: ${author}\nISBN:${SPACE*3}${isbn}\nYear:${SPACE*3}${pub_year}\n

Output Should Contain Blog
    [Arguments]  ${name}  ${author}  ${url}
    Output Should Contain  Title:${SPACE*2}${name}\nAuthor: ${author}\nISBN:${SPACE*3}${url}\n

Output Should Contain Video
    [Arguments]  ${title}  ${url}
    Output Should Contain  Title:${SPACE*2}${title}\nUrl:${SPACE*4}${url}\n

Run And Quit Application
    Input  q
    Run Application
