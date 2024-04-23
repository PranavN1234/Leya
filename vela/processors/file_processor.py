import ast
import astunparse
import os

def chunk_code(file_path):
    with open(file_path, "r") as file:
        source = file.read()

    tree = ast.parse(source)
    chunks = []

    # Extract source file name
    file_name = os.path.basename(file_path)

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            # Use astunparse to get the source code of the current node
            node_source = astunparse.unparse(node)

            # Construct the function definition string
            function_definition = node_source.strip()

            # Add the function information to the list
            chunks.append({
                "function_name": node.name,
                "function_definition": function_definition,
                "source_file_structure": None,  # First line of the file
                "source_file_name": file_name
            })

    return chunks
