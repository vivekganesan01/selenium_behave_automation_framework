pipeline {
    agent {
       docker {
			image 'vivekjarvis/py_selenese:slim'
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
                sh 'python3 pipe.py'
            }
        }
        stage('Deploy') {
            steps {
                echo "DEPLOY:"
            }
        }
    }
}