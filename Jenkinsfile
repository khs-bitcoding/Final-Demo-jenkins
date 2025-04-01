pipeline {
    agent any
    
    environment {
        DEPLOY_SERVER = "${USER}@${GCP_DEPLOY_SERVER_IP}"
        DEPLOY_DIR = "${DEPLOY_DIR}"
        SSH_KEY = "${SSH_KEY}"
        BRANCH = "${env.BRANCH_NAME}" 
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: "${BRANCH}", url: 'https://github.com/khs-bitcoding/Final-Demo-jenkins.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Python Code Execution') {
            when {
                branch 'dev'
            }
            steps {
                echo "Deploying to Dev..."
                sh '. venv/bin/activate && python3 main.py'
            }
        }

        stage('Run Tests') {
            when {
                branch 'qa'
            }
            steps {
                echo "Deploying to QA..."
                sh '. venv/bin/activate && pytest tests --junitxml=report.xml'
            }
        }

        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                echo "Deploying to: ${DEPLOY_SERVER}"
                echo "Deploying to: ${DEPLOY_DIR}"
                echo "Deploying to: ${SSH_KEY}"

                echo "Deploying to Production..."
            }
        }
    }
}
