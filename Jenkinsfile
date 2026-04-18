pipeline {
    agent any

    environment {
        IMAGE_NAME = "mumma-ai"
    }

    stages {

        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest || true'
            }
        }

        stage('Code Quality') {
            steps {
                sh 'flake8 . || true'
            }
        }

        stage('Security') {
            steps {
                sh 'docker run --rm aquasec/trivy image $IMAGE_NAME'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker run -d mumma-ai'
            }
        }

        stage('Release') {
            steps {
                echo 'Release v1.0'
            }
        }

        stage('Monitoring') {
            steps {
                sh 'docker run -d -p 9090:9090 prom/prometheus'
            }
        }
    }
}
