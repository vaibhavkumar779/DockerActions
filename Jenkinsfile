pipeline { 
  
    agent any 
    parameters {
        choice(name: 'Version', choices: ['0.0.1','0.1.0'], description:'')
        booleanParam(name: 'executable', default:true ,description:'')
    }
   
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
            when {
                expression{
                    params.executeTests
                }
            }
            steps {
                echo "testing Application"
                
            }
        }
        stage('Deploy') {
            steps {
                echo "deploying Application"
                echo "deploying version ${params.Version}"
            }
        }
    }

    post{
        success{
            echo "successful"
        }
    }
}
