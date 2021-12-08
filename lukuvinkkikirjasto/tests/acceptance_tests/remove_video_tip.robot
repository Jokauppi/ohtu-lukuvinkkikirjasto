*** Settings ***
Resource  resource.robot
Test Setup  Setup App And Input Add Video Command

*** Test Cases ***
Remove Existing Video Tip
    Add Video Tip  Title  www.example.com/video
    Delete Video Tip  Title  www.example.com/video
    
    Database Should Not Contain Video  Title  www.example.com/video

Remove Nonexisting Video Tip
    Delete Video Tip  Title  www.example.com/video
    
    Database Should Not Contain Video  Title  www.example.com/video

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
