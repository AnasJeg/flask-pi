pipeline {
    agent { 
        node {
            label 'py-pipline'
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
                cd src
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd src
                python3 app.py
                python3 app.py --name=Brad
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