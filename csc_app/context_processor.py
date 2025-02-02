def global_context(request):
    return {
        "company": "Annamalai Nagar",
        "user_ip": request.META.get("REMOTE_ADDR", "Unknown"),
    }
    
company = "Annamalai Nagar"
site_pass = "608002"