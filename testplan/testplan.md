# Summary:

The focus of this test plan is to verify the functional correctness of the solar panel monitor's state machine 
and the notification logic to the customer in the event of zero generation conditions.

# Feature Overview:

The solar panel's monitor has an alerting state machine that accurately sets the state of a panel. 
The state can be in one of 'Open', 'Acknowledged', or 'Closed' state depending upon the existence
of a new or existing zero generation condition, and whether it is acknowledged by the customer.
In addition, there is business requirement that an email alert be sent to the user in the event of a new zero
generation condition, and to be continually notified daily of such a condition until the user acknowledges it, and 
to stop sending the email notification when the zero generation condition is 'Closed'. 

For additional details on the business logic refer to : https://github.com/AlsoEnergyInc/QACodingChallenge

# Test Plan Stakeholders:

- Development - Lead Engineer and Architect
- Development - Alerts and notification feature developer
- Quality Engineering - Lead Engineer and Architect
- Quality Engineering - Feature test engineer
- Product Management - Product Lead and Product Owner

# Entry/Exit Criteria For Testing:

## Entry criteria:

Before this feature is ready for functional and regression testing the following needs to be complete:
- The acceptance criteria for the feature is established 
- The dev team has good coverage with unit tests
- A stable build is available from the correct dev or staging branch for testing
- Test data and test environment are ready whereby real solar panels are not required for testing. 
To support frequent CI based or ad hoc testing purposes, at the very least, an API driven solar panel 
simulator that works with the same code as production is available in the test lab environment. A final
test run will be executed on a real solar panel to verify the functionality on a complete end-to-end product.


## Exit criteria:

This feature will exit testing when:
- Feature meets business requirements
- No outstanding high priority and high severity defects remain to be addressed

# What will be tested and automated:
- The alerting state machine will be tested and automated. 
- The notification logic will be tested and automated.
- Automated tests will be integrated as a separate stage in the CI pipeline for regular testing

# What will not be tested:
- This test plan covers the software and API functionality only. So, the solar panel's sensitivity and 
accuracy to detect and trigger zero generation conditions is out of the scope of testing.

# Defects:
All defects will be reported using the standard defect tracker used by the team.

# Test Environments:
The QA test environment will be used for this test cycle.

# Test Cases:

## Alerting Test Cases:

- After a **new** zero generation condition the alert status is set to **'Open'**
- After an **existing** zero generation condition is *'Acknowledged'* by user, the alert status is set to **'Acknowledged'**
- After an **existing** zero generation condition **stops occurring**, the alert status is set to **'Closed'**

## Notification Test Cases:

- After a *new zero generation* condition (day 0) an **alert email is sent** to the user
- After an *existing zero generation* condition (day 1) and *not  'Acknowledged' by user* an alert **email is re-sent** to the user
- After an *existing zero generation* condition *is 'Acknowledged'* by user, **no longer alert email is sent** to the user
- After a zero generation condition is *set to 'Closed'* (day 0) an **email is sent** to the user
- After a zero generation condition is *set to 'Closed' (day 1)* **no email is sent** to the user (normal operation)

## Sunset/Sunrise Test Cases:

- When *'Sunrise'* is set to True, all *alerting and notification test cases* described above **should work as designed.**
    - Setting 'Sunrise' to True can be a pre-condition to the above tests easily done with the use of setup fixtures.
- When *'Sunset'* is set to True, all *alerting and notification will be disabled*. In this condition, the *alerts state 
machine will not change any states and no emails will be sent to the user.*
    - Setting 'Sunset' to True can be a pre-condition to the above tests and test assertions will be changed to verify 
    that **no** state changed nor notification emails were sent.