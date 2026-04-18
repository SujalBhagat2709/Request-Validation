# Request Validation

## Overview

Simple validation system for file uploads.

---

## Features

* Check file type (jpg, jpeg, png)
* Check file size (max 5MB)
* Combined validation function

---

## Files

* `file_validator.py` → checks extension
* `size_validator.py` → checks file size
* `validate_request.py` → combines validation

---

## Usage

```id="u8cbf1"
python validate_request.py
```

---

## Output Example

```id="6mb81f"
{'status': True, 'message': 'Valid request'}
```

---

## Use Case

Can be used before:

* Image upload APIs
* ML model inference
* File processing systems
