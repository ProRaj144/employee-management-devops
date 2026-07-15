
pipeline {
    agent any

    environment {
        APP_DIR = "/opt/production-app"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Copy Latest Source') {
            steps {
                sh '''
                rm -rf $APP_DIR/backend
                rm -rf $APP_DIR/frontend

                cp -r backend $APP_DIR/
                cp -r frontend $APP_DIR/
                cp docker-compose.yml $APP_DIR/
                '''
            }
        }

        stage('Build Backend Image') {
            steps {
                sh '''
                cd $APP_DIR/backend
                docker build -t employee-backend:v4 .
                '''
            }
        }

        stage('Build Frontend Image') {
            steps {
                sh '''
                cd $APP_DIR/frontend
                docker build -t employee-frontend:v1 .
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                cd $APP_DIR
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
