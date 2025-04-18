pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/your-username/temp-converter.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t temp-converter .'
                }
            }
        }
        stage('Run Container') {
            steps {
                script {
                    // Stop and remove old container if exists
                    sh 'docker rm -f temp-converter || true'
                    sh 'docker run -d -p 5000:5000 --name temp-converter temp-converter'
                }
            }
        }
    }
}
