*** Settings ***
Resource  resource.robot
Test Setup  Setup Application

*** Test Cases ***
Add Tag For Book Tip
    Add Book Tip To Service  book1  writer1  11111-11111-11111  2000
    Input Command  c
    Input Command  0
    Input Command  t
    Input Command  a
    Input Command  tag
    Input Command  p
    Run And Quit Application

    Output Should Contain Book  book1  writer1  11111-11111-11111  2001  False  ${EMPTY}  tag

Add Tag For Video Tip
    Add Video Tip To Service  Video1  video.example.com/1
    Input Command  c
    Input Command  0
    Input Command  t
    Input Command  a
    Input Command  tag
    Input Command  p
    Run And Quit Application
    Run And Quit Application

    Output Should Contain Video  Video1  video.example.com/1  False  ${EMPTY}  tag

Add Tag For Blog Tip
    Add Blog Tip To Service  Name1  Author1  www.example.com/blog1
    Input Command  c
    Input Command  0
    Input Command  t
    Input Command  a
    Input Command  tag
    Input Command  p
    Run And Quit Application
    Run And Quit Application

    Output Should Contain Blog  Name1  Author1  www.example.com/blog1  False  ${EMPTY}  tag

Add Multiple Tags
    Add Blog Tip To Service  Name1  Author1  www.example.com/blog1
    Input Command  c
    Input Command  0
    Input Command  t
    Input Command  a
    Input Command  tag1
    Input Command  c
    Input Command  0
    Input Command  t
    Input Command  a
    Input Command  tag2
    Input Command  p
    Run And Quit Application
    Run And Quit Application

    Output Should Contain Blog  Name1  Author1  www.example.com/blog1  False  ${EMPTY}  tag1, tag2

Remove Tag
    Add Blog Tip To Service  Name1  Author1  www.example.com/blog1
    Input Command  c
    Input Command  0
    Input Command  t
    Input Command  a
    Input Command  tag1
    Input Command  c
    Input Command  0
    Input Command  t
    Input Command  r
    Input Command  tag1
    Input Command  p
    Run And Quit Application
    Run And Quit Application

    Output Should Contain Blog  Name1  Author1  www.example.com/blog1  False  ${EMPTY}  tag1
    Output Should Contain Blog  Name1  Author1  www.example.com/blog1  False  ${EMPTY}  ${EMPTY}

*** Keywords ***
Setup Application
    Clear Database
    Setup App
