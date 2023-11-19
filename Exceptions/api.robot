*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    OperatingSystem
Library     SeleniumLibrary
Library     Collections


*** Test Cases ***
validate the sample curl
    ${json_data}       load json from file    ${CURDIR}\\test.json
#    ${headers}          Create Dictionary    Accept=application/json, text/plain, */*    Content-Type=application/json    Cookie=_engineerai_session=MHZGRHJObFBNcU9ReWswMGhXUUZvdjJCNTFjNmt5QmdpeXZJb1B2ODBLOWNReW5UZ2hPSzh2UGxua1V2WVlaSWpJOFA0MzI5eHozZnJzcmtqUXc5TXc9PS0tSXI3WVBJdVRtUWczcVJGazA3b3poZz09--b4a5cb0d70a2047c9849a61a04d5a41e76ef23f9; _session_id=TU1XWXFCd3ptUlNOZ0ZNV2l6OHJrTzBYK041UmNveFcrZE5LbTMwSVZjWVQ3MHR4Tm9PbVlKeW9WOGMwRnQ3c0tSWkpjNDJOL2VJS2tnVW04OTZPSVE9PS0tNmVHSmk4bllLSzhacUJudmo3emtFQT09--3b2cfa8041621c8d6c4a1cb3bf7a22849c512b65

#    ${json_data}        evaluate    {"user": {"first_name": "Test", "last_name": "", "email": "Felicia.Roberts78@hotmail.com", "password": "12345678", "phone_number": "+91-8285408009", "user_type": "User", "currency_id": 1}}

    log to console    ${json_data}
    ${resp}     POST    https://api-staging-builder.engineer.ai/users       json=${json_data}      expected_status=422
    log to console    ${resp.json()}