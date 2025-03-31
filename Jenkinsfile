pipeline {
    agent any
    
    environment {
        DEPLOY_SERVER = "user@GCP_DEPLOY_SERVER_IP"
        DEPLOY_DIR = "/home/user/myapp"
        SSH_KEY = "/home/jenkins/.ssh/jenkins_gcp"
        BRANCH = "${params.BRANCH_NAME}"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: "${BRANCH_NAME}", url: ''
            }
        }
        
        stage('Setup Python') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            when {
                branch 'dev'
            }
            steps {
                sh '. venv/bin/activate && pytest tests --junitxml=report.xml'
            }
        }

        stage('Deploy to QA') {
            when {
                branch 'qa'
            }
            steps {
                echo "Deploying to QA..."
            }
        }

        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                echo "Deploying to Production..."
            }
        }
    }
}
