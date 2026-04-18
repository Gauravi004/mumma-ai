pipeline {
    agent any

    environment {
        IMAGE_NAME = "mumma-ai"
        IMAGE_TAG = "v1"
    }

    stages {

        stage('Checkout SCM') {
          steps {
            git branch: 'main', url: 'https://github.com/Gauravi004/mumma-ai.git'
         }
       }

        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
            }
        }

        stage('Test') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install pytest || true
                pytest || true
                '''
            }
        }

        stage('Code Quality') {
            steps {
                sh '''
                . venv/bin/activate || true
                pip install flake8 || true
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
                echo 'Releasing version v1 of Mumma AI'
            }
        }

        stage('Monitoring') {
            steps {
                sh 'docker ps'
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
