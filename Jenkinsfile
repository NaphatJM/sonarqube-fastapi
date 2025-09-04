pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root -v /var/run/docker.sock:/var/run/docker.sock'
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

        stage('Install Java') {
            steps {
                sh '''
                    apt-get update -qq
                    apt-get install -y wget gnupg lsb-release
                    wget -O - https://packages.adoptium.net/artifactory/api/gpg/key/public | apt-key add -
                    echo "deb https://packages.adoptium.net/artifactory/deb $(lsb_release -sc) main" > /etc/apt/sources.list.d/adoptium.list
                    apt-get update -qq
                    apt-get install -y temurin-17-jdk
                    java -version
                '''
            }
        }
        stage('Setup Virtualenv & Install Dependencies') {
            steps {
                sh '''
                  python -m venv venv
                  . venv/bin/activate
                  pip install --upgrade pip
                  pip install -r requirements.txt
                '''
            }
        }
        

        stage('Run Tests & Coverage') {
            steps {
                sh '''
                  . venv/bin/activate
                  pytest --cov=app --cov-report=xml test/
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh "${tool 'sonarqube-scanner'}/bin/sonar-scanner"
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
                sh '''
                  docker rm -f fastapi-app || true
                  docker run -d --restart unless-stopped -p 8000:8000 --name fastapi-app fastapi-app:latest
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline finished"
        }
    }
}
