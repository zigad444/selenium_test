pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/zigad444/selenium_test.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Test') {
            steps {
                sh './venv/bin/python test_login.py'
            }
        }
    }
}
