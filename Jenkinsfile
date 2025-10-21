pipeline {
  agent any
  stages {
    stage('Env check') {
      steps {
        sh '''
          echo "PATH=$PATH"
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
Once
