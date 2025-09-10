import os

def mm_to_cm(mm: float):
        return mm / 10.0
    
def cm_to_mm(cm: float):
    return cm * 10.0

def is_file_exists(file_path: str):
    return os.path.isfile(file_path)

def is_image_file(file_path: str):
    _, extension = os.path.splitext(file_path.lower())

    is_extension = extension in {'.jpg', '.jpeg', '.png'}

    return is_extension