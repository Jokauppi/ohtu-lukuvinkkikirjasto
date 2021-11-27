*** Settings ***
Library  ../../app_library.py

*** Keywords ***
Input Command
    [Arguments]  ${command}
    Input  ${command}

Input Book Tip
    [Arguments]  ${name}  ${author} ${isbn} ${author}
    Input  ${username}
    Input  ${password}
    Run Application
