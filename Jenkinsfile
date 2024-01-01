pipeline {
    agent {
        docker {
            image 'python:3.9-slim-buster'
        }
    }
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd src && pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd src
                python3 -m unittest discover tests
                '''
            }
        }
        stage('Prod') {
            steps {
                echo 'Production....'
                sh '''
                echo "doing prod stuff.."
                '''
            }
        }
    }
}