*** Settings ***
Documentation       Creating test which would work on all browser is not possible.
...                 These tests are for Chrome only.

Library             ../resources/testlibs/get_selenium_options.py
Resource            resource.robot

Suite Teardown      Close All Browsers

Test Tags           robot:skip    known issue firefox    known issue safari    known issue internet explorer


*** Test Cases ***
Chrome Browser With Selenium Options As String
    [Documentation]
    ...    LOG 1:3 DEBUG GLOB: *"goog:chromeOptions"*
    ...    LOG 1:3 DEBUG GLOB: *args": ["--disable-dev-shm-usage"?*
    Open Browser    ${FRONT PAGE}    ${BROWSER}    remote_url=${REMOTE_URL}
    ...    desired_capabilities=${DESIRED_CAPABILITIES}    options=add_argument("--disable-dev-shm-usage")
    ...    executable_path=%{WEBDRIVERPATH}

Chrome Browser With Selenium Options As String With Attribute As True
    [Documentation]
    ...    LOG 1:3 DEBUG GLOB: *"goog:chromeOptions"*
    ...    LOG 1:3 DEBUG GLOB: *args": ["--disable-dev-shm-usage"?*
    ...    LOG 1:3 DEBUG GLOB: *"--headless=new"*
    Open Browser
    ...    ${FRONT PAGE}
    ...    ${BROWSER}
    ...    remote_url=${REMOTE_URL}
    ...    desired_capabilities=${DESIRED_CAPABILITIES}
    ...    options=add_argument ( "--disable-dev-shm-usage" ) ; add_argument ( "--headless=new" )
    ...    executable_path=%{WEBDRIVERPATH}

Chrome Browser With Selenium Options With Complex Object
    [Documentation]
    ...    LOG 1:3 DEBUG GLOB: *"goog:chromeOptions"*
    ...    LOG 1:3 DEBUG GLOB: *"mobileEmulation": {"deviceName": "Galaxy S5"*
    ...    LOG 1:3 DEBUG GLOB: *args": ["--disable-dev-shm-usage"?*
    [Tags]    nogrid
    Open Browser
    ...    ${FRONT PAGE}
    ...    ${BROWSER}
    ...    remote_url=${REMOTE_URL}
    ...    desired_capabilities=${DESIRED_CAPABILITIES}
    ...    options=add_argument ( "--disable-dev-shm-usage" ) ; add_experimental_option( "mobileEmulation" , { 'deviceName' : 'Galaxy S5'})
    ...    executable_path=%{WEBDRIVERPATH}

Chrome Browser With Selenium Options Object
    [Documentation]
    ...    LOG 2:3 DEBUG GLOB: *"goog:chromeOptions"*
    ...    LOG 2:3 DEBUG GLOB: *args": ["--disable-dev-shm-usage"?*
    ${options} =    Get Chrome Options
    Open Browser    ${FRONT PAGE}    ${BROWSER}    remote_url=${REMOTE_URL}
    ...    desired_capabilities=${DESIRED_CAPABILITIES}    options=${options}
    ...    executable_path=%{WEBDRIVERPATH}

Chrome Browser With Selenium Options Invalid Method
    Run Keyword And Expect Error    AttributeError: 'Options' object has no attribute 'not_here_method'
    ...    Open Browser    ${FRONT PAGE}    ${BROWSER}    remote_url=${REMOTE_URL}
    ...    desired_capabilities=${DESIRED_CAPABILITIES}    options=not_here_method("arg1")
    ...    executable_path=%{WEBDRIVERPATH}

Chrome Browser With Selenium Options Argument With Semicolon
    [Documentation]
    ...    LOG 1:3 DEBUG GLOB: *"goog:chromeOptions"*
    ...    LOG 1:3 DEBUG GLOB: *["has;semicolon"*
    Open Browser    ${FRONT PAGE}    ${BROWSER}    remote_url=${REMOTE_URL}
    ...    desired_capabilities=${DESIRED_CAPABILITIES}    options=add_argument("has;semicolon")
    ...    executable_path=%{WEBDRIVERPATH}
