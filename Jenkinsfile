pipeline {
  agent any
  environment {
    PATH = "/opt/homebrew/bin:/usr/local/bin:${env.PATH}"   // arm64 first, then Intel
  }
  stages {
    stage('Env check') {
      steps {
        sh '''
          echo PATH=$PATH
          which git || true
          which docker || true
          which minikube || true
          which kubectl || true
          git --version || true
          docker --version || true
          minikube version || true
          kubectl version --client || true
        '''
      }
    }
  }
}
