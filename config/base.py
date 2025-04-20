from dataclasses import dataclass

from environs import Env

env = Env()


@dataclass
class OpenTelemetryConfig:
    service_name: str
    otlp_endpoint: str
    environment: str


class BaseConfig:
    SERVICE_NAME = env("SERVICE_NAME", "sealify")
    ENVIRONMENT = env("ENVIRONMENT", "local")

    #
    # Logging config
    #
    LOG_LEVEL = env("LOG_LEVEL", "INFO")
    LOG_FORMAT = env(
        "LOG_FORMAT",
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    #
    # Database config
    #
    DB_CONNECTION_STRING = env("DATABASE_URL", "sqlite:///./warehouse.db")

    #
    # OpenTelemetry config
    #
    OTEL_OTLP_ENDPOINT = env("OTEL_OTLP_ENDPOINT", "http://localhost:4317")
    OTEL_SERVICE_NAME = env("OTEL_SERVICE_NAME", SERVICE_NAME)
    OTEL_ENVIRONMENT = env("OTEL_ENVIRONMENT", ENVIRONMENT)

    def get_otel_config(self) -> OpenTelemetryConfig:
        return OpenTelemetryConfig(
            service_name=self.OTEL_SERVICE_NAME,
            otlp_endpoint=self.OTEL_OTLP_ENDPOINT,
            environment=self.OTEL_ENVIRONMENT,
        )
