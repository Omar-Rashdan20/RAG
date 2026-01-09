from enum import Enum
class ResponseEnum(str, Enum):
    SUCCESS = "Success upload"
    FAILURE = "Failure"
    INVALID_FILE_TYPE = "Invalid file type"
    FILE_TOO_LARGE = "File size exceeds the maximum limit"
    FILE_NOT_FOUND = "File not found"
    UPLOAD_ERROR = "Error occurred during file upload"
    PROCESSING_ERROR = "Error occurred during file processing"
    PROJECT_NOT_FOUND = "Project not found"
    UNAUTHORIZED = "Unauthorized access"
    FORBIDDEN = "Forbidden access"
    SERVER_ERROR = "Internal server error"
    TIMEOUT = "Request timed out"
    CONFLICT = "Conflict occurred"
    BAD_REQUEST = "Bad request"
    NOT_IMPLEMENTED = "Not implemented"
    SERVICE_UNAVAILABLE = "Service unavailable"
    DEPENDENCY_ERROR = "Dependency error occurred"
    
    