pipeline { 
  
    agent any 
    stages {
        stage('Build') { 
            when {
                expression{
                    BRANCH_NAME == 'main'
                }
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
