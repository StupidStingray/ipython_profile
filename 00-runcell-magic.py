from IPython.core.magic import register_line_magic
import re

@register_line_magic
def runcell(line):
    """
    usage: %runcell <cell title> <filename>
    runs cell (marked by '#%% <title>') inside <filename>.
    """
    parts = line.split(maxsplit = 1)
    if len(parts) != 2:
        print("Usage: %runcell <cell_title> <filename>")
        return

    cell_title, filename = parts
    with open(filename, 'r', encoding = 'utf-8') as f:
        code = f.read()

    cells = re.split(r"(?m)^#%%.*$", code)
    headers = re.findall(r"(?m)^#%%\s*(.*)$", code)

    if cell_title not in headers:
        print(f"Cell '{cell_title}' not found.")
        return

    idx = headers.index(cell_title)
    exec(cells[idx+1], globals())
