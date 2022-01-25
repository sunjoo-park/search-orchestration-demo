pipeline {
    agent any
    triggers {
        issueCommentTrigger('.*start build.*')
        githubPush()
    }
    stages {
        stage('Get methods') {
            steps {
                script {
                    sh 'env|sort'
                }
            }
        }
    }

    post {

        always {
            script {
                    pullRequest.createStatus(status: 'error',
                         description: 'Failed',
                         targetUrl: "${env.BUILD_URL}")
            }
        }

    }
}
