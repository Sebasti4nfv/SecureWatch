from fastapi import FastAPI, Request, Header
from kafka import KafkaProducer
import json, uuid
from datetime import datetime

app = FastAPI()

producer = KafkaProducer(
    bootstrap_servers=["kafka:9092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

@app.post("/api/v1/logs")
async def ingest_log(request: Request, x_client_id: str = Header(...)):
    data = await request.json()
    event = {
        "id": str(uuid.uuid4()),
        "client_id": x_client_id,
        "log": data.get("log"),
        "source": data.get("source", "unknown"),
        "timestamp": datetime.utcnow().isoformat()
    }
    producer.send("logs_generic", event)
    return {"status": "ok", "event_id": event["id"]}
