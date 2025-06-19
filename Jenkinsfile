pipeline {
    agent any

    stages {
        stage('Clone source') {
            steps {
                git url: 'https://github.com/lydmy/aqa_070225', branch: 'homework__29'
            }
        }
        stage('Build and activate venv') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest -s -v "$WORKSPACE/lesson_24/test_lesson_24.py" --junitxml=$WORKSPACE/report.xml
                '''
                junit '**/report.xml'
            }
        }
    }
    post {
        always {
            emailext (
                to: "${RECIPIENT}",
                subject: "Jenkins Pipeline: Результат тестування проекту ${currentBuild.fullDisplayName}",
                body: """
                
                ${currentBuild.currentResult}

               
                """
            )
        }
    }
}