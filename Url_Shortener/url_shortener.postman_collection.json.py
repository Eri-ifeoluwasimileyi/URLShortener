var = {
    "info": {
        "name": "URL Shortener API",
        "_postman_id": "12345678-abcd-efgh-ijkl-9876543210",
        "description": "Postman collection for URL Shortener Flask API",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
    },
    "item": [
        {
            "name": "Shorten URL",
            "request": {
                "method": "POST",
                "header": [
                    {
                        "key": "Content-Type",
                        "value": "application/json"
                    }
                ],
                "body": {
                    "mode": "raw",
                    "raw": "{\n    \"long\": \"https://www.example.com\"\n}"
                },
                "url": {
                    "raw": "http://localhost:5000/shorten",
                    "protocol": "http",
                    "host": ["localhost"],
                    "port": "5000",
                    "path": ["shorten"]
                }
            },
            "response": []
        },
        {
            "name": "Redirect Short URL",
            "request": {
                "method": "GET",
                "url": {
                    "raw": "http://localhost:5000/abc123",
                    "protocol": "http",
                    "host": ["localhost"],
                    "port": "5000",
                    "path": ["abc123"]
                }
            },
            "response": []
        }
    ]
}
