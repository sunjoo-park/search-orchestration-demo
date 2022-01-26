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
                    if(env.CHANGE_ID) {
                        echo pullRequest.title
                        echo pullRequest.body
                        echo pullRequest.state
                        echo pullRequest.labels[0]
                        pullRequest.comment("Ttes Commenv " + env.JENKINS_URL)
                    }
                }
            }
        }
    }
    post {
        success {
            script {
            /*
                    pullRequest.createStatus(status: 'error',
                         description: 'Failed',
                         targetUrl: "${env.BUILD_URL}")
                         */
                echo "post: success"
                if(env.CHANGE_ID) {
                    pullRequest.comment("Post Section")
                }
            }
        }

    }
}
