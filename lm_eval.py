#!/home/jiz22029/miniconda3/envs/lm_eval/bin/python
# -*- coding: utf-8 -*-
import re
import sys
from lm_eval.__main__ import cli_evaluate
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    # print("############### sys argv: ###############")
    # print(re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0]))
    # exit()
    sys.exit(cli_evaluate())
