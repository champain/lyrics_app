#!/usr/bin/env bash

minikube start
MINIK8S_IP=$(minikube ip)
unamestr=$(uname)
if [[ "$unamestr" == 'Darwin' ]]; then
  TEE_COMMAND=$(which gtee)
else
  TEE_COMMAND=$(which tee)
fi

if ! kubectl cluster-info; then
  echo "Something's wrong with minikube, check it, and try again"
  exit 2
fi

kubectl create -f kubernetes/deployment.yaml
kubectl create -f kubernetes/service.yaml
kubectl create -f kubernetes/ingress.yaml

if ! grep 'lyrics.sample.devel' /etc/hosts > /dev/null; then
  echo "${MINIK8S_IP} lyrics.sample.devel" | sudo "$TEE_COMMAND" --append /etc/hosts
fi

curl http://lyrics.samplel.devel/verbs/Muse/Uprising
