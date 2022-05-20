import mkdocs_gen_files
from pathlib import Path

for py_script in Path().glob("**/*.py"): # get all .py
    if ".github" not in str(py_script): # avoid e.g. this file.
        
        filename = f"{py_script.with_suffix('.md')}"
        mk_format = str(py_script.with_suffix('')).replace("/", ".")

        with mkdocs_gen_files.open(filename, "w") as f:
            print(f"::: {mk_format}", file=f)
                
        mkdocs_gen_files.set_edit_path(filename, "gen_pages.py")
