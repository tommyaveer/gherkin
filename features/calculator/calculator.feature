@calculator
Feature: Calculator Functionality

  @calculate
  Scenario Outline: Calculating two numbers
    Given I have entered the number <number> into the calculator
    When I press the <op> button
    And I have entered another number <number1> into the calculator
    Then the result displayed should be <expectedResult>
    Examples:
      | number | op       | number1 | expectedResult |
      | 10     | subtract | 5       | 5              |
      | 10     | add      | 5       | 15             |
      | 20     | subtract | 5       | 15             |
      | 20     | add      | 5       | 25             |
      | 30     | subtract | 5       | 25             |
      | 30     | add      | 5       | 35             |