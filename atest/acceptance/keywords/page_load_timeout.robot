*** Settings ***
Resource            ../resource.robot

Suite Teardown      Switch Back To Suite Browser
Test Teardown       Close Browser And Reset Page Load Timeout


*** Test Cases ***
Should Open Browser With Default Page Load Timeout
    [Documentation]    Verify that 'Open Browser' changes the page load timeout.
    ...    LOG 1.1.1:27 DEBUG REGEXP: POST http://localhost:\\d{2,5}/session/[a-f0-9-]+/timeouts {"pageLoad": 300000}
    ...    LOG 1.1.1:29 DEBUG STARTS: Remote response: status=200
    # Note: previous log check was 33 and 37. Recording to see if something is swtiching back and forth
    Open Browser To Start Page

Should Run Into Timeout Exception
    Open Browser To Start Page
    Set Selenium Page Load Timeout    1 ms
    Run Keyword And Expect Error    *Timeout*    Reload Page

Should Set Page Load Timeout For All Opened Browsers
    [Documentation]    One browser is already opened as global suite setup.
    ...    LOG 2:1 DEBUG REGEXP: POST http://localhost:\\d{2,5}/session/[a-f0-9-]+/timeouts {"pageLoad": 5000}
    ...    LOG 2:5 DEBUG REGEXP: POST http://localhost:\\d{2,5}/session/[a-f0-9-]+/timeouts {"pageLoad": 5000}
    Open Browser To Start Page
    Set Selenium Page Load Timeout    5 s


*** Keywords ***
Close Browser And Reset Page Load Timeout
    Close Browser
    Set Selenium Page Load Timeout    5 minutes

Switch Back To Suite Browser
    Switch Browser    keywords
