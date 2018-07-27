# __author__ = "Vivek Ganesan"
Feature: TLS : Validate home page features

  @unittest
    # To check TLS is running
  Scenario Outline: Make sure TLS in up and running
      Given Get the title of the current page "<Title>"
      Then Check the http response code for the site

    Examples:
        | Title               |
        | Home Page - The TLS |

  @unittest2
    # To check all the header link response code
  Scenario: Make sure all the header links are working
      Given Gather all the header link
      Then Check the http response code for the link

  @unittest3
    # To check subject page
  Scenario: Make sure subject page works as expected
      Given Navigate to subject category
      Then Gather all the article-section header and check the status code

  @unittest4
    # Check load more button on subject back
  Scenario Outline: Make sure article section doesn't hold broken article
      Given Navigate to subject category
      Then Go to the "<section>" article section
      Then Check all available article http link

    Examples:
        | section |
        | ARTS    |

  @unittest5
      # Check load more button on single article section
  Scenario Outline: Check the default count of the single article section page
     Given Navigate to subject category
     Then Go to the "<section>" article section
     And Make sure the default article count is not more than "<articlecount>"

    Examples:
      | section | articlecount |
      | ARTS    |   12         |

    @unittest6
      # Check load more button on single article section
    Scenario Outline: Make sure load more button work on single article section
        Given Navigate to subject category
        Then Go to the "<section>" article section
        And Check the load more button feature

      Examples:
        | section |
        | ARTS    |

  @unittest6
    # Check login button
  Scenario Outline: Make sure login functionality works
      Given As a user, Click on login
      And Enter "<username>" and "<password>" and login in
      Then User should see the logged in screen

    Examples:
        | username            | password            |
        | properties.USERNAME | properties.PASSWORD |
  # check sub button
  # check logout button
  # Check user action login
  # check private article after login
  # check private article before login
  # goto top button