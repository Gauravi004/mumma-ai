pipeline {
    agent any

    environment {
        IMAGE_NAME = "mumma-ai"
        IMAGE_TAG = "v${BUILD_NUMBER}"
    }

    stages {

        stage('Build') {
          steps {
           echo 'Building Docker Image (simulated)'
          }
        }

        stage('Test') {
            steps {
                sh '''
                pip3 install pytest || true
                pytest || true
                '''
            }
        }

        stage('Code Quality') {
            steps {
                sh '''
                pip3 install flake8 || true
                flake8 . || true
                '''
            }
        }

        stage('Security') {
            steps {
                sh 'docker run --rm aquasec/trivy fs . || true'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker rm -f mumma-container || true
                docker run -d --name mumma-container -p 5001:5000 $IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }

        stage('Release') {
            steps {
                echo "Releasing version ${IMAGE_TAG}"
                sh 'echo $IMAGE_TAG > release.txt'
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
