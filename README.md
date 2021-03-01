---


---

<p>**</p>
<h2 id="project-brief">Project Brief</h2>
<p>The brief set for this project is to create a service-orientated architecture for my application, with the tools, methodologies and technologies that cover all core modules covered during training. The application must be composed of at least four services that work together.</p>
<h3 id="requirements">Requirements</h3>
<p>In order to achieve the brief, the following requirements must be achieved:</p>
<ul>
<li>Trello board</li>
<li>Relational database - with one table.</li>
<li>Clear documentation including design, architecture and risk assessment.</li>
<li>An application fully integrated using the feature branch model into a Version Control System (VCS). The VCS will be built through a CI server (Jenkins) and deployed to a cloud-based virtual machine.</li>
<li>When a change to the code is pushed to the VCS, webhooks must be set up for the CI server to recreate and redeploy the application.</li>
<li>The application must follow the service-orientated architecture which must be deployed using containerisation and an orchestration tool.</li>
<li>Ansible playbook must be made that will provide the environment for the application to run.</li>
<li>A reverse proxy must be set up to make the applciation accessible to the user.</li>
</ul>
<p>**</p>
<h2 id="microservice-architecture">Microservice-architecture</h2>
<p>My project consists of many moving parts, at the very base I have a total of four services which all interact with one another. Service 2 &amp; 3 would both generate a name and slogan from a pre-populated string, randomly. Service 4 would then make requests to both API’s and consolidate this new information which would then be requested by Service 1. Service 1 would then interact with the user and provide them with their desired output as well as persist data to a database so the User could access said data.<br>
Behind all of this Jenkins, Ansible, Docker Swarm/Compose and NGINX are all automating various tasks. Credit to Jenkins for being the centre point to this complex architecture.</p>
<h2 id="my-strategy">My Strategy</h2>
<p>I used an iterative method by simply creating a functional app at first with successful tests, then moving on to enable it’s dockerised capabilities through Dockerfiles and a docker-compose.yaml.  I then incorporated the use of Jenkins to build the various steps of Testing, Building and Deploying at that stage. Then I configured VM’s via Ansible and an NGINX load-balancer.</p>
<p>**</p>
<h2 id="project-management">Project Management</h2>
<p>Usage of Trello Board to constantly keep me on task and working in an organised manner.</p>
<img width="823" alt="Trello" src="https://user-images.githubusercontent.com/66776309/109551603-a9750b00-7ac8-11eb-9fdf-b2f6defb7e8a.png">
<p>My board allowed me to prioritise and understand different aspects of this project. It created a linear methodology of content creating which I really enjoyed.</p>
<h2 id="cicd-pipeline">CI/CD Pipeline</h2>
<p>Below is an overview of the technologies used in implementing this Project. From tracking progress on my Trello Board to creating content in Python through Visual Studio. Then adding, committing and pushing these changes to GitHub. Automating containerisation through Jenkins as well as configuration through Jenkins inspired Ansible to finally deploying the app.</p>
<img width="651" alt="CI CD pipeline" src="https://user-images.githubusercontent.com/66776309/109552161-60718680-7ac9-11eb-8794-412861ccaf22.png">
<h2 id="jenkins-pipeline">Jenkins Pipeline</h2>
<p>Jenkins was the heart and soul of the automation of this project. Using a pipeline build I automated many mundane tasks through commands in my Jenkinsfile which further triggered other automatic processes such as building images then pushing them to DockerHub and so on.</p>
<p>Below is a successful pipeline showing the various stages of automation.</p>
<img width="700" alt="jenkinspipeine" src="https://user-images.githubusercontent.com/66776309/109553126-8a777880-7aca-11eb-8c7a-11ad3651cb5d.png">
<h2 id="testing">Testing</h2>
<p>I tested my various services through Pytesting. I conducted unit tests as well as Mock tests, the unit tests ensured the page was running as was hoped whilst the mock tests tested functionality. Below is an example of testing passing and a coverage of 96% being achieved.</p>
<img width="506" alt="project2 tests" src="https://user-images.githubusercontent.com/66776309/109541016-2d27fb00-7abb-11eb-8f44-a0498c8bce2c.png">
<h2 id="risk-assessment">Risk Assessment</h2>
<p><strong>My initial risk-assessment</strong></p>
<img width="575" alt="risk assessment" src="https://user-images.githubusercontent.com/66776309/109549027-49c93080-7ac5-11eb-8e08-4daf1b63e5f8.png">
<p>Whilst carrying out the project I realised I needed to update my Risk Assessment as a few more risks had emerged.<br>
<img width="488" alt="riskassessment2" src="https://user-images.githubusercontent.com/66776309/109548873-138bb100-7ac5-11eb-8385-65941a7c5be5.png"></p>
<p><strong>Further Enhancements</strong></p>
<ul>
<li>Use of CSS and Javascript to create an appealing front-end experience</li>
<li>Allow for an Image/Logo to be in relation to output</li>
<li>Further enhancement of project specification by including more services and more different requests</li>
</ul>
<p><strong>Acknowledgements</strong><br>
QA Training Academy for allowing me to develop and implement skills I was previously oblivious to.</p>
<p><strong>Author</strong><br>
Bilal Mustafa</p>

