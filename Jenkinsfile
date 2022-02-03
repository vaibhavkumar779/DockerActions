pipeline { 
  
    agent any 
  
    options {
        skipStagesAfterUnstable()
    }
   
    stages {
        stage('Build') { 
            steps { 
                echo "Building Application"
                 
            }
        }
        stage('Test'){
            steps {
                echo "testing Application"
                
            }
        }
        stage('Deploy') {
            steps {
                echo "deploying Application"
               
            }
        }
    }
}
