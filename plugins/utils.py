def handle_response(response):
    """
    Check response status
    """
    if response.status_code == 200:
        return True
    return False
