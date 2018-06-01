# The Lyrics App

This is a demo app designed to demonstrate a basic REST API that does it's level
best to determine the parts of speech in popular song lyrics. Specifically it
has three paths:

* GET `/verbs/<artist>/<title>` => verbs [json]
* GET `/adjectives/<artist>/<title>` => adjectives [json]
* GET `/healthz` => response code 200

## Using this app

When developing the app directly, it's easy to just run the docker container:

```bash
docker build . -t lyrics-app
docker run -p 8080:8080 lyrics_app
```

Then, just use `curl`!

```bash
curl 'http://127.0.0.1:8080/adjectives/Prince/Little%20Red%20Corvette'
```

```bash
curl 'http://127.0.0.1:8080/verb/Prince/Little%20Red%20Corvette'
```

And you're off to the races!

## Deploying to Kubernetes
This app has been pushed to the Docker Hub, so it can be pulled from there
directly. 

First, start your minikube cluster

```
minikube start
```

Check to ensure it's up

```
kubectl cluster-info
```

Then begin your deployment of the app

```
kubectl create -f kubernetes/deployment.yaml
kubectl create -f kubernetes/service.yaml
kubectl create -f kubernetes/ingress.yaml
```

Next, be sure to update your `/etc/hosts` file or resolver

```bash
MINIK8S_IP=$(minikube ip)
unamestr=$(uname)
if [[ "$unamestr" == 'Darwin' ]]; then
  TEE_COMMAND=$(which gtee)
else
  TEE_COMMAND=$(which tee)
fi

if ! grep 'lyrics.sample.devel' /etc/hosts > /dev/null; then
  echo "${MINIK8S_IP} lyrics.sample.devel" | sudo "$TEE_COMMAND" --append /etc/hosts
fi
```

Finally, be sure to test your code:

```bash
curl http://lyrics.samplel.devel/verbs/Muse/Uprising
```
