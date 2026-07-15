pipeline {
    agent any

    environment {
        APP_DIR = "/opt/production-app"
    }

    stages {

        stage('Update Source') {
            steps {
                sh '''
                cd $APP_DIR
                git config --global --add safe.directory $APP_DIR
                git fetch origin
                git reset --hard origin/main
                '''
            }
        }

        stage('Build Backend') {
            steps {
                sh '''
                cd $APP_DIR/backend
                docker build -t employee-backend:v4 .
                '''
            }
        }

        stage('Build Frontend') {
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
                sh '''
                curl http://localhost:8000/health
                '''
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
