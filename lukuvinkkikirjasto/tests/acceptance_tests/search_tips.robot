*** Settings ***
Resource  resource.robot
Test Setup  Setup App And Input Add Blog Command


*** Test Cases ***
Search For Book Tip
    Add Book Tip To Service  book1  writer1  11111-11111-11111  2000
    Add Book Tip To Service  book2  writer2  22222-22222-22222  2001
    Input Command  s
    Input Command  k
	Input Command  book1
	Input Command  writer1
	Input Command  11111-11111-11111
	Input Command  2000
	Input Command  E
    Run And Quit Application

    Output Should Contain Book  book1  writer1  11111-11111-11111  2000



Search For Video Tip
    Add Video Tip To Service  Video1  video.example.com/1
    Add Video Tip To Service  Video2  video.example.com/2
    Input Command  s
    Input Command  v
	Input Command  Video1
	Input Command  video.example.com/1
	Input Command  E
    Run And Quit Application

    Output Should Contain Video  Video1  video.example.com/1

Search For Blog Tip
    Add Blog Tip To Service  Blog1  Author1  blog.example.com/1
    Add Blog Tip To Service  Blog2  Author2  blog.example.com/2
    Input Command  s
    Input Command  b
	Input Command  Blog1
	Input Command  Author1
	Input Command  blog.example.com/1
	Input Command  E
    Run And Quit Application

    Output Should Contain Blog  Blog1  Author1  blog.example.com/1


*** Keywords ***
Setup App And Input Add Blog Command
    Clear Database
    Setup App

Add Blog Tip
    [Arguments]  ${name}  ${author}  ${url}
    Input Blog Tip  ${name}  ${author}  ${url}
    Run And Quit Application