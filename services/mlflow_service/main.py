import mlflow
from mlflow import log_metric, log_param, log_artifacts

if __name__ == "__main__":
    mlflow.set_tracking_uri("http://localhost:5000")  # zmień URL dla środowiska klastra
    mlflow.set_experiment("ai_trading_experiment")

    with mlflow.start_run():
        log_param("param1", 5)
        log_metric("metric1", 0.85)
        mlflow.log_artifacts("path/to/artifacts")