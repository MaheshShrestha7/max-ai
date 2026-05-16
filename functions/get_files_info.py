import os
from google.genai import types
#- README.md: file_size=1032 bytes, is_dir=False
#- src: file_size=128 bytes, is_dir=True
#- package.json: file_size=1234 bytes, is_dir=False


def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    
    abs_directory=os.path.abspath(os.path.join(working_directory,directory))

    if not abs_directory.startswith(abs_working_directory) :
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    


    final_response=""
    contents = os.listdir(abs_directory)    

    for content in contents : 
        content_path = os.path.join(abs_directory,content)
        is_dir = os.path.isdir(content_path)
        size =  os.path.getsize(content_path)
        final_response +=f"- {content} : file_size={size} bytes, is_dir={is_dir}"
    
    return final_response    


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)