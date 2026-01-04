def send_internal_alert(data):
    message = (
        f"🚨 New RFQ Received\n"
        f"Client: {data['contact_name']}\n"
        f"Product: {data['product']}\n"
        f"Qty: {data['quantity']}\n"
        f"City: {data['city']}"
    )
    print(message)
