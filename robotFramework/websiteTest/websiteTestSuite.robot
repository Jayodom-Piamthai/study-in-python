*** Keywords ***
Open Dummy HTML
    [Documentation]    automatically open dummy HTML file,its not that nescessary but it is to show what keyword can do
    ...    as something akin to function for robotframework
    Open Browser    ${testHTML}    edge

*** Variables ***
${testHTML}       file:///C:/Outie%20stuff/study-in-python/robotFramework/websiteTest/radiobutton.html
@{listVariable}    exampleUser    exaexample@gmail.com
&{dictionaryVariable}    name=ace,jay,em    city=madrid,bangkok,heinan
#variable for database connection
${dbname}         customers
${dbuser}         root
${dbpasswd}       admin
${dbhost}         localhost
${dbport}         3306
@{queryResults}

*** Settings ***
Library           SeleniumLibrary
Library           DatabaseLibrary

*** Test Cases ***
TC-Textbox
    # Log message to the console
    Open Browser    https://magento.softwaretestingboard.com/    edge
    Input Text    name:q    robot Framework    #input "robot framework into text field named 'q'"
    Press Keys    name:q    ENTER    #press of a function button need to be uppercase , letters are lowercase

TC-RadioButton
    Open Dummy HTML
    Select Radio Button    gender    female

TC-Checkbox
    #add open browser later if you want to test this one solo
    Select Checkbox    name:option3

TC-DropdownBox
    Select From List By Value    name:year    3    #03 and 3 is not the same for robot
    Select From List By Index    name:days    21
    Select From List By Label    name:months    April    #case sensitive , so careful about that too
    Sleep    5    seconds

TC-variableTest
    Log    ${testHTML}
    Log Many    ${listVariable}    #variables all use $ to call even if its a list or a dict
    Log    index 1 of listVariable is:${listVariable}[1]
    Log Many    ${dictionaryVariable}
    Log    ${dictionaryVariable}[name]

TC-SetupTeardown
    [Setup]    Open Browser    https://www.bing.com/images/search?q=rick+astley&form=HDRSC3&first=1    edge    # open an image of rick astley in bing
    #setup run at the start of test,teardown run at the end of test
    Log    omg its rick astley
    [Teardown]    Close Browser

TC-DatabaseTest
    Connect To Database    pymysql    ${dbname} ${dbuser}${dbpasswd} ${dbhost} ${dbport}
    Table Must Exist    customer
    Check If Exists In Database    SELECT * FROM customer
    @{queryResults}    Query    SELECT * FROM customer
    Log    @{queryResults}[0]
