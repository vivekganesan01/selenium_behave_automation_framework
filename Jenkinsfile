pipeline {
    agent {
        label 'Test run'
    }
    parameters {
		choice(name: 'TEST_ENV', choices: 'dev\nuat\nstaging\nprod', description: 'Testing environment:')
		choice(name: 'TAGS', choices: 'prod\nreg\nsanity\nuat\ndev\nunittest\none', description: 'Tags to be executed:')
		type(name: 'FEATURE')
    }
    stages {
        stage('Build') {
            steps {
                echo "BUILD"
            }
        }
        stage('Test') {
            steps {
                echo "TEST"
            }
        }
        stage('Deploy') {
            steps {
                echo "DEPLOY"
            }
        }
    }
}