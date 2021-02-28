pipeline {
    agent any 
    stages{

        stage('Test'){
            steps{
                sh '''
                cd ./service-1
                pip3 install -r requirements.txt
                pytest --cov=app --cov-report=term-missing
                cd ..

                # test service-2
                cd ./service-2
                pytest --cov=app --cov-report=term-missing
                cd ..

                # test service-3
                cd ./service-3
                pytest --cov=app --cov-report=term-missing
                cd ..

                # test service-4
                cd ./service-4
                pytest --cov=app --cov-report=term-missing
                cd ..
                '''
            }
        }
        stage('Build'){
            steps{
                sh ''' sudo chmod 666 /var/run/docker.sock

                docker-compose down --rmi all
                docker-compose build
                sudo docker login -u bmustafa97 -p password17
                sudo docker-compose push
                '''
            }
        }
        stage("Ansible"){
            steps{
                sh '''
                    cd ansible
                    pwd
                    ansible-playbook -i inventory.yaml playbook.yaml
                    '''     
            }
        }
        stage('Deploy'){
            steps{
                sh '''
                pwd
                cd ~ && cd /
                pwd
                cd /home/jenkins
                pwd
                ls -la
                cd .docker
                pwd
                sudo chmod 777 config.json 
                scp -i ~/.ssh/id_rsa /home/jenkins/.jenkins/workspace/projectpipeline/docker-compose.yaml jenkins@35.197.65.166:docker-compose.yaml
                ssh -i ~/.ssh/id_rsa jenkins@35.197.65.166 << EOF
                export SEC_KEY=${SEC_KEY} 
                export DB_URI=${DB_URI} 
                docker stack deploy --compose-file docker-compose.yaml restraunt-gen
                '''
            }
        }                   
    }
}
