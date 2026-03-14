pipeline {

    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/NuwanChaminda/playwright_bdd_test.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
                bat 'python -m playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }

    }
}