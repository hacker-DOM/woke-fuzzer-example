import woke
import logging
import traceback
import sys
from typing import List, DefaultDict, Dict, Tuple, Set
from random import choice, randint

import woke.testing.campaign
from woke.testing.campaign import Campaign
from woke.testing.contract import dev_interface, Address, Wei
from woke.testing.decorators import flow, invariant, weight
from woke.testing.random import *
from woke.testing.utils import snapshot_and_revert, connect

from pytypes.src.Counter import Counter

log = logging.getLogger(__name__)

class Test:
    c: Counter
    num: int = 0
    

    def __init__(self):
        self.c = Counter.deploy()

    @flow
    def flow_inc(self):
        log.info(" Incrementing number")
        self.c.increment()
        self.num += 1


    @flow
    @weight(50)
    def flow_set(self):
        num = randint(0, 2**256-1)
        log.info(f"Setting number to {num}")
        self.c.setNumber(num)
        self.num = num
        
    @invariant
    def invariant_number(self):
        assert self.num == self.c.number()


@connect(dev_interface, "http://localhost:8545")
def test_counter():
    try:
        dev_interface.console_logs_callback = lambda tx_hash, logs: print(f"{tx_hash}: {logs}")
        woke.testing.campaign.logger.setLevel(logging.INFO)
        log.setLevel(logging.INFO)
        log.addHandler(logging.StreamHandler(sys.stdout))
        campaign = Campaign(Test)
        campaign.run(20, 200)
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print('An error occurred on line {} in statement {}'.format(line, text))

test_counter()