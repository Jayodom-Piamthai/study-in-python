#think of this as a function for test case
*** Keywords ***
DIsplayMessage
    [Arguments]    ${msg}
    Log    ${msg} , sponsered by DisplayMessage keyword

*** Test Cases ***
TCKeywordDriven
    # Log message to the console
    DIsplayMessage    Hello World!!!

TCDataDriven
    [Template]    DisplayMessage
    #data driven use keyword as a template to push these words as parameter in msg
    myFirstTestCase
    TestingTemplate
