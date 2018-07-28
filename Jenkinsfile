pipeline {
    agent {
       docker {
			image 'python:3.7.0-stretch'
		}
    }
    parameters {
		choice(name: 'TEST_ENV', choices: 'dev\nuat\nstaging\nprod', description: 'Testing environment:')
		choice(name: 'TAGS', choices: 'prod\nreg\nsanity\nuat\ndev\nunittest\none', description: 'Tags to be executed:')
    }
    stages {
        stage('Build') {
            steps {
                echo "BUILD : "
                sh 'python --version'
                sh 'pip install r requirements.txt'
            }
        }
        stage('Execute') {
            steps {
                echo "PIPELINE : "
                sh 'python ./pipe.py'
            }
        }
        stage('Deploy') {
            steps {
                echo "DEPLOY : "
            }
        }
    }
}