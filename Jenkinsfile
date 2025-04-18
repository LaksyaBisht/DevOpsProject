pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/LaksyaBisht/DevOpsProject.git'
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
                    sh 'docker rm -f temp-converter || true'
                    sh 'docker run -d -p 5000:5000 --name temp-converter temp-converter'
                }
            }
        }
    }
}
