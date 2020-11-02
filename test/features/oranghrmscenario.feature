# Created by rubel at 10/30/2020
@smoke
Feature: OrangeHRM Login

  Scenario: Login to HRM Application
    Given I launch browser
   When Enter valid username and password
   And click on login
   Then I should landed to the HomePage


