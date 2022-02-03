pipeline { 
  
    agent any 
  
    options {
        skipStagesAfterUnstable()
    }
   
    stages {
        stage('Build') { 
            steps { 
                echo "Building Application"
                sh 'make' 
            }
        }
        stage('Test'){
            steps {
                echo "testing Application"
                sh 'make check'
                junit 'reports/**/*.xml' 
            }
        }
        stage('Deploy') {
            steps {
                echo "deploying Application"
                sh 'make publish'
            }
        }
    }
}
