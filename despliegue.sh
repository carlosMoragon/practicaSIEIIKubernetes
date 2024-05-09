#!/bin/bash

# Construir la imagen del contenedor
docker build -t reloj-app:latest .

# Etiquetar la imagen del contenedor para Artifact Registry
docker tag reloj-app:latest europe-west2-docker.pkg.dev/dark-yen-414408/practicak8s/reloj-app:latest

# Empujar la imagen del contenedor a Artifact Registry
docker push europe-west2-docker.pkg.dev/dark-yen-414408/practicak8s/reloj-app:latest

# Obtener las credenciales del clúster de Kubernetes
gcloud container clusters get-credentials practicak8s --region europe-west2

# Aplicar el archivo de orquestación de Kubernetes
kubectl apply -f archivo_orquestacion.yaml
