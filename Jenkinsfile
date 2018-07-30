pipeline {
    agent {
       docker {
			image 'ubuntu:16.04'
		}
    }
    parameters {
		choice(name: 'TEST_ENV', choices: 'dev\nuat\nstaging\nprod', description: 'Testing environment:')
		choice(name: 'TAGS', choices: 'prod\nreg\nsanity\nuat\ndev\nunittest\none', description: 'Tags to be executed:')
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
            }
        }
        stage('Deploy') {
            steps {
                echo "DEPLOY:"
            }
        }
    }
}