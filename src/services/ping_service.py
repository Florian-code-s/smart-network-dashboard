from ping3 import ping

def ping_host(host: str, timeout: float = 1.0):
    rtt = ping(host, timeout=timeout)  # seconds or None
    if rtt is None:
        return {"host": host, "reachable": False, "rtt_ms": None}
    return {"host": host, "reachable": True, "rtt_ms": round(rtt * 1000, 2)}