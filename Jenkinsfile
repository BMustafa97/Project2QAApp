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
                    chmod 666 inventory.yaml playbook.yaml
                    ls -la
                    ansible-playbook -i inventory.yaml playbook.yaml
                    '''     
            }
        }
        stage('Deploy'){
            steps{
                sh '''
                    ssh -i ~/.ssh/jenkins_agent_key manager << EOF
                    sudo rm -rf Project2QAApp
                    git clone https://github.com/BMustafa97/Project2QAApp
                    cd Project2QAApp
                    docker stack rm restaurant-gen
                    docker stack deploy --compose-file docker-compose.yaml restaurant-gen
                    EOF
                '''
            }
        }                   
    }
}
