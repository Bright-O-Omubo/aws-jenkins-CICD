pipeline {
    agent any 
    environment {
        version= "web-version:${BUILD_NUMBER}"
    }
    stages {
        
       
        stage ("Build") {
            steps{
                script {
                    sh "docker build -t ${version} ."
                }
            }
        }
        stage ("ECR push") {
            steps {
                script {
                    sh "aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 153099270414.dkr.ecr.us-east-1.amazonaws.com"
                    sh "docker tag web-version:2.0 153099270414.dkr.ecr.us-east-1.amazonaws.com/${version}"
                    sh "docker push 153099270414.dkr.ecr.us-east-1.amazonaws.com/${version}"

                }

            }
        }
        stage ("Deploy") {
            steps {
                script {
                    sh "aws --version"
                    sh "docker pull 153099270414.dkr.ecr.us-east-1.amazonaws.com/${version}"
                    sh "docker run -d -p 8081:5000 153099270414.dkr.ecr.us-east-1.amazonaws.com/${version}"
                }
            }
        }
    }

}