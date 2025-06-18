pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/AnshuRegmi/flask-cicd.git', branch: 'main'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m unittest test_app.py'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-flask-app .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 my-flask-app'
            }
        }
    }
}

