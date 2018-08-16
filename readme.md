SP - Automation Framework
-------------------------
author = Vivek Ganesan
Version = v1.0

Project Flow:
	 * Jenkins Pipeline -> Docker images {Chrome/Python/Selenium/Allure} -> Behave BDD python code.

Framework used : Behave

Code File and Folder Structure:
		ProjectFolder
			-- allure-results
			-- feature
			    -- po
			        -- *.py
			    -- steps
			        -- *.py
			-- utilizer_selense
			        -- utilizer.py
			-- behave.ini
			-- framework.ini
			-- Jenkinsfile
			-- pipeline.py
			-- runner_allure.sh
			-- *.log
			-- debug.log

Running the Framework:
   Entire framework is build on the behave framework as base.Behave is a python test automation framework used to
   achieve BDD - Behavior data driven in the python for testing.

   Reference : https://behave.readthedocs.io/en/latest/

   Via Jenkins :
    - Login to http://54.171.169.47/login?from=%2F
    - Trigger the {tls_qa_pipeline} project
    - At the run time, choose the environment and tags to be triggered
    OPTIONS : DEV,UAT,STAGING,PROD
    - Based on the env you chose the testcase will be executed
    - Choose the tags
    OPTIONS : prod,reg,sanity,uat,dev,unittest,none
    Note : Only above mentioned tags should be used in the .feature file
           any other tags will be ignored by the pipeline.
    - Trigger the pipeline
    - Result will be an allure report displayed in the jenkins GUI

    FOR SLACK NOTIFICATION about the Jenkins build : Subscribe to NTS_QA_AUTOMATION

    Architecture:
      - Jenkins is using a open ocean plugin for pipeline and its running on EC2
      - Jenkinsfile available in this framework will deploy a docker image
        {vivekjarvis/sele_py_jar_allure:v1.0} in the EC2 container
      - This docker image is build with debian os
      - Docker container consists of Debian jessey 8, Chrome stable version,
        Chrome driver, Java 1.8, Python 3.6, Pip3, Allure2 in-build
      - All the framework code and feature file will be running inside this docker container
      - Once test completes the result will be displayed as allure report

Files:
    - environment.py
      * consists of all the hooks for behave framework
            - Browser config
            - log
    - utilizer.py
        * consists of all selenium custom code - core file
    - framework.ini
        * Config file consists of all the environment parameter
          - URL
          - BROWSER
          - TIME LAZY loading
          - APPLICATION NAME
          - EMAIL
          NOTE : For all UAT/DEV/PROD/STAGING

requirement.txt:
   * Python package to be installed mandatory

-------------------------------------------------------------------------------------------
MAIN RUNNER FILE :
 * pipeline.py
        - To be triggered by jenkins pipeline.
 * runner_allure.sh
        - Main core runner file for excuting test case via behave
--------------------------------------------------------------------------------------------
Via commandline: Go to project folder -
 * ./behave -D instance={} --tags={} -f allure_behave.formatter:AllureFormatter -o allure-results feature

    PARAM : instance = UAT/DEV/PROD/STAGING
            --tags = prod,reg,sanity,uat,dev,unittest,none

    eg:
    ./behave -D instance=UAT --tags=prod -f allure_behave.formatter:AllureFormatter -o allure-results feature

Pre requirement:
  - Python3
  - requirement.txt
  - Complete Framework {from git}
  - allure
  - java 1.8

Else :
  - Install Docker
  - Download Image {vivekjarvis/sele_py_jar_allure:v1.0}
  - Run docker image
  - Copy all the code
  - Run the CMD
   eg:
    ./behave -D instance=UAT --tags=prod -f allure_behave.formatter:AllureFormatter -o allure-results feature

