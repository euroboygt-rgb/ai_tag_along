import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        # 1. Path Validation
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        
        if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # 2. Check if file exists and is a regular file
        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        # 3. Check for .py extension
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        # 4. Build the command
        command = ["python", abs_file_path]
        if args:
            command.extend(args)

        # 5. Run the subprocess
        result = subprocess.run(
            command,
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            timeout=30
        )

        # 6. Build output string
        output = ""
        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}\n"
        
        if not result.stdout and not result.stderr:
            output += "No output produced"
        else:
            if result.stdout:
                output += f"STDOUT:\n{result.stdout}"
            if result.stderr:
                output += f"STDERR:\n{result.stderr}"

        return output.strip()

    except Exception as e:
        return f"Error: executing Python file: {e}"
