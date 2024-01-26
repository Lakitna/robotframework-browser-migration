*** Settings ***
Library     SeleniumLibraryToBrowser    run_on_failure=Nothing    implicit_wait=5 seconds
Library     Collections
Library     OperatingSystem
Library     DateTime


*** Variables ***
${SERVER}                   localhost:7000
${BROWSER}                  chrome
${REMOTE_URL}               ${NONE}
${DESIRED_CAPABILITIES}     ${NONE}
${ROOT}                     http://${SERVER}/html
${FRONT_PAGE}               ${ROOT}/
${SPEED}                    0


*** Keywords ***
Open Browser To Start Page
    [Documentation]    This keyword also tests 'Set Selenium Speed' and 'Set Selenium Timeout'
    ...    against all reason.
    [Arguments]    ${alias}=${None}
    ${default speed}    ${default timeout} =    Open Browser To Start Page Without Testing Default Options
    ...    ${alias}
    # FIXME: We shouldn't test anything here. If this stuff isn't tested elsewhere, new *tests* needs to be added.
    # FIXME: The second test below verifies a hard coded return value!!?!
    Should Be Equal    ${default speed}    0 seconds
    Should Be Equal    ${default timeout}    5 seconds

Open Browser To Start Page Without Testing Default Options
    [Documentation]    Open Browser To Start Page Without Testing Default Options
    [Arguments]    ${alias}=${None}
    Open Browser    ${FRONT PAGE}    ${BROWSER}    remote_url=${REMOTE_URL}
    ...    desired_capabilities=${DESIRED_CAPABILITIES}    alias=${alias}
    ${orig speed} =    Set Selenium Speed    ${SPEED}
    ${orig timeout} =    Set Selenium Timeout    5 seconds
    RETURN    ${orig speed}    5 seconds

Cannot Be Executed In IE
    [Documentation]    Cannot Be Executed In IE
    ${runsInIE} =    Set Variable If
    ...    "${BROWSER}".replace(' ', '').lower() in ['ie', '*iexplore', 'internetexplorer']
    ...    ${TRUE}
    IF    ${runsInIE}    Set Tags    ie-incompatible
    IF    ${runsInIE}
        Fail And Set Non-Critical    This test does not work in Internet Explorer
    END

Fail And Set Non-Critical
    [Documentation]    Fails And Set Non-Critical
    [Arguments]    ${msg}
    Remove Tags    regression
    Fail    ${msg}

Go to Front Page
    [Documentation]    Goes to front page
    Go To    ${FRONT PAGE}

Go To Page "${relative url}"
    [Documentation]    Goes to page
    Go To    ${ROOT}/${relative url}

Set ${level} Loglevel
    [Documentation]    Sets loglevel
    Set Log Level    ${level}

Verify Location Is "${relative url}"
    [Documentation]    Verifies location
    Wait Until Keyword Succeeds    5    1    Location Should Be    ${ROOT}/${relative url}

Set Global Timeout
    [Arguments]    ${timeout}
    ${previous} =    Set Selenium timeout    ${timeout}
    Set Suite Variable    ${PREVIOUS TIMEOUT}    ${previous}

Restore Global Timeout
    Set Selenium timeout    ${PREVIOUS TIMEOUT}
