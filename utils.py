import os

def get_files_in_dir(directory: str):
    """Returns a list of all file names in the given directory."""
    try:
        return [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
        return []
