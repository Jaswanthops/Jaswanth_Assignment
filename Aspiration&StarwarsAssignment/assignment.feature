Feature: Validation for Aspiration by Jaswanth Kallem

  Scenario: As a user, I can view Customer products and prices by clicking Spend and Save Link
    Given Launch browser navigates to aspiration.com home page
    When User clicks on Spend and Save link
    And Click on Get Aspiration button
    Then Verify that a modal containing input field for an email address to sign up appears
    And Close the email modal box check that Two products are shown again
    And Click on Get Aspiration Plus button
    Then Verify that Get Aspiration Plus have A modal with monthly and yearly plans
    Then Verify that Yearly plan shows $71.88 as a price per Year
    And Verify that Yearly plan shows $7.99 as a price per Month
