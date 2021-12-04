*** Settings ***
Resource  resource.robot
Test Setup  Setup App And Input Add Video Command

*** Test Cases ***
Add Video Tip With Valid Data
    Add Video Tip  Title  www.example.com/video
    Output Should Contain  Video lisätty
    Database Should Contain Video  Title  www.example.com/video

Add Video Tip With Invalid Title
    Add Video Tip  ${EMPTY}  www.example.com/video
    Output Should Contain  Otsikon pituus pitää olla 1-100 merkkiä
    Output Should Contain  Videon lisäys ei onnistunut

Add Video Tip With Invalid Url
    Add Video Tip  Title  ${EMPTY}
    Output Should Contain  url pituus pitää olla 5-100 merkkiä
    Output Should Contain  Videon lisäys ei onnistunut

*** Keywords ***
Setup App And Input Add Video Command
    Clear Database
    Setup App
    Input Command  a
    Input Command  v

Add Video Tip
    [Arguments]  ${title}  ${url}
    Input Video Tip  ${title}  ${url}
    Run And Quit Application
