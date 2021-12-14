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
    [Arguments]  ${name}  ${author}  ${isbn}  ${pub_year}  ${comment}  ${tags}
    Output Should Contain  Title:${SPACE*3}${name}\nAuthor:${SPACE*2}${author}\nISBN:${SPACE*4}${isbn}\nYear:${SPACE*4}${pub_year}\nRead:${SPACE*4}False\nComment: ${comment}\nTags:${SPACE*4}${tags}

Output Should Contain Blog
    [Arguments]  ${name}  ${author}  ${url}  ${comment}  ${tags}
    Output Should Contain  Title:${SPACE*3}${name}\nAuthor:${SPACE*2}${author}\nurl:${SPACE*5}${url}\nRead:${SPACE*4}False\nComment: ${comment}\nTags:${SPACE*4}${tags}

Output Should Contain Video
    [Arguments]  ${title}  ${url}  ${comment}  ${tags}
    Output Should Contain  Title:${SPACE*3}${title}\nUrl:${SPACE*5}${url}\nRead:${SPACE*4}False\nComment: ${comment}\nTags:${SPACE*4}${tags}

Run And Quit Application
    Input  q
    Run Application

List Tips
    Input Command  p
