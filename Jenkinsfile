pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AnshuRegmi/flask-cicd.git'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run --rm -v $PWD:/app -w /app python:3.9-slim sh -c "pip install -r requirements.txt && python -m unittest test_app.py"'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-cicd .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                    docker rm -f flask-cicd || true
                    docker run -d -p 5000:5000 --name flask-cicd flask-cicd
                '''
            }
        }
    }
}

