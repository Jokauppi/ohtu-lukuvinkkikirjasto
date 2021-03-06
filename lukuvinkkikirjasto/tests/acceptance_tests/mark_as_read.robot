*** Settings ***
Resource  resource.robot
Test Setup  Setup Application

*** Test Cases ***
Mark Book Tip As Read
    Add Book Tip To Service  book1  writer1  11111-11111-11111  2000
    Add Book Tip To Service  book2  writer2  22222-22222-22222  2001
    Input Command  c
    Input Command  1
    Input Command  r
    Input Command  p
    Run And Quit Application

    Output Should Contain Book  book2  writer2  22222-22222-22222  2001  True  ${EMPTY}  ${EMPTY}

Mark Video Tip As Read
    Add Video Tip To Service  Video1  video.example.com/1
    Add Video Tip To Service  Video2  video.example.com/2
    Input Command  c
    Input Command  1
    Input Command  r
    Input Command  p
    Run And Quit Application

    Output Should Contain Video  Video2  video.example.com/2  True  ${EMPTY}  ${EMPTY}

*** Keywords ***
Setup Application
    Clear Database
    Setup App
