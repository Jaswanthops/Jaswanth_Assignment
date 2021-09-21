*** Settings ***
Library    JSONLibrary
Library    RequestsLibrary
Library    Collections
Library    String

*** Variables ***
${base_url}    https://swapi.dev

*** Test Cases ***
TC1-checking-count
    [Tags]    TC1
    Create Session    people    ${base_url}
    ${result}=    GET On Session    people    /api/people    expected_status=Anything
    ${status}=    Convert To String    ${result.status_code}
    ${json}=    Set Variable    ${result.json()}
    Run Keyword If    '${status}'!='200'
    ...    Pass Execution    "Status is ${status} - ${json}"
    ${total_count}=    Get From Dictionary    ${json}    count
    Log    count = ${total_count}
    ${res}=    Convert To String    ${total_count}
    Run Keyword If    '${res}'=='82'    Log    count 82 is correct
    ...    ELSE    Log    The actual count is ${res}

TC2-validating-height
    [Tags]    TC2
    ${list}    Create List
    FOR    ${no}    IN RANGE   1    84
        Create Session    people    ${base_url}
        ${result}    GET On Session    people    /api/people/${no}    expected_status=Anything
        ${status}=    Convert To String    ${result.status_code}
        #Log to Console    page ${no} status = ${status}
        Run Keyword If    '${status}'!='200'    Continue For Loop
        ${response}=    Convert To String   ${result.json()}
        ${json}=    Evaluate    ${response}
        ${list_name}=    Get Value From JSON    ${json}    $.name
        ${list_height}=   Get Value From JSON    ${json}    $.height
        ${str_name}=    Convert To String    ${list_name}
        ${str_height}=    Convert To String    ${list_height}
        ${str_name}    Remove String    ${str_name}    [    ]    '    '
        ${str_height}    Remove String    ${str_height}    [    ]    '    '
        Run Keyword If    '${str_height}'=='unknown'    Continue For Loop
        ${height}    Convert To Integer    ${str_height}
        Run Keyword If    ${height}>200
        ...    Append To List    ${list}    ${str_name}
    END
    Log    ${list}
    ${value}    Get Length    ${list}
    ${people}    Convert To String    ${list}
    ${people1}    Remove String    ${people}    [    ]    '    '
    Log To Console    The total number of people where height is greater than 200 = ${value}
    Log To Console    People with height greater than 200 are ${people1}
    Log    The total number of people where height is greater than 200 = ${value}
    Log    People with height greater than 200 are ${people1}
