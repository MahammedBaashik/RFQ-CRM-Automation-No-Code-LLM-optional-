import json
from datetime import datetime

def create_opportunity(data, path="data/crm_opportunities.json"):
    opportunity = {
        "id": f"OPP-{int(datetime.now().timestamp())}",
        "client": data["contact_name"],
        "product": data["product"],
        "quantity": data["quantity"],
        "city": data["city"],
        "status": "New RFQ"
    }

    try:
        with open(path, "r") as f:
            existing = json.load(f)
    except FileNotFoundError:
        existing = []

    existing.append(opportunity)

    with open(path, "w") as f:
        json.dump(existing, f, indent=2)

    return opportunity
