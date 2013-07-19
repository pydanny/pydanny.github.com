import os

TARGET = "../blogblook/docs/"

INDEX = """
.. Inside the Head of Pydanny: E-book Edition

Inside the Head of Pydanny: E-book Edition
========================================

Inside the Head of Pydanny: E-book Edition
1st Edition
by Daniel Greenfeld

Copyright  2013 Daniel Greenfeld and Cartwheel Web.

All rights reserved. This book may not be reproduced in any form, in whole or 
in part, without written permission from the authors, except in the case of
brief quotations embodied in articles or reviews.

Limit of Liability and Disclaimer of Warranty: The author has used his best
efforts in preparing this book, and the information provided herein ``as is.''
The information provided is sold without warranty, either express or implied.
Neither the author nor Cartwheel Web will be held liable for any damages to be
caused either directly or indirectly by the contents of this book.

Trademarks: Rather than indicating every occurrence of a trademarked name as
such, this book uses the names only in an editorial fashion and to the benefit
of the trademark owner with no intention of infringement of the trademark.

First printing, July 2013


Table of Contents:

.. toctree::
   :maxdepth: 2
   
   introduction
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
        


    