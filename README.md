# **Automated Deployment with S3 Logs** 🚀

## **Overview**

This project automates the deployment of an open-source web application by:\
✅ **Containerizing** the app using Docker\
✅ Setting up a **CI/CD pipeline** using Jenkins\
✅ Deploying it to an **AWS EC2 instance**\
✅ Configuring **log storage** in an **S3 bucket**

## **Tech Stack**

- **Docker** 🐳 - Containerization
- **Jenkins** 🤖 - CI/CD Automation
- **AWS EC2** ☁️ - Hosting the application
- **AWS S3** 📦 - Storing logs
- **Bash Scripting** 🖥️ - Automating deployment

## **Project Structure**

```
📂 Automated-Deployment-With-S3-Logs
│── 📂 app-code/               # The open-source app's code
│── 📂 docker/                 # Docker-related files
│   ├── Dockerfile             # The Dockerfile for containerization
│── 📂 scripts/                # Deployment automation scripts
│   ├── deploy.sh              # Deploys app to EC2
│   ├── configure-s3.sh        # Configures S3 log storage
│── 📂 jenkins/                # CI/CD pipeline files
│   ├── Jenkinsfile            # Defines the Jenkins pipeline
│── README.md                  # Project documentation
│── .gitignore                 # Ignoring unnecessary files
```

## **How It Works**

1️⃣ **Containerization**

- The application is **Dockerized** using a `Dockerfile`.
- The image is pushed to a **Docker registry** (ECR or Docker Hub).

2️⃣ **CI/CD Pipeline (Jenkins)**

- **Triggered on GitHub commits** ✅
- Builds and pushes the **Docker image** 🚀
- Deploys the app on **EC2** 🔄

3️⃣ **EC2 Deployment**

- **Pulls & runs** the latest Docker image.
- Exposes the application on a public IP.

4️⃣ **Log Storage in S3**

- A **cron job** on EC2 **uploads logs** every hour.

## **Setup Guide**

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/your-username/Automated-Deployment-With-S3-Logs.git
cd Automated-Deployment-With-S3-Logs
```

### **2️⃣ Build & Run Docker Container**

```bash
docker build -t my-app .
docker run -d -p 8080:8080 my-app
```

### **3️⃣ Configure Jenkins Pipeline**

- Install **Jenkins + Docker Plugin**
- Create a new **pipeline job**
- Use the `Jenkinsfile` in this repo

### **4️⃣ Deploy to EC2 & Connect S3 Logs**

```bash
bash scripts/deploy.sh
bash scripts/configure-s3.sh
```

---


## **Contributors**

- **Ali (frenzyali)** 👨‍💻

---
