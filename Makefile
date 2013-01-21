# Some helpful utility commands.

build:
	pelican-themes -r pydanny
	pelican-themes -i ../pelican-themes/pydanny
	pelican . -o . -s settings.py