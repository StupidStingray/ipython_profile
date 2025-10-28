import re

def runcell(cell_title, filename):

    with open(filename, 'r', encoding ='utf-8') as f:
        code = f.read()

        cells = re.split(r"(?m)^#%%.*$", code)
        headers = re.findall(r"(?m)^#%%\s*(.*)$", code)

        if cell_title not in headers:
            print(f"Cell '{cell_title}' not found.")
            return
        idx = headers.index(cell_title)
        exec(cells[idx+1], globals())
