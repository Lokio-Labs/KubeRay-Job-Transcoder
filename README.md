# KubeRay-Job-Transcoder
The KubeRay Job Transcoder automates converting Python Ray scripts into Kubernetes Job YAML files. These files are executed as pods in a Kubernetes cluster. It also ensures security best practices, like using non-root privileges and proper container configurations.

Usage:
python3 kuberay-job-transcoder.py <file_to_convert>

Example:
python3 kuberay-job-transcoder.py hello_world.py
