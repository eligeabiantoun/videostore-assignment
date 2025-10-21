pipeline {
  agent any
  stages {
    stage('Smoke') {
      steps {
        sh 'echo OK from Jenkins; whoami; which bash || true'
      }
    }
  }
}
