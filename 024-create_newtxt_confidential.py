from distutils.command.build_scripts import first_line_re
import sys

first_txt=open(sys.argv[1], "r")

linhas = first_txt.readlines()