pipeline {
  agent any
  triggers { pollSCM('H/2 * * * *') }
  stages {
    stage('Checkout') {
      steps { git branch: 'main', url: 'https://github.com/eligeabiantoun/videostore-assignment' }
    }
    stage('Env check') {
      steps { sh '''
        echo "PATH=$PATH"
        which docker || true
        which minikube || true
        which kubectl || true
        docker --version || true
        minikube version || true
        kubectl version --client || true
      ''' }
    }
    stage('Build in Minikube Docker') {
      steps { sh '''
        eval $(minikube docker-env)
        docker build -t videostore:latest .
      ''' }
    }
    stage('Deploy to Minikube') {
      steps { sh '''
        kubectl apply -f deployment.yaml
        kubectl rollout status deployment/videostore-deployment
      ''' }
    }
  }
}
