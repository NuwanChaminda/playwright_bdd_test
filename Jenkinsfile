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
                bat 'python -m venv env2'
                bat 'env2\\Scripts\\python -m pip install --upgrade pip'
                bat 'env2\\Scripts\\python -m pip install -r requirements.txt'
                bat 'env2\\Scripts\\python -m playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'env2\\Scripts\\python -m pytest features/steps/test_related_products_steps.py::test_tc025_validate_related_products_rule_25 --alluredir=allure-results'
            }
        }

    }

    post {
        always {
            allure includeProperties: false,
            jdk: '',
            results: [[path: 'allure-results']]
        }
    }
}