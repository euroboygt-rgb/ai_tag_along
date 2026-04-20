from google.genai import types
# 1. Imports for the actual logic and the first schema
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file

# 2. Define your schemas (Make sure these dictionaries are full and uncommented)
schema_get_file_content = {
    "name": "get_file_content",
    "description": "Read the content of a specific file",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "file_path": {"type": "STRING", "description": "The path to the file"}
        },
        "required": ["file_path"]
    }
}

schema_run_python_file = {
    "name": "run_python_file",
    "description": "Execute a Python script",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "file_path": {"type": "STRING", "description": "The path to the .py file"},
            "args": {
                "type": "ARRAY", 
                "items": {"type": "STRING"}, 
                "description": "List of arguments"
            }
        },
        "required": ["file_path"]
    }
}

schema_write_file = {
    "name": "write_file",
    "description": "Write content to a file",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "file_path": {"type": "STRING", "description": "The target file path"},
            "content": {"type": "STRING", "description": "The text to write"}
        },
        "required": ["file_path", "content"]
    }
}

# 3. Define the Tool list AFTER the schemas are defined
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ],
)

# 4. Your dispatcher function
def call_function(function_call, verbose=False):
    function_name = function_call.name or ""

    if verbose:
        print(f"Calling function: {function_name}({function_call.args})")
    else:
        print(f" - Calling function: {function_name}")

    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    # Prepare arguments with a shallow copy (Step 6)
    args = dict(function_call.args) if function_call.args else {}

    # Set working directory constraint (Step 7)
    args["working_directory"] = "./calculator"

    # Execute (Step 8)
    function_to_call = function_map[function_name]
    function_result = function_to_call(**args)

    # Return response (Step 9)
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
