import requests
import pytest
import os, sys
sys.path.append(os.getcwd())
from utils.mysql import query
from utils.filetools import read_file
from utils.exceltools import read_excel
