# take current file structure of obsidian workbook and create SUMMARY.md
# SUMMARY.md dictates the structure of gitbook

# https://github.com/GitbookIO/gitbook/blob/master/docs/pages.md

import os
def format_string(name, path):
    # create proper file linking 
    return "[" + name.split(".md")[0] + "](" + path + ")"


f = open("SUMMARY.md", "a")
f.truncate(0)

dir = os.listdir()
print(dir)

exclude = [".obsidian", ".git", "Scripts", "Templates", "node_modules", ".github", "_book"]


for folder in dir: 
    if os.path.isdir(folder) and not (folder in exclude):
        walk = os.walk(folder)
        walk_dir = [x[0] for x in walk]
        
        # path in each directory
        for path in walk_dir:
            print(path) 
            print(os.listdir(path))
            files = [x for x in os.listdir(path) if x.count(".md")] # files of current path

            # check how many / there is, which means how many tabs for each article
            backslash_count = path.count("/")
            tabs = "\t" * backslash_count

            # section
            f.write(tabs + "* " + format_string(path.split("/")[-1], path + "/" + "README.md") + "\n")

            # each article
            for file in files:
                if file.count("README.md"): # section 
                   continue
                else: # article
                    f.write(tabs + "\t" + "* " + format_string(file, path + "/" + file) + "\n")

f.write("* " + "[Tags](tags.md)")                   
f.close()