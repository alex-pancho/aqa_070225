pipeline {
    agent any


    environment {
        VENV_PATH = "${WORKSPACE}/venv"
    }


    stages {
        stage('Clone repo') {
            steps {
                git branch: 'homework29', url: 'https://github.com/Julialaz/aqa_070225.git'
            }
        }


        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }


        stage('Run tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest lesson_29_homework/tests/ --junitxml=report.xml
                '''
            }
        }


        stage('Publish results') {
            steps {
                junit 'report.xml'
            }
        }
    }


    post {
        always {
            echo "🧹 Pipeline finished"
            emailext (
                subject: "Jenkins Build ${currentBuild.fullDisplayName} - ${currentBuild.currentResult}",
                body: """Build finished with status: ${currentBuild.currentResult}
                        |Check details: ${env.BUILD_URL}""".stripMargin(),
                to: 'julialazurkevych@gmail.com'
            )
        }
        success {
            echo "✅ Tests passed successfully!"
        }
        failure {
            echo "❌ Tests failed!"
        }
        unstable {
            echo "⚠️ Pipeline is unstable (some tests failed or warnings)"
        }
    }
}
