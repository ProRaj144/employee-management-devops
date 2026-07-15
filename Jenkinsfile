pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Docker') {
            steps {
                sh 'docker --version'
                sh 'docker compose version'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                cd /opt/production-app
                docker compose up -d
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh 'curl http://localhost:8000/health'
            }
        }
    }

    post {
        success {
            echo 'Deployment Successful!'
        }

        failure {
            echo 'Deployment Failed!'
        }
    }
}
