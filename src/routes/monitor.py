from flask import Blueprint, request
from ..services.ping_service import ping_host
from ..services.github_service import github_status

monitor_bp = Blueprint("monitor", __name__)

@monitor_bp.get("/monitor/ping")
def monitor_ping():
    host = request.args.get("host", "8.8.8.8")
    return ping_host(host)

@monitor_bp.get("/monitor/github")
def monitor_github():
    return github_status()