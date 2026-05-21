import os
import subprocess
import sys

def execute_notebook():
    print("Executing Jupyter notebook...")
    # Paths
    notebook_path = os.path.join("notebooks", "retail_sales_analysis.ipynb")
    
    # We can use nbconvert to execute the notebook in place
    cmd = [
        sys.executable, 
        "-m", "jupyter", 
        "nbconvert", 
        "--to", "notebook", 
        "--execute", 
        "--inplace", 
        notebook_path
    ]
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("Notebook executed successfully!")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error executing notebook:", e)
        print("Stdout:", e.stdout)
        print("Stderr:", e.stderr)
        sys.exit(1)

if __name__ == "__main__":
    execute_notebook()
