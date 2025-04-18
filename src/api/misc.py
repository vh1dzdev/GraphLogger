class Response:
    Create_Response = {
        200: {
            "description": "Success",
            "content": {
                "application/json": {
                    "example": {
                        "status": "success",
                        "logger_id": "1234123123"
                    }
                }
            }
        }
    }

    Delete_Response = {
        200: {
            "description": "Success",
            "content": {
                "application/json": {
                    "example": {
                        "status": "success",
                        "message": ""
                    }
                }
            }
        }
    }

    GetLogs_Response = {
        200: {
            "description": "Success",
            "content": {
                "application/json": {
                    "example": {
                        "status": "success",
                        "logger_id": "123123123",
                        "logs": "..."
                    }
                }
            }
        }
    }