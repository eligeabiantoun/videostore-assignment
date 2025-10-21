pipeline {
  agent any

  // Same trigger cadence as the tutorial
  triggers { pollSCM('H/2 * * * *') }

  stages {

    // Matches the tutorial's Checkout stage (Pipeline-from-SCM jobs will still log this nicely)
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/eligeabiantoun/videostore-assignment.git'
      }
    }

    // Build the image INSIDE Minikube's Docker daemon (tutorial's docker-env + build)
    stage('Build in Minikube Docker') {
      steps {
        sh '''
          # Point Docker to Minikube
          eval $(minikube docker-env)

          # Build your Video Store image
          docker build -t videostore:latest .
        '''
      }
    }

    // Apply manifests and wait for successful rollout (tutorial's kubectl apply + rollout status)
    stage('Deploy to Minikube') {
      steps {
        sh '''
          kubectl apply -f deployment.yaml
          kubectl apply -f service.yaml

          # Wait until the Deployment is rolled out
          kubectl rollout status deployment/videostore-deployment
        '''
      }
    }
  }
}
