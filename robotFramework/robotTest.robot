*** Test Cases ***
TC0
    pass    
TC1
    [Documentation]    test case number one for robotframework test
    Log To Console    this is the first proper test case
    Log To Console    seems like its a success!

TC1.L
    [Documentation]    fail test
    LO    \    this is fail test case with typo to see error respond and log]
