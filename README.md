# AI Trading

## Table of Contents

- [Project Description](#project-description)
- [Directory Structure](#directory-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
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
│   ├── data_services/                  # Deployment for data services
│   │   ├── Dockerfile
│   │   ├── job.yaml
│   │   ├── run.sh
│   │   └── update_docker_image.sh
│   └── other_service/                  # Additional services can be added here
│       ├── Dockerfile
│       ├── job.yaml
│       ├── run.sh
│       └── update_docker_image.sh
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
│   ├── data_services/                  # Data service to download and manage data
│   │   ├── download_data/
│   │   │   ├── main.py
│   │   │   ├── requirements.txt
│   │   │   └── ...
│   │   └── other_data_service/
│   │       ├── main.py
│   │       ├── requirements.txt
│   │       └── ...
│   └── other_services/                  # Future services can be added here
│
└── tests/                              # Unit and integration tests
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
    ./ setup.sh
    ```

3. **Build Docker images for services:**

    ```bash
    docker build -t your-docker-repo/data-service -f Dockerfile .
    # Repeat for other services if necessary
    ```

4. **Deploy the infrastructure using Terraform:**

    ```bash
    cd terraform
    terraform init
    terraform plan
    terraform apply
    ```

5. **Deploy the services to Kubernetes:**

    ```bash
    kubectl apply -f deployments/....yaml
    # Repeat for other service deployment files if necessary
    ```

## Usage

### Running the script

1. **Start the services locally:**

    ```bash
    python src/services/download_data.py
    # Repeat for other services if necessary
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

