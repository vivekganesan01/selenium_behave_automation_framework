behave --no-logcapture -f allure_behave.formatter:AllureFormatter -o results ./features
allure serve %allure_result_folder%

behave --no-logcapture feature/home.feature

behave --no-logcapture -D instance=UAT --tags=@uat -f allure_behave.formatter:AllureFormatter -o allure-results feature