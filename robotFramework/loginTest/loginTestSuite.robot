Language: English

*** Variables ***
${loginSite}      file:///C:/Outie%20stuff/study-in-python/robotFramework/loginTest/html/index.html
${browser}        edge
${failurePage}    file:///C:/Outie%20stuff/study-in-python/robotFramework/loginTest/html/loginfailed.html

*** Keywords ***
openLoginPage
    [Arguments]    ${SiteName}    ${browserChoice}
    Open browser    ${SiteName}    ${browserChoice}
    Log To Console    Initializing test
    Maximize Browser Window
    Title Should Be    login page

Test login
    [Arguments]    ${email}    ${password}
    [Setup]    Open Browser    ${loginSite}    ${browser}
    Log    what the hekk
    Input Text    email    ${email}
    Input Text    passwd    ${password}
    Click Button    btnsubmit
    [Teardown]    Close Browser

loginShouldFailed
    Location Should Be    ${failurePage}
    Title Should Be    Login Failed

*** Settings ***
Library           SeleniumLibrary
