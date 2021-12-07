*** Settings ***
Resource  resource.robot
Test Setup  Setup App And Input Add Blog Command

*** Test Cases ***
Add Blog Tip With Valid Data
    Add Blog Tip  Name  Author  www.example.com/blog
    Output Should Contain  Blogi lisätty
    Database Should Contain Blog  Name  Author  www.example.com/blog

Add Blog Tip With Invalid Title
    Add Blog Tip  ${EMPTY}  Author  www.example.com/blog
    Output Should Contain  Nimen pituus pitää olla 1-100 merkkiä
    Output Should Contain  Blogin lisäys ei onnistunut

Add Blog Tip With Invalid Author
    Add Blog Tip  Name  ${EMPTY}  www.example.com/blog
    Output Should Contain  Nimen pituus pitää olla 1-100 merkkiä
    Output Should Contain  Blogin lisäys ei onnistunut

Add Blog Tip With Invalid Url
    Add Blog Tip  Name  Author  ${EMPTY}
    Output Should Contain  url pituus pitää olla 5-100 merkkiä
    Output Should Contain  Blogin lisäys ei onnistunut

*** Keywords ***
Setup App And Input Add Blog Command
    Clear Database
    Setup App
    Input Command  a
    Input Command  b

Add Blog Tip
    [Arguments]  ${name}  ${author}  ${url}
    Input Blog Tip  ${name}  ${author}  ${url}
    Run And Quit Application
