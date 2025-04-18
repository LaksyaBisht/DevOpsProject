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
                    // Stop and remove the container if it exists
                    bat 'docker ps -q -f name=temp-converter | xargs -r docker rm -f'
                    // Run the container
                    bat 'docker run -d -p 5000:5000 --name temp-converter temp-converter'
                    
                    // View logs (optional, for debugging)
                    bat 'docker logs temp-converter'
                }
            }
        }
    }
}
