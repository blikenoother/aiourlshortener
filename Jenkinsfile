#!/usr/bin/env groovy

def python_versions = [
    "3.4.3", "3.4.4", "3.4.5", "3.4.6", "3.4.7",
    "3.5.0", "3.5.1", "3.5.2", "3.5.3", "3.5.4",
    "3.6.0", "3.6.1", "3.6.2", "3.6.3", "3.6.4",
]

def steps = python_versions.collectEntries {
    ["Python $it": run_ci(it)]
}

parallel steps


def get_env() {
    return [
        'HOME=/tmp/',
    ]
}

def get_credentials() {
    return [
        string(credentialsId: 'AIOURLSHORTENER_BITLY',
               variable: 'AIOURLSHORTENER_BITLY'),
        string(credentialsId: 'AIOURLSHORTENER_GOOGLE',
               variable: 'AIOURLSHORTENER_GOOGLE'),
    ]
}

def run_ci(python_version) {
    return {
        timestamps {
            withEnv(get_env()) {
                withCredentials(get_credentials()) {
                    docker.image("python:${python_version}").inside {
                        checkout scm
                        sh 'make install venv=/tmp/venv'
                        sh 'make test venv=/tmp/venv'
                    }
                }
            }
        }
    }
}
