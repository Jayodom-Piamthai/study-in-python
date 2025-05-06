*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${url}            https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
${browser}        edge

*** Keywords ***
Test Browser
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
