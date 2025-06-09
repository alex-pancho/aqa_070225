pipeline {
    agent any

    environment {
        MAIL_CREDENTIALS = credentials('mailtrap-credentials-id')  
    }

    stages {
        stage('Clone repo') {
            steps {
                git url: 'https://github.com/Ilonkab/aqa_070225', branch: 'homework30'
            }
        }

        stage('Install dependencies') {
            steps {
                dir('lesson_30/homework_30') {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run tests') {
            steps {
                dir('lesson_30/homework_30') {
                    sh '''
                        . venv/bin/activate
                        pytest db_tests.py --junitxml=report.xml
                    '''
                }
            }
        }

        stage('Publish test results') {
            steps {
                junit 'lesson_30/homework_30/report.xml'
            }
        }
    }

    post {
        always {
            emailext(
                subject: "Test Results: ${currentBuild.fullDisplayName}",
                body: """
                Build result: ${currentBuild.currentResult}
                Job: ${env.JOB_NAME}
                Build: #${env.BUILD_NUMBER}
                Link: ${env.BUILD_URL}
                """,
                to: 'ilonkainbox@inbox.mailtrap.io',
                mimeType: 'text/plain',
                attachLog: true,
                smtpHost: 'sandbox.smtp.mailtrap.io',
                smtpPort: '2525',
                replyTo: 'noreply@example.com',
                from: 'jenkins@example.com',
                authUsername: "${MAIL_CREDENTIALS_USR}",
                authPassword: "${MAIL_CREDENTIALS_PSW}"
            )
        }
    }
}