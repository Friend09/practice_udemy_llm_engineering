import nbformat
import os
import sys

def clear_notebooks(source_dir, destination_dir):
    """
    Clear code and output cells from Jupyter notebooks in a source directory and save them to a destination directory.

    This function processes Jupyter notebook files (.ipynb) by:
    1. Creating an empty destination directory if it doesn't exist
    2. Reading each notebook from the source directory
    3. Clearing all code cell contents and outputs
    4. Saving the cleared notebook to the destination directory with 'practise_' prefix

    Parameters:
        source_dir (str): Path to the directory containing original notebooks
        destination_dir (str): Path to the directory where cleared notebooks will be saved

    Returns:
        None

    Example:
        >>> clear_notebooks('path/to/source', 'path/to/destination')
        Processed: path/to/source/notebook.ipynb -> path/to/destination/practise_notebook.ipynb

    Notes:
        - Only processes files with .ipynb extension
        - Preserves markdown cells and notebook structure
        - Creates destination directory if it doesn't exist
        - Adds 'practise_' prefix to output filenames
    """
    # Ensure destination directory exists
    os.makedirs(destination_dir, exist_ok=True)

    # Iterate over all files in the source directory
    for filename in os.listdir(source_dir):
        if filename.endswith('.ipynb'):  # Process only .ipynb files
            source_path = os.path.join(source_dir, filename)
            dest_filename = f"practise_{filename}"
            destination_path = os.path.join(destination_dir, dest_filename)

            # Load the notebook
            with open(source_path, 'r', encoding='utf-8') as f:
                notebook = nbformat.read(f, as_version=4)

            # Clear code cells
            for cell in notebook['cells']:
                if cell['cell_type'] == 'code':
                    cell['source'] = ''  # Clear the code
                    cell['outputs'] = []  # Clear the outputs

            # Save the cleared notebook to the destination directory
            with open(destination_path, 'w', encoding='utf-8') as f:
                nbformat.write(notebook, f)

            print(f"Processed: {source_path} -> {destination_path}")

def main():
    # source = "/path/to/source/notebooks"
    # destination = "/path/to/destination/notebooks"
    print(f"Arguments passed: {sys.argv}")
    if len(sys.argv) != 3:
        print("Usage: python script.py source_dir destination_dir")
        sys.exit(1)
    clear_notebooks(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
