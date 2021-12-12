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
    Output Should Contain  Title:${SPACE*2}${name}\nAuthor: ${author}\nISBN:${SPACE*3}${isbn}\nYear:${SPACE*3}${pub_year}\nRead:${SPACE*3}False\nComment:${SPACE}

Output Should Contain Blog
    [Arguments]  ${name}  ${author}  ${url}
    Output Should Contain  Title:${SPACE*2}${name}\nAuthor: ${author}\nurl:${SPACE*4}${url}\nRead:${SPACE*3}False\nComment:${SPACE}

Output Should Contain Video
    [Arguments]  ${title}  ${url}
    Output Should Contain  Title:${SPACE*2}${title}\nUrl:${SPACE*4}${url}\nRead:${SPACE*3}False\nComment:${SPACE}

Run And Quit Application
    Input  q
    Run Application

List Tips
    Input Command  p
