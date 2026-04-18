pipeline {
    agent any

    environment {
        IMAGE_NAME = "mumma-ai"
        IMAGE_TAG = "v${BUILD_NUMBER}"
    }

    stages {

     stage('Setup') {
         steps {
        sh '''
        echo "Installing dependencies..."

        pip3 install --upgrade pip --break-system-packages || true
        pip3 install pytest flake8 requests google-generativeai --break-system-packages || true
        '''
      }
  }

        stage('Build') {
            steps {
                sh '''
                echo "Building Docker image..."
                docker build -t $IMAGE_NAME:$IMAGE_TAG .
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                echo "Running tests..."
                pytest || true
                '''
            }
        }

        stage('Code Quality') {
            steps {
                sh '''
                echo "Checking code quality..."
                flake8 . || true
                '''
            }
        }

        stage('Security') {
            steps {
                sh '''
                echo "Running security scan..."
                docker run --rm aquasec/trivy fs . || true
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                echo "Deploying container..."
                docker rm -f mumma-container || true
                docker run -d --name mumma-container -p 5001:5000 $IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }

        stage('Release') {
            steps {
                sh '''
                echo "Releasing version $IMAGE_TAG"
                echo $IMAGE_TAG > release.txt
                '''
            }
        }

        stage('Monitoring') {
            steps {
                sh '''
                echo "Running Containers:"
                docker ps

                echo "Container Logs:"
                docker logs mumma-container || true
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully 🚀'
        }
        failure {
            echo 'Pipeline failed ❌'
        }
    }
}
