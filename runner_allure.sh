#!/bin/bash
# __author__ = "Vivek Ganesan"

echo "<< +++ EXECUTING BATCH FILE +++ >>"

echo "<< +++ Running BEHAVE CMD : $1"

#behave --no-logcapture --tags=$1 -f allure_behave.formatter:AllureFormatter -o allure_result_folder $2
#allure serve allure_result_folder

xvfb-run --server-args="-screen 0 1024x768x24"
behave --no-logcapture $1

echo "------------------------------------- END OF SH --------------------------------------------------"

