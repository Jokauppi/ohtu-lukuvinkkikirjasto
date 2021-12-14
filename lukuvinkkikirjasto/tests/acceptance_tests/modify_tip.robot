*** Settings ***
Resource  resource.robot
Test Setup  Setup Application

*** Test Cases ***
Modify Book Tip
    Add Book Tip To Service  book1  writer1  11111-11111-11111  2000
    Add Book Tip To Service  book2  writer2  22222-22222-22222  2001
    Input Command  c
    Input Command  0
    Input Command  m
    Input Command  t
    Input Command  book1_muokattu
    Input Command  c
    Input Command  0
    Input Command  m
    Input Command  p
    Input Command  1000
    Input Command  p
    Run And Quit Application

    Output Should Contain Book  book1_muokattu  writer1  11111-11111-11111  1000  ${EMPTY}  ${EMPTY}

Modify Video Tip
    Add Video Tip To Service  Video1  video.example.com/1
    Add Video Tip To Service  Video2  video.example.com/2
    Input Command  c
    Input Command  0
    Input Command  m
    Input Command  t
    Input Command  video1_muokattu
    Input Command  c
    Input Command  0
    Input Command  m
    Input Command  u
    Input Command  url_muokattu
    Input Command  p
    Run And Quit Application

    Output Should Contain Video  video1_muokattu  url_muokattu  ${EMPTY}  ${EMPTY}

Modify Blog Tip
    Add Blog Tip To Service  Name1  Author1  www.example.com/blog1
    Add Blog Tip To Service  Name2  Author2  www.example.com/blog2
    Input Command  c
    Input Command  0
    Input Command  m
    Input Command  a
    Input Command  author_muokattu
    Input Command  c
    Input Command  0
    Input Command  m
    Input Command  u
    Input Command  url_muokattu
    Input Command  p
    Run And Quit Application

    Output Should Contain Blog  Name1  author_muokattu  url_muokattu  ${EMPTY}  ${EMPTY}


*** Keywords ***
Setup Application
    Clear Database
    Setup App
