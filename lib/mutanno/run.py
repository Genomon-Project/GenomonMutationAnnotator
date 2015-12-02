#! /usr/bin/env python

import sys
import os
import math
import argparse
import logging
from annotator import annotator


#
# Main
#
def run_annotate(arg):

    inh_snv = annotator(arg.tabix_db, arg.header, arg.column_size)
    inh_snv.annotate(arg.target_mutation_file, arg.output)


