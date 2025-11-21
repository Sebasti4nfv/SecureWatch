from prometheus_client import Histogram

api_incidentes_latencia_ms = Histogram(
    "api_incidentes_latencia_ms",
    "Tiempo de respuesta del endpoint /incidentes",
    buckets=[50, 100, 200, 500, 1000]
)
