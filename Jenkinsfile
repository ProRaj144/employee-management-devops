pipeline {

    agent any

    environment {

        APP_DIR = "/opt/production-app"

        AWS_REGION = "us-east-1"

        AWS_ACCOUNT_ID = "345857776164"

        BACKEND_REPO = "345857776164.dkr.ecr.us-east-1.amazonaws.com/employee-backend"

        FRONTEND_REPO = "345857776164.dkr.ecr.us-east-1.amazonaws.com/employee-frontend"

        IMAGE_TAG = "${BUILD_NUMBER}"

    }

    stages {

        stage('Checkout Source') {
            steps {
                checkout scm
            }
        }

        stage('Update Source') {

            steps {

                sh '''
                echo "========================================"
                echo "Updating Source Code"
                echo "========================================"

                cd $APP_DIR

                git config --global --add safe.directory $APP_DIR

                git fetch origin

                git reset --hard origin/main
                '''

            }

        }

        stage('Code Quality') {

            steps {

                sh '''
                echo "========================================"
                echo "Running Flake8"
                echo "========================================"

                cd $APP_DIR/backend

                docker build -t employee-backend:test .

                docker run --rm employee-backend:test flake8 app

                echo "Flake8 Completed Successfully"
                '''

            }

        }

        stage('Backend Tests') {

            steps {

                sh '''
                echo "========================================"
                echo "Running Backend Tests"
                echo "========================================"

                cd $APP_DIR/backend

                mkdir -p $APP_DIR/reports

                docker build -t employee-backend:test .

                docker run --rm \
                -e PYTHONPATH=/app \
                employee-backend:test \
                python -m pytest tests \
                --junitxml=/app/tests-report.xml

                docker cp $(docker create employee-backend:test):/app/tests-report.xml $APP_DIR/reports/backend-test-report.xml || true

                echo "Backend Tests Completed Successfully"
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
                echo "========================================"
                echo "Building Backend Docker Image"
                echo "========================================"

                cd $APP_DIR/backend

                docker build \
                -t $BACKEND_REPO:$IMAGE_TAG \
                -t $BACKEND_REPO:latest .
                '''

            }

        }

        stage('Build Frontend Image') {

            steps {

                sh '''
                echo "========================================"
                echo "Building Frontend Docker Image"
                echo "========================================"

                cd $APP_DIR/frontend

                docker build \
                -t $FRONTEND_REPO:$IMAGE_TAG \
                -t $FRONTEND_REPO:latest .
                '''

            }

        }

        stage('Push Images to Amazon ECR') {

            steps {

                sh '''
                echo "========================================"
                echo "Logging into Amazon ECR"
                echo "========================================"

                aws ecr get-login-password --region $AWS_REGION | docker login \
                --username AWS \
                --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com

                echo "Pushing Backend Image..."

                docker push $BACKEND_REPO:$IMAGE_TAG

                docker push $BACKEND_REPO:latest

                echo "Pushing Frontend Image..."

                docker push $FRONTEND_REPO:$IMAGE_TAG

                docker push $FRONTEND_REPO:latest
                '''

            }

        }

        stage('Deploy Development') {

            steps {

                sh '''
                echo "========================================"
                echo "Deploying Application"
                echo "========================================"

                cd $APP_DIR

                docker compose -f docker-compose.dev.yml pull

                docker compose -f docker-compose.dev.yml up -d
                '''

            }

        }

        stage('Health Check') {

            steps {

                sh '''
                echo "========================================"
                echo "Checking Backend Health"
                echo "========================================"

                sleep 20

                curl --retry 5 \
                     --retry-delay 5 \
                     --retry-connrefused \
                     --fail \
                     http://localhost:8000/health

                echo "Application is Healthy"
                '''

            }

        }

        stage('Manual Approval') {

            steps {

                timeout(time: 15, unit: 'MINUTES') {

                    input(
                        message: 'Deploy to Production?',
                        ok: 'Deploy'
                    )

                }

            }

        }

        stage('Deploy Production') {

            steps {

                sh '''
                echo "========================================"
                echo "Production Deployment"
                echo "========================================"

                cd $APP_DIR

                docker compose -f docker-compose.dev.yml pull

                docker compose -f docker-compose.dev.yml up -d

                echo "Production Deployment Successful"
                '''

            }

        }

    }

    post {

        success {

            emailext(

                subject: "SUCCESS : ${env.JOB_NAME} #${env.BUILD_NUMBER}",

                body: """

Hello,

The Employee Management CI/CD Pipeline completed successfully.

Job Name : ${env.JOB_NAME}

Build Number : ${env.BUILD_NUMBER}

Status : SUCCESS

Stages Completed

✔ Checkout

✔ Code Quality

✔ Backend Tests

✔ Docker Build

✔ Amazon ECR Push

✔ Development Deployment

✔ Health Check

✔ Production Deployment

Regards,

Jenkins

""",

                to: "YOUR_GMAIL@gmail.com"

            )

        }

        failure {

            echo "Deployment Failed"

            echo "Rollback can be added here."

            emailext(

                subject: "FAILED : ${env.JOB_NAME} #${env.BUILD_NUMBER}",

                body: """

Hello,

The Employee Management CI/CD Pipeline has failed.

Job Name : ${env.JOB_NAME}

Build Number : ${env.BUILD_NUMBER}

Please check the Jenkins Console Output.

Regards,

Jenkins

""",

                to: "YOUR_GMAIL@gmail.com"

            )

        }

        always {

            archiveArtifacts artifacts: 'reports/**/*', allowEmptyArchive: true

            junit allowEmptyResults: true, testResults: 'reports/**/*.xml'

            sh '''
            docker ps

            docker images | head -20
            '''

        }

    }

}
