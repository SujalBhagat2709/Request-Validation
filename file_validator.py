ALLOWED_EXTENSIONS = ["jpg", "jpeg", "png"]

def is_valid_file(filename):
    
    if "." not in filename:
        return False
    
    ext = filename.split(".")[-1].lower()
    
    return ext in ALLOWED_EXTENSIONS


if __name__ == "__main__":
    print(is_valid_file("image.jpg"))   # True
    print(is_valid_file("file.txt"))    # False