*** Settings ***
Resource  resource.robot
Test Setup  Setup App And Input Add Blog Command

*** Test Cases ***
Remove Existing Blog Tip
    Add Blog Tip  Name  Author  www.example.com/blog
    Input Command  c
    Input Command  0
    Input Command  d
    Run And Quit Application
    
    Database Should Not Contain Blog  Name  Author  www.example.com/blog

Remove Nonexisting Blog Tip
    Delete Blog Tip  Name  Author  www.example.com/blog
    
    Database Should Not Contain Blog  Name  Author  www.example.com/blog

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
    
