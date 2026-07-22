pipeline {
    agent any

    environment {
        APP_DIR = "/opt/production-app"
    }

    stages {

        stage('Update Source') {
            steps {
                sh '''
                echo "Updating source code..."

                cd $APP_DIR

                git config --global --add safe.directory $APP_DIR

                git fetch origin

                git reset --hard origin/main
                '''
            }
        }

        stage('Verify Docker') {
            steps {
                sh '''
                docker --version
                docker compose version
                '''
            }
        }

        stage('Build Backend Image') {
            steps {
                sh '''
                echo "Building Backend Image..."

                cd $APP_DIR/backend

                docker build -t employee-backend:v4 .
                '''
            }
        }

        stage('Build Frontend Image') {
            steps {
                sh '''
                echo "Building Frontend Image..."

                cd $APP_DIR/frontend

                docker build -t employee-frontend:v1 .
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                echo "Deploying Application..."

                cd $APP_DIR

                docker compose up -d
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                echo "Waiting for backend to become healthy..."

                sleep 15

                curl --retry 5 \
                     --retry-delay 5 \
                     --retry-connrefused \
                     --fail \
                     http://localhost:8000/health

                echo "Backend is Healthy."
                '''
            }
        }
    }

    post {

        success {
            echo "========================================"
            echo "Deployment Successful!"
            echo "Employee Management System is Live."
            echo "========================================"
        }

        failure {
            echo "========================================"
            echo "Deployment Failed!"
            echo "Check Console Output for Errors."
            echo "========================================"
        }

        always {
            sh 'docker ps'
        }
    }
}
