
*** Settings ***
Library           SeleniumLibrary
Resource          resources/resource1.robot

*** Test Cases ***
TC1
    [Documentation]    Test case for selenium library for web browser interactions
    #you can even choose browser for this! wahoo!
    Open Browser    https://www.tutorialspoint.com/robot_framework/robot_framework_writing_and_executing_test_cases.htm    edge
    Maximize Browser Window
    Minimize Browser Window
    Close Browser

TC2
    [Tags]    TC2
    ${number}    Set Variable    3
    ${a}    Set Variable    Hi
    Log    ${a}
    ${b}    Set Variable If    ${number}>0    Yes    No
    Log    ${b}

TC3
    #we import resource from resource folder - this will import test and varible from there to use here
    Test Browser
    Close Browser
