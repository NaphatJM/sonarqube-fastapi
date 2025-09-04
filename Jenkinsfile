pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        SONARQUBE = credentials('sonarqube-token')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/NaphatJM/sonarqube-fastapi.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install --user --upgrade pip'
                sh 'pip install --user -r requirements.txt'
            }
        }

        stage('Run Tests & Coverage') {
            steps {
                sh 'pytest --cov=app --cov-report=xml test/'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh 'sonar-scanner'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t fastapi-app:latest .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh 'docker run -d -p 8000:8000 --name fastapi-app fastapi-app:latest'
            }
        }
    }

    post {
        always {
            echo "Pipeline finished"
        }
    }
}
