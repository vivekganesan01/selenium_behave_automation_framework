behave --no-logcapture -f allure_behave.formatter:AllureFormatter -o results ./features
allure serve %allure_result_folder%

behave --no-logcapture feature/home.feature

Thoughts :
steps :  BUILD
{
 - Jenkins pipeline to be created
    - INSTANCE (uat/prod/dev)
    - tags (@prod,@reg,@sanity,@uat,@dev,@unittest,none)
    }
    RUN
{
    - Docker instance ubuntu / selenium / python / dependent package as image
      - fetch github code
      - connect to saucelab
      - run the test
    }
    POST
{
    - Publish the result of Saucelab in Jenkins via plugin
    }
 or

PLAN B :
Slack for automation : Request for automation run
- Github
- project name
- instance
- tag
    Finally run the code in common sause lab and reply with report/status

problem : inconsistence , People will use different programming language