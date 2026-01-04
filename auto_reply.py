def generate_reply(data, lang="en"):
    if lang == "ar":
        return f"""
عزيزي {data['contact_name']},

شكرًا لطلب عرض السعر الخاص بـ {data['quantity']} وحدة من {data['product']}.
سيتم التواصل معكم قريبًا.

مع التحية،
شركة الروؤف للإضاءة
"""
    return f"""
Dear {data['contact_name']},

Thank you for your RFQ for {data['quantity']} units of {data['product']}.
Our sales team is reviewing your request and will contact you shortly.

Best regards,
Alrouf Lighting
"""
