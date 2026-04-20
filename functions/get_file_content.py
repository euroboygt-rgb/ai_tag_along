import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        # Normalize paths for security
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))
        
        # Security: Ensure the file is inside the working directory
        if os.path.commonpath([abs_working_dir]) != os.path.commonpath([abs_working_dir, abs_file_path]):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Check if it is a valid file
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read the file up to the MAX_CHARS limit
        with open(abs_file_path, "r", encoding="utf-8") as f:
            content = f.read(MAX_CHARS)
            
            # Check if there is more content (truncation check)
            if f.read(1):
                content += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            
            return content

    except Exception as e:
        return f"Error: {str(e)}"
