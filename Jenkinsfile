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
                    def commitId = '567e7110ac0a3de2053c22001627974703fa376f'
                    def path = 'Jenkinsfile'
                    def lineNumber = 1
                    def body = 'The review comment'
                    def comment = pullRequest.reviewComment(commitId, path, lineNumber, body)
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
