#!/usr/bin/env python
import sys
from hearthstone.enums import *
from utils import *
from fireplace import cards
#from fireplace.debug_utilities import printClasses, printClasses_BG24, parse, parseDeck, printPool
from fireplace.config import Config

sys.path.append("..")




####################################################################

### HEARTHSTONE=3

def battleground_main():
	from fireplace.battlegrounds.BG_utils import  BG_main
	for repeat in range(50):
		BG=BG_main()
		BG.BG_main()



if __name__ == "__main__":
	battleground_main()
