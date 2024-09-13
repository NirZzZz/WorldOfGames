pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "world-of-games"
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials') //
        SCORES_FILE = "scores.db" //
    }

    stages {
        stage('Checkout') {
            steps {
                //
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    //
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    //
                    sh """
                        docker run -d --name test_container \
                        -p 8777:8777 \
                        -v ${SCORES_FILE}:/app/scores.db ${DOCKER_IMAGE}
                    """
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    //
                    try {
                        sh "python3 e2e.py"
                    } catch (Exception e) {
                        //
                        error "End-to-End tests failed!"
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    //
                    sh "docker stop test_container && docker rm test_container"

                    //
                    sh """
                        echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin
                    """

                    // P
                    sh "docker tag ${DOCKER_IMAGE} ${DOCKERHUB_CREDENTIALS_USR}/${DOCKER_IMAGE}:latest"
                    sh "docker push ${DOCKERHUB_CREDENTIALS_USR}/${DOCKER_IMAGE}:latest"
                }
            }
        }
    }

    post {
        always {
            //
            sh 'docker rm -f test_container || true'
            sh 'docker rmi ${DOCKER_IMAGE} || true'
        }
    }
}