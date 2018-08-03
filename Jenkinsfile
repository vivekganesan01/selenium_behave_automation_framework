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
                echo "BUILD :"
            }
        }
        stage('Execute') {
            steps {
                echo "PIPELINE : "
                sh 'python3 pipeline.py'
            }
        }
        stage('Deploy') {
            steps {
                echo "DEPLOY:"
            }
        }
    }
}