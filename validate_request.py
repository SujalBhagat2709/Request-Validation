from file_validator import is_valid_file
from size_validator import is_valid_size

def validate(filename, file_size):
    
    if not is_valid_file(filename):
        return {"status": False, "error": "Invalid file type"}
    
    if not is_valid_size(file_size):
        return {"status": False, "error": "File too large"}
    
    return {"status": True, "message": "Valid request"}


if __name__ == "__main__":
    
    result = validate("test.jpg", 1024 * 1024)
    print(result)