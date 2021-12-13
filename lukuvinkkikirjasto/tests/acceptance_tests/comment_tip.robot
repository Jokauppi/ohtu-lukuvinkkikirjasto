*** Settings ***
Resource  resource.robot
Test Setup  Setup Application

*** Test Cases ***
Comment Book Tip
    Add Book Tip To Service  book1  writer1  11111-11111-11111  2000
    Add Book Tip To Service  book2  writer2  22222-22222-22222  2001
    Input Command  c
    Input Command  1
    Input Command  c
    Input Command  kommentti
    Input Command  p
    Run And Quit Application

    Output Should Contain Book  book2  writer2  22222-22222-22222  2001  kommentti

Comment Video Tip
    Add Video Tip To Service  Video1  video.example.com/1
    Add Video Tip To Service  Video2  video.example.com/2
    Input Command  c
    Input Command  1
    Input Command  c
    Input Command  kommentti
    Input Command  p
    Run And Quit Application

    Output Should Contain Video  Video2  video.example.com/2  kommentti

Comment Blog Tip
    Add Blog Tip To Service  Name1  Author1  www.example.com/blog1
    Add Blog Tip To Service  Name2  Author2  www.example.com/blog2
    Input Command  c
    Input Command  1
    Input Command  c
    Input Command  kommentti
    Input Command  p
    Run And Quit Application

    Output Should Contain Blog  Name2  Author2  www.example.com/blog2  kommentti



*** Keywords ***
Setup Application
    Clear Database
    Setup App
