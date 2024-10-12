# AI Trading

## Table of Contents

- [Project Description](#project-description)
- [Directory Structure](#directory-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage locally](#usage-locally)
- [Contributing](#contributing)
- [License](#license)

## Project Description

The AI Trading project aims to create an assistant that will analyze market data, identify patterns and dependencies, and notify users when a significant relationship is detected.
In a potential next phase, the system could be connected via API to develop an automated trading bot.
The bot is designed to be highly modular, scalable, and easy to deploy on Kubernetes (k8s).

## Directory Structure
```
ai-trading/
│
├── deployments/                        # Kubernetes deployment files
│   └── ...
│
├── infra/                              # Infrastructure-related files
│   ├── minikube/                       # Scripts for managing Minikube
│   │   ├── restart_minikube.sh
│   │   └── start_minikube.sh
│   ├── minio/                          # Setup and management scripts for MinIO
│   │   ├── delete_minio.sh
│   │   ├── forward_minio.sh
│   │   ├── install_minio.sh
│   │   └── set_minio_secrets.sh
│   └── terraform/                      # Terraform files for infrastructure provisioning
│
├── services/                           # Microservices source code
│   └── ...
│
└── tests/                              # Unit and integration tests
```

Every service in `deployment/` have structure like this:
```
deployments/
   └── example_service/
       ├── Dockerfile
       ├── job.yaml
       ├── run.sh
       └── update_docker_image.sh
```

Every service in `services/` have structure like this:
```
services/
    └── example_service/                
        ├── main.py
        ├── requirements.txt
        └── src/
```

## Setup and Installation

### Prerequisites

#### Basic
- Python 3.10+
- pip (Python package installer)

#### To run on cluster
- Docker
- Terraform
- Kubernetes cluster (`minio` to run local or other cluster to run on the cloud)

### Installation Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/bartoszbok/ai-trading.git
    cd ai-trading
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    ./setup.sh
    ```
   
### Deploy Steps

1. **Setup cluster:**

    ```bash
    ./infra/clusters/CLUSTER_NAME/start.sh
    ```

2. **Setup minio:**

    ```bash
    ./infra/minio/install_minio.sh
    ./infra/minio/set_minio_secrets.sh
    ```

3. **Deploy the infrastructure using Terraform:**

   #TODO

    ```bash
    cd infra/terraform
    terraform init
    terraform plan
    terraform apply
    ```

4. **Build Docker images for services:**

    ```bash
    ./deployments/SERVICE_DIR/update_docker_image.sh
    ```

5. **Deploy the services to Kubernetes:**

    ```bash
    ./deployments/SERVICE_DIR/run.sh
    ```

## Usage locally

### Running the script locally

1. **Start the service locally:**

    ```bash
    python3 services/SERVICE_DIR/main.py
    ```

### Jupyter Notebooks

Explore the provided Jupyter notebooks in the `notebooks/` directory for examples and experiments.

## Contributing

We welcome contributions to improve AI Trading! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

