from enum import Enum
class ResponseEnum(str, Enum):
    SUCCESS = "Success upload"
    FAILURE = "Failure"
    INVALID_FILE_TYPE = "Invalid file type"
    FILE_TOO_LARGE = "File size exceeds the maximum limit"
    