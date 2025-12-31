# Contact Manager API

A simple REST API to manage contacts using Python (FastAPI) and MongoDB, running on Kubernetes.

# Prerequisites
* **Docker** (Desktop or Engine)
* **Minikube** (Local Kubernetes cluster)
* **Kubectl** (Kubernetes CLI)

# Setup & Run

# 1. Start Minikube
Start your local Kubernetes cluster:
```bash
minikube start
```

# 2. Navigate to Project
``` bash 
cd week11_k8s_contacts
```

# 3. Apply the configuration files for MongoDB and the API:
``` bash
kubectl apply -f k8s/
```

# 4. Expose the service and open the connection:
``` bash
minikube service api-service
```
