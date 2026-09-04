from fastapi import FastAPI
import psutil
import platform
import socket

app = FastAPI(title="CloudOps Lab")


@app.get("/")
def root():
    return {
        "service": "CloudOps Lab",
        "status": "running",
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent,
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
