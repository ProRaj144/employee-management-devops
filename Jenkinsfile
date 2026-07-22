pipeline {
    agent any

    environment {
        APP_DIR="/opt/production-app"
        AWS_REGION="us-east-1"
        AWS_ACCOUNT_ID="345857776164"
        BACKEND_REPO="345857776164.dkr.ecr.us-east-1.amazonaws.com/employee-backend"
        FRONTEND_REPO="345857776164.dkr.ecr.us-east-1.amazonaws.com/employee-frontend"
        IMAGE_TAG="${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout SCM') {
            steps { checkout scm }
        }

        stage('Prepare Workspace') {

    steps {

        sh '''

        echo "========================================"

        echo "Preparing Workspace"

        echo "========================================"

        pwd

        ls -la

        '''

    }

}

        stage('Code Quality') {
            steps {
                sh """
                cd backend
                docker build -t employee-backend:test .
                docker run --rm employee-backend:test flake8 app
                """
            }
        }
       	stage('Backend Tests') {
    	    steps {
	        sh '''
        	mkdir -p "$WORKSPACE/reports"

	        cd backend

	        docker build -t employee-backend:test .

        	docker rm -f backend-test-report >/dev/null 2>&1 || true

	        docker run \
        	  --name backend-test-report \
	          -e PYTHONPATH=/app \
        	  employee-backend:test \
	          python -m pytest tests \
        	  --junitxml=/app/backend-test-report.xml

	        docker cp \
        	  backend-test-report:/app/backend-test-report.xml \
	          "$WORKSPACE/reports/backend-test-report.xml"

        	docker rm backend-test-report
	        '''
	       }
	    }
        stage('Verify Docker') {
            steps {
                sh "docker --version && docker compose version"
            }
        }

        stage('Build Backend') {
            steps {
                sh "cd backend && docker build -t $BACKEND_REPO:$IMAGE_TAG -t $BACKEND_REPO:latest ."
            }
        }

        stage('Build Frontend') {
            steps {
                sh "cd frontend && docker build -t $FRONTEND_REPO:$IMAGE_TAG -t $FRONTEND_REPO:latest ."
            }
        }

        stage('Push Images') {
            steps {
                sh "aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com && docker push $BACKEND_REPO:$IMAGE_TAG && docker push $BACKEND_REPO:latest && docker push $FRONTEND_REPO:$IMAGE_TAG && docker push $FRONTEND_REPO:latest"
            }
        }

       stage('Deploy Development') {
	    steps {
        	sh '''

	        echo "====================================="
	        echo "Deploying Development"
        	echo "====================================="

	        docker compose -f docker-compose.dev.yml down || true
	
        	docker rm -f employee-backend employee-frontend >/dev/null 2>&1 || true

	        docker compose -f docker-compose.dev.yml pull

	        docker compose -f docker-compose.dev.yml up -d --remove-orphans

	        '''	
	    }
	}

        stage('Health Check') {
	    steps {
	        sh '''
	        mkdir -p reports

	        echo "======================================"
	        echo "Checking Application Health"
	        echo "======================================"

	        sleep 20

	        curl --retry 5 \
	             --retry-delay 5 \
	             --retry-connrefused \
	             --fail \
	             http://localhost:8000/health \
	             | tee reports/health-report.json

        	echo "Application is Healthy"
	        '''
	    }
	}

        stage('Manual Approval') {
            steps {
                timeout(time:15, unit:'MINUTES') {
                    input message:'Deploy to Production?', ok:'Deploy'
                }
            }
        }

        stage('Deploy Production') {
            steps {
                sh '''
		
		echo "======================================"
		
		echo "Deploying to production"

		echo "======================================"

		docker compose -f docker-compose.dev.yml pull

		docker compose -f docker-compose.dev.yml up -d

		'''
            }
        }
     } 
    
    post {
        success {
            emailext(to:"sajja.sujith44@gmail.com", subject:"SUCCESS: ${JOB_NAME} #${BUILD_NUMBER}", body:"Deployment completed successfully.")
        }

        failure {
            emailext(to:"sajja.sujith44@gmail.com", subject:"FAILED: ${JOB_NAME} #${BUILD_NUMBER}", body:"Pipeline failed. Check Jenkins console.")
        }

        always {
            archiveArtifacts artifacts:'reports/**/*', fingerprint: true

            junit allowEmptyResults:true,
		  testResults:'reports/backend-test-report.xml'
        }
    }
}

