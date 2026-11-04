pipeline {
    agent any 

    stages {
        
       
        stage ("Build") {
            steps{
                script {
                    sh "docker build -t web-version:2.0 ."
                }
            }
        }
        stage ("ECR push") {
            steps {
                script {
                    sh "aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 153099270414.dkr.ecr.us-east-1.amazonaws.com"
                    sh "docker tag web-version:2.0 153099270414.dkr.ecr.us-east-1.amazonaws.com/web-version:2.0"
                    sh "docker push 153099270414.dkr.ecr.us-east-1.amazonaws.com/web-version:2.0"

                }

            }
        }
        stage ("Deploy") {
            steps {
                script {
                    sh "aws --version"
                    sh "docker pull 153099270414.dkr.ecr.us-east-1.amazonaws.com/web-version:2.0"
                    sh "docker run -d -p 8080:5000 153099270414.dkr.ecr.us-east-1.amazonaws.com/web-version:2.0"
                }
            }
        }
    }

}