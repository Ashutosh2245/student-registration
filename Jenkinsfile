pipeline {

    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building Student Registration Project...'
                bat 'dir'
            }
        }

        stage('Test') {
            steps {
                bat 'python test.py'
            }
        }
    }

    post {

        success {
            echo 'Build and tests passed!'
        }

        failure {
            echo 'Build or tests failed!'
        }
    }
}