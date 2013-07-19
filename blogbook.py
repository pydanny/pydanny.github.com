import os

TARGET = "../blogblook/docs/"

INDEX = """
.. Inside the Head of Pydanny: E-book Edition

Inside the Head of Pydanny: E-book Edition
========================================

Table of Contents:

.. toctree::
   :maxdepth: 2
   
{{ index }}
"""

def main():
    
    index = ""

    articles = []
    for root, dirs, files in os.walk("."):
    
        if not root.startswith('./posts'):
            continue
        
        for f in [x for x in files if x.endswith("rst")]:
            path = os.path.join(root, f)
            articles.append(path)
    
    article_names = ""
    for article in articles:
        with open(article) as f:
            incoming = f.read() + "\n"
            
        if ":blogbook: True" not in incoming:
            continue
            
        for line in incoming.splitlines():
            if ":slug:" in line:
                incoming = incoming.replace(line, "")
                break
            
        incoming = incoming.replace(":blogbook: True", "")
        article_name = article.split('/')[-1]
        article_names += "   " + article_name + "\n"

        # write the article to the target
        target = os.path.join(TARGET, article_name)
        with open(target, "w") as f:
            f.write(incoming)
        
    index = INDEX.replace("{{ index }}", article_names)
    index_file = os.path.join(TARGET, "index.rst")
    with open(index_file, "w") as f:
        f.write(index)
        
        
if __name__ == "__main__":
    main()
        


    