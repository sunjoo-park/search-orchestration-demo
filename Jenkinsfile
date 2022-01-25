pipeline {
    agent any
    triggers {
        issueCommentTrigger('.*start build.*')
        githubPush()
    }
    stages {
        stage('Get methods') {
            steps {
                sh 'ls'
                sh 'hostname'
                sh 'env|sort'
                pullRequest.addLabel('Build Passing')
            }
        }
    }
}

