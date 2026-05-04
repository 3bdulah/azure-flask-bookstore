# Bookstore App with MongoDB & Azure Kubernetes Service (AKS)

**Public repository:** [github.com/3bdulah/azure-flask-bookstore](https://github.com/3bdulah/azure-flask-bookstore) — start there for badges, CI, and the high-level README.

## Overview
The **Bookstore App** is a cloud-based application developed using Python, Flask, and MongoDB. It is deployed on **Azure Kubernetes Service (AKS)** with Docker images stored in **Azure Container Registry (ACR)**. The application supports full CRUD (Create, Read, Update, Delete) operations for managing book records.

## Features
- **Create, Read, Update, Delete (CRUD) Operations:** Add, view, update, and delete book records.
- **Cloud Deployment:** Fully containerized and deployed using AKS.
- **Secure Networking:** Kubernetes Network Policies for secure communication between pods.
- **Database Management:** MongoDB hosted on Azure Cosmos DB with automatic scaling and backup.

## Project Architecture
1. **Azure Kubernetes Service (AKS)**: Hosts the application.
2. **MongoDB CosmosDB Instance**: Database backend.
3. **Flask Application Pods**: Application backend using Flask.
4. **Azure Container Registry (ACR)**: Stores Docker container images.
5. **Kubernetes Services**: Manages LoadBalancer and ClusterIP services.

## Deployment Guide
### Prerequisites
- Azure Subscription
- Azure CLI Installed
- Docker Installed
- kubectl Installed
- Python 3.x Installed

### Deployment Steps
1. **Setup Azure CosmosDB:**
   - Create a MongoDB API instance in Azure CosmosDB.
   - Collect the connection string.

2. **Create Azure Container Registry (ACR):**
   - Use Azure Portal to create an ACR.

3. **Docker Image Creation:**
   - Build the Docker image:
     ```bash
     docker build -t <acr-login-server>/bookstore-app:latest .
     ```
   - Push the Docker image to ACR:
     ```bash
     docker push <acr-login-server>/bookstore-app:latest
     ```

4. **Create AKS Cluster:**
   - Deploy AKS using Azure Portal and link it with ACR.

5. **Deploy Kubernetes Resources:**
   - Edit `YAML/deployment.yaml` (container image), `YAML/configmap.yaml`, and `YAML/secrets.yaml` with your values. Do not commit real secrets.
   - From the `YAML` directory, apply manifests:
     ```bash
     cd YAML
     kubectl apply -f mongodb-pvc.yaml
     kubectl apply -f mongodb-deployment.yaml
     kubectl apply -f mongodb-service.yaml
     kubectl apply -f service.yaml
     kubectl apply -f deployment.yaml
     kubectl apply -f configmap.yaml
     kubectl apply -f secrets.yaml
     kubectl apply -f network-policy.yaml
     ```
   - Verify application status:
     ```bash
     kubectl get all
     ```

6. **Application Access:**
   - Access the application via the Azure LoadBalancer external IP.

## Configuration Files
- **YAML Files:** Found under the `YAML/` folder.
- **Source Code:** Flask application source code under `app/`.

## Technologies Used
- **Azure Services:** Azure Kubernetes Service (AKS), Azure Container Registry (ACR), Azure Cosmos DB.
- **Application Framework:** Flask (Python).
- **Database:** MongoDB.
- **Containerization:** Docker.
- **Orchestration:** Kubernetes.

## Contributors
- **Project Owner:** Abdullah Hani Abdellatif Al-Shobaki
- **Student ID:** 2284612

## License
This project is licensed under the MIT License.

## Acknowledgments
Special thanks to the course instructor **Gökşin Bakır** for the guidance and support throughout the project.

---

**Note:** Ensure that the AKS cluster is running when accessing the application and that all required Azure services are correctly configured.