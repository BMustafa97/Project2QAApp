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
                    scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@manager:/home/jenkins/docker-compose.yaml
                    ssh -i ~/.ssh/id_rsa jenkins@manager
                    docker stack deploy --compose-file /home/jenkins/docker-compose.yaml restaurant-gen
                    '''
            }
        }                   
    }
}
