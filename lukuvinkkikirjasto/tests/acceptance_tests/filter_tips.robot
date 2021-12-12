*** Settings ***
Resource  resource.robot
Test Setup  Setup Application

*** Test Cases ***
List Tips With Empty Filter
    Save Filter
    List Tips
    Run And Quit Application

    Output Should Contain Book  book1  writer1  11111-11111-11111  2000
    Output Should Contain Book  book2  writer1  22222-22222-22222  2001
    Output Should Contain Book  book3  writer2  33333-33333-33333  2002
    Output Should Contain Book  book4  writer2  44444-44444-44444  2000
    Output Should Contain Book  book5  writer1  55555-55555-55555  2000
    Output Should Contain Blog  blog1  blogger1  blog.example.com/1
    Output Should Contain Blog  blog2  blogger1  blog.example.com/2
    Output Should Contain Blog  blog3  blogger2  blog.example.com/3
    Output Should Contain Video  video1  video.example.com/1
    Output Should Contain Video  video2  video.example.com/2
    Output Should Contain Video  video3  video.example.com/3


List Tips With Name Filter
    Filter By Name  book1
    Save Filter
    List Tips
    Run And Quit Application

    Output Should Contain Book  book1  writer1  11111-11111-11111  2000


List Tips With Author Filter
    Filter By Author  writer1
    Save Filter
    List Tips
    Run And Quit Application

    Output Should Contain Book  book1  writer1  11111-11111-11111  2000
    Output Should Contain Book  book2  writer1  22222-22222-22222  2001
    Output Should Contain Book  book5  writer1  55555-55555-55555  2000


List Tips With ISBN Filter
    Filter By ISBN  22222-22222-22222
    Save Filter
    List Tips
    Run And Quit Application

    Output Should Contain Book  book2  writer1  22222-22222-22222  2001


List Tips With Year Filter
    Filter By Year  2000
    Save Filter
    List Tips
    Run And Quit Application

    Output Should Contain Book  book1  writer1  11111-11111-11111  2000
    Output Should Contain Book  book4  writer2  44444-44444-44444  2000
    Output Should Contain Book  book5  writer1  55555-55555-55555  2000


List Tips With Url Filter
    Filter By Url  video.example.com/2
    Save Filter
    List Tips
    Run And Quit Application

    Output Should Contain Video  video1  video.example.com/1


List Tips After Resetting Filters
    Filter By Name  book1
    Save Filter
    Open Filter Menu
    Reset Filters
    Save Filter
    List Tips
    Run And Quit Application

    Output Should Contain Book  book1  writer1  11111-11111-11111  2000
    Output Should Contain Book  book2  writer1  22222-22222-22222  2001
    Output Should Contain Book  book3  writer2  33333-33333-33333  2002
    Output Should Contain Book  book4  writer2  44444-44444-44444  2000
    Output Should Contain Book  book5  writer1  55555-55555-55555  2000
    Output Should Contain Blog  blog1  blogger1  blog.example.com/1
    Output Should Contain Blog  blog2  blogger1  blog.example.com/2
    Output Should Contain Blog  blog3  blogger2  blog.example.com/3
    Output Should Contain Video  video1  video.example.com/1
    Output Should Contain Video  video2  video.example.com/2
    Output Should Contain Video  video3  video.example.com/3


List Tips With Author And Year Filters
    Filter By Author  writer1
    Filter By Year  2000
    Save Filter
    List Tips
    Run And Quit Application

    Output Should Contain Book  book1  writer1  11111-11111-11111  2000
    Output Should Contain Book  book5  writer1  55555-55555-55555  2000


*** Keywords ***
Setup Application
    Clear Database
    Setup App
    Add Tips
    Open Filter Menu

Open Filter Menu
    Input Command  f

Filter By Name
    [Arguments]  ${name}
    Input Command  n
    Input  ${name}

Filter By Author
    [Arguments]  ${author}
    Input Command  w
    Input  ${author}

Filter By ISBN
    [Arguments]  ${isbn}
    Input Command  i
    Input  ${isbn}

Filter By Year
    [Arguments]  ${year}
    Input Command  y
    Input  ${year}

Filter By Url
    [Arguments]  ${url}
    Input Command  u
    Input  ${url}

Filter By Read
    [Arguments]  ${read}
    Input Command  r
    Input  $‚{read}

Reset Filters
    Input Command  c

Save Filter
    Input Command  s

Add Tips
    Add Book Tip To Service  book1  writer1  11111-11111-11111  2000
    Add Book Tip To Service  book2  writer1  22222-22222-22222  2001
    Add Book Tip To Service  book3  writer2  33333-33333-33333  2002
    Add Book Tip To Service  book4  writer2  44444-44444-44444  2000
    Add Book Tip To Service  book5  writer1  55555-55555-55555  2000
    Add Video Tip To Service  video1  video.example.com/1
    Add Video Tip To Service  video2  video.example.com/2
    Add Video Tip To Service  video3  video.example.com/3
    Add Blog Tip To Service  blog1  blogger1  blog.example.com/1
    Add Blog Tip To Service  blog2  blogger1  blog.example.com/2
    Add Blog Tip To Service  blog3  blogger2  blog.example.com/3
    