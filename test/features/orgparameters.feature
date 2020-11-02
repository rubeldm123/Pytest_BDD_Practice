@int
Feature: OrangeHRM Login with multiple user

  Scenario Outline: Login to HRM Application with multiple users
    Given I launch ORG browser
   When Enter valid "<username>"
   And Enter valid "<password>"
   And click on Submit Button
   Then I should be landing in Homepage

   Examples: User Credential
    |username | password |
    |admin    |admin123 |
    |admin1    |admin1234 |