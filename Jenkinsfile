pipeline {
  agent any
  triggers { pollSCM('H/2 * * * *') }   // same as tutorial

  environment {
    PATH = "/opt/homebrew/bin:/usr/local/bin:${env.PATH}"
    IMAGE_NAME = "videostore:latest"
  }

  stages {
    stage('Checkout') {
      steps {
        // OK to keep even when job is "Pipeline script from SCM" — it re-logs the checkout
        git branch: 'main', url: 'https://github.com/eligeabiantoun/videostore-assignment.git'
      }
    }

    stage('Build in Minikube Docker') {
      steps {
        sh '''
          eval $(minikube docker-env)
          docker build -t ${IMAGE_NAME} .
        '''
      }
    }

    stage('Deploy to Minikube') {
      steps {
        sh '''
          kubectl apply -f deployment.yaml
          kubectl apply -f service.yaml
          kubectl rollout status deployment/videostore-deployment --timeout=120s
        '''
      }
    }

    stage('Expose URL') {
      steps {
        sh 'minikube service videostore-service --url'
      }
    }
  }
}
