MAX_SIZE_MB = 5

def is_valid_size(file_size_bytes):
    
    size_mb = file_size_bytes / (1024 * 1024)
    
    return size_mb <= MAX_SIZE_MB


if __name__ == "__main__":
    print(is_valid_size(2 * 1024 * 1024))  # True
    print(is_valid_size(10 * 1024 * 1024)) # False