pipeline {
    agent none
    parameters {
		choice(name: 'TEST_ENV', choices: 'dev\nuat\nstaging\nprod', description: 'Testing environment:')
		choice(name: 'TAGS', choices: 'prod\nreg\nsanity\nuat\ndev\nunittest\none', description: 'Tags to be executed:')
    }
    stages {
        stage('Execute') {
            steps {
                sh 'python ./pipeline.py'
            }
        }
    }
}