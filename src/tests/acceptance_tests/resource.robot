*** Settings ***
Library  ../../AppLibrary.py

*** Keywords ***
Input Login Command
    [Arguments]  ${command}
    Input  ${command}
