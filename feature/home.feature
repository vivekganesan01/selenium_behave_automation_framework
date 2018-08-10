# __author__ = "Vivek Ganesan"
Feature: TLS : Validate home page features

  @unittest @uat @prod @staging
    # To check TLS is running
  Scenario Outline: Make sure TLS in up and running
      Given Get the title of the current page "<Title>"
      Then Check the http response code for the site

    Examples:
        | Title               |
        | Home Page - The TLS |

  @unittest2 @uat @prod @staging
    # To check all the header link response code
  Scenario: Make sure all the header links are working
      Given Gather all the header link
      Then Check the http response code for the link

  @unittest3 @uat @prod @staging
    # To check subject page
  Scenario: Make sure subject page works as expected
      Given Navigate to subject category
      Then Gather all the article-section header and check the status code

  @unittest4 @uat @prod @staging
    # Check load more button on subject back
  Scenario Outline: Make sure article section doesn't hold broken article
      Given Navigate to subject category
      Then Go to the "<section>" article section
      Then Check all available article http link

    Examples:
        | section |
        | ARTS    |

  @unittest5 @uat @prod @staging
      # Check load more button on single article section
  Scenario Outline: Check the default count of the single article section page
     Given Navigate to subject category
     Then Go to the "<section>" article section
     And Make sure the default article count is not more than "<articlecount>"

    Examples:
      | section | articlecount |
      | ARTS    |   12         |

  @unittest6 @uat @prod @staging
      # Check load more button on single article section
  Scenario Outline: Make sure load more button work on single article section
        Given Navigate to subject category
        Then Go to the "<section>" article section
        And Check the load more button feature

      Examples:
        | section |
        | ARTS    |

  @unittest7 @prod
    # Check login feature
  Scenario Outline: Make sure subscribe login and logout functionality works
      Given As a user, Click on login
      And Enter "<username>" and "<password>" and login in
      Then Verify the login is success
      Then Try validating log out feature

    Examples:
        | username            | password            |
        | properties.USERNAME | properties.PASSWORD |

  @unittest8 @uat @prod @staging
    # check sub button
  Scenario: Make sure subscription page is working
      Given As a user, Click on subcription button
      Then User should be in the "Subscribe to The Times Literary Supplement" page


  @unittest9 @prod @staging
    # check private article after login
  Scenario Outline: Check the private article for logged in user
      Given As a user, Click on login
      And Enter "<username>" and "<password>" and login in
      Then Verify the login is success
      Then Open a private article under any category
      And  User should able to read the full article

    Examples:
        | username            | password            |
        | properties.USERNAME | properties.PASSWORD |


  @unittest10 @uat @prod @staging
    # check private article before login
  Scenario: Check the private article for non user
      Given Make sure user not logged in
      Then Open a private article under any category
      And User should not be able to read full article


  @unittest11 @uat @prod @staging
    # Search option
  Scenario: Validate search option in TLS
      Given Click on search
      Then Enter Mary Beard and perform search
      Then Search should return related article


  @unittest12 @uat @prod @staging
    # Validating go to top button on section
  Scenario: Validate go to top feature
      Given Open subjects page
      Then Open any section
      Then Navigate to bottom and validate go to top button

  @unittest13 @uat @prod @staging
    # validate go to on each page
  Scenario: Validate go to top on each page
      Given Click on latest edition
      Then Navigate to bottom and validate go to top button

  @unittest14 @uat @prod @staging
   # Validating go to top on article page
  Scenario: Validate go to top on single article
      Given Open subjects page
      Then Open any section
      Then Open any article inside the section
      Then Navigate to bottom and validate go to top button
