pipeline {
  agent any

  // Same behavior as the tutorial: poll Git every ~2 minutes
  triggers { pollSCM('H/2 * * * *') }

  // Make sure Homebrew paths are visible inside Jenkins shells
  environment {
    // include both common Homebrew prefixes
    PATH = "/opt/homebrew/bin:/usr/local/bin:${env.PATH}"
    IMAGE_NAME = "videostore:latest"
    DEPLOYMENT = "videostore-deployment"
    SERVICE    = "videostore-service"
  }

  options {
    timestamps()
    ansiColor('xterm')
  }

  stages {

    // If your job is "Pipeline script from SCM", Jenkins already checks out,
    // but we keep this for clarity and logs.
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Env check') {
      steps {
        sh '''
          echo "PATH=$PATH"
          which docker || true
          which minikube || true
          which kubectl || true
          docker --version || true
          minikube version || true
          kubectl version --client || true
        '''
      }
    }

    stage('Ensure Minikube up') {
      steps {
        sh '''
          # Start Minikube if not running (idempotent)
          minikube status || minikube start --driver=docker
          # Point Docker to Minikube's Docker daemon (very important)
          eval $(minikube docker-env)
          docker info >/dev/null 2>&1 || { echo "Docker not reachable"; exit 1; }
        '''
      }
    }

    stage('Build in Minikube Docker') {
      steps {
        sh '''
          eval $(minikube docker-env)
          docker build -t ${IMAGE_NAME} .
          docker images | grep videostore || { echo "Image not built"; exit 1; }
        '''
      }
    }

    stage('Deploy to Minikube') {
      steps {
        sh '''
          # Apply k8s manifests (same structure as the tutorial, renamed for videostore)
          kubectl apply -f deployment.yaml
          kubectl apply -f service.yaml

          # Wait for rollout to complete
          kubectl rollout status deployment/${DEPLOYMENT} --timeout=120s

          echo "Pods:"
          kubectl get pods -l app=videostore-app -o wide
        '''
      }
    }

    stage('Expose URL') {
      steps {
        sh '''
          # Print the service URL so it's easy to click in the logs
          URL=$(minikube service ${SERVICE} --url)
          echo "Video Store is available at: $URL"
        '''
      }
    }
  }

  post {
    failure {
      echo "Build failed. Check earlier stages for PATH/minikube/docker issues."
    }
    success {
      echo "✅ Deployed ${IMAGE_NAME} to Minikube and exposed via NodePort."
    }
  }
}
