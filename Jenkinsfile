pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    bat 'docker build -t temp-converter .'
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Use double quotes for Windows cmd
                    bat 'docker rm -f temp-converter || exit 0'
                    bat 'docker run -d -p 5000:5000 --name temp-converter temp-converter'
                }
            }
        }
    }
}
