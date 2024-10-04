# AI Trading

## Project Description

AI Trading is a project aimed at creating a fully automated trading bot that utilizes machine learning algorithms to analyze market data and make trading decisions. The bot is designed to be highly modular, scalable, and easy to deploy on Kubernetes (k8s).

## Table of Contents

- [Project Description](#project-description)
- [Directory Structure](#directory-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Directory Structure

...


## Setup and Installation

### Prerequisites

#### Basic
- Python 3.10+
- pip (Python package installer)

#### To run on cluster
- Docker
- Terraform
- Kubernetes cluster

### Installation Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/bartoszbok/ai-trading.git
    cd ai-trading
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Build Docker images for services:**

    ```bash
    docker build -t your-docker-repo/data-service -f Dockerfile .
    # Repeat for other services if necessary
    ```

5. **Deploy the infrastructure using Terraform:**

    ```bash
    cd terraform
    terraform init
    terraform plan
    terraform apply
    ```

6. **Deploy the services to Kubernetes:**

    ```bash
    kubectl apply -f deployments/....yaml
    # Repeat for other service deployment files if necessary
    ```

   **OR run this command:**

    ```bash
    ./setup.sh
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

