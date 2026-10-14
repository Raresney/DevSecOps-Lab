import json
from datetime import datetime, timezone


def create_event(event_type: str, severity: str) -> dict:
    """Create a structured security event."""
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event_type": event_type,
        "severity": severity,
    }


def main():
    event = create_event("application_started", "info")
    print(json.dumps(event, indent=2))


if __name__ == "__main__":
    main()


