#!/bin/bash

echo "**** Executing ****"

echo "*** Running $1"

#behave --no-logcapture --tags=$1 -f allure_behave.formatter:AllureFormatter -o allure_result_folder $2

#allure serve allure_result_folder

behave --no-logcapture $1

echo "-----------------------END-------------------------------------------------------------------------------------"

