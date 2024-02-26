import json

def extract_code_from_ipynb(ipynb_file_path):
    with open(ipynb_file_path, "r") as file:
        content = json.load(file)
    
    code_fragments = []
    
    # Iterate through each cell in the notebook
    for cell in content['cells']:
        # Check if the cell is a code cell
        if cell['cell_type'] == 'code':
            # Get the source code from the cell
            source_code = ''.join(cell['source'])
            code_fragments.append(source_code)
    
    return code_fragments