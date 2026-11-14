pipeline {
    agent any 
    environment {
        version= "web-version:${BUILD_NUMBER}"
        URL="http://32.200.160.110:8081/health"
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
                withCredentials ([
                    usernamePassword (
                        credentialsId: 'jenkins-awsEcr',
                        usernameVariable: 'AWS',
                        passwordVariable: 'SECRET'
                    )
                ])
                script {
                     sshagent(['aws-JKey']) {
                        sh "ssh ubuntu@32.200.160.110"
                        sh "aws sts get-caller-identity"
                        sh "aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 153099270414.dkr.ecr.us-east-1.amazonaws.com"
                        sh "docker tag ${version} 153099270414.dkr.ecr.us-east-1.amazonaws.com/${version}"
                        sh "docker push 153099270414.dkr.ecr.us-east-1.amazonaws.com/${version}"
                    }
                }
            }
        }
        stage ("Deploy") {
            steps {
                script {
                    sshagentz(['aws-JKey']) {
                        sh "aws --version"
                        sh "docker pull 153099270414.dkr.ecr.us-east-1.amazonaws.com/${version}"
                        sh "docker rm -f nervous_robinson || true"
                        sh "docker run -d -p 8081:5000 153099270414.dkr.ecr.us-east-1.amazonaws.com/${version}"
                    }
                }
            }
        }
    }
}