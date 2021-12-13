*** Settings ***
Resource  resource.robot
Test Setup  Setup App And Input Add Video Command

*** Test Cases ***
Remove Existing Video Tip
    Add Video Tip To Service  Title  www.example.com/video
    Input Command  c
    Input Command  0
    Input Command  d
    Run And Quit Application
    
    Database Should Not Contain Video  Title  www.example.com/video

Remove Wrong Id Video Tip
    Add Video Tip To Service  Title  www.example.com/video
    Input Command  c
    Input Command  1
    Input Command  0
    Input Command  d
    Run And Quit Application
    
    Database Should Not Contain Video  Title  www.example.com/video

*** Keywords ***
Setup App And Input Add Video Command
    Clear Database
    Setup App

Add Video Tip
    [Arguments]  ${title}  ${url}
    Input Video Tip  ${title}  ${url}
    Run And Quit Application
