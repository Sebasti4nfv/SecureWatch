from prometheus_client import Counter

ingesta_requests_total = Counter(
    "ingesta_requests_total",
    "Cantidad de logs recibidos por el servicio de ingesta"
)
