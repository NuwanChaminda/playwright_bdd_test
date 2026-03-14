pipeline {

    agent any

    triggers {
        cron('0 4 * * *')
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/NuwanChaminda/playwright_bdd_test.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate'
                bat 'python -m pip install -r requirements.txt'
                bat 'python -m playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\activate && pytest -n 4 --alluredir=allure-results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false, results: [[path: 'allure-results']]
            }
        }

    }

    post {

        always {
            archiveArtifacts artifacts: 'allure-results/**'
        }

        failure {
            mail to: 'nuwanwusl@gmail.com',
                 subject: "Automation Failed",
                 body: "Jenkins automation run failed"
        }

    }

}