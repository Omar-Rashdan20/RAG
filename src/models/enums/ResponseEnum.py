from enum import Enum
class ResponseEnum(str, Enum):
    SUCCESS = "Success"
    FAILURE = "Failure"
    INVALID_FILE_TYPE = "Invalid file type"
    FILE_TOO_LARGE = "File size exceeds the maximum limit"