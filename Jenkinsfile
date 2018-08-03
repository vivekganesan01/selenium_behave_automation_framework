pipeline {
    agent {
       docker {
			image 'vivekjarvis/sp_py_selenese:latest'
		}
    }
    parameters {
		choice(name: 'TEST_ENV', choices: 'DEV\nUAT\nSTAGING\nPROD', description: 'Testing environment:')
		choice(name: 'TAGS', choices: 'prod\nreg\nsanity\nuat\ndev\nunittest\nnone', description: 'Tags to be executed:')
    }
    stages {
        stage('Build') {
            steps {
                slackSend (color: '#439FE0', message: "BUILD RUNNING")
                echo "BUILD : Running"
                slackSend (color: 'good', message: "BUILD: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
            }
        }
        stage('Execute') {
            steps {
                slackSend (color: 'warning', message: "BUILD RUNNING")
                echo "PIPELINE : "
                sh 'python3 pipeline.py'
                slackSend (color: 'good', message: "EXECUTE: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
            }
        }
        stage('Deploy') {
            steps {
                echo "DEPLOY:"
                slackSend (color: '#439FE0', message: "DEPLOYMENT SUCCESSFULL : Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
            }
        }
    }
}