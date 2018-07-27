#!/bin/bash

echo "**** Executing ****"

echo "*** Running tags $1"
echo "*** Feature File $2"

behave --no-logcapture --tags=$1 -f allure_behave.formatter:AllureFormatter -o allure_result_folder $2

allure serve allure_result_folder

echo "-----------------------END-------------------------------------------------------------------------------------"

