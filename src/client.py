'''
Pythonn library for implementing Git like system.
'''

import argparse
import collections
import configparser
import hashlib
import os
import re
import sys
import zlib

from helpers.repo_helpers import RepoHelper

# Create an Argument Parser
argparser = argparse.ArgumentParser(description='Git Command Parser')

# Add Sub parsers
subparsers = argparser.add_subparsers(title='Commands', dest='command')
subparsers.required = True

# Adds the Init Command
argsp = subparsers.add_parser('init', help='Initializes a new empty Repository')
argsp.add_argument("path",
                   metavar="directory",
                   nargs="?",
                   default=".",
                   help="Where to create the repository.")

def cmd_init(args):
    '''
    Initializes the Empty Repository
    '''
    RepoHelper.repo_create(args.path)
    


def main(argv=sys.argv[1:]):
    '''
    Main execution for performing Git Like operations.
    '''
    args = argparser.parse_args(argv)

    if args.command == "add":
        cmd_add(args)
    elif args.command == "cat-file":
        cmd_cat_file(args)
    elif args.command == "checkout":
        cmd_checkout(args)
    elif args.command == "commit":
        cmd_commit(args)
    elif args.command == "hash-object":
        cmd_hash_object(args)
    elif args.command == "init":
        cmd_init(args)
    elif args.command == "log":
        cmd_log(args)
    elif args.command == "ls-tree":
        cmd_ls_tree(args)
    elif args.command == "merge":
        cmd_merge(args)
    elif args.command == "rebase":
        cmd_rebase(args)
    elif args.command == "rev-parse":
        cmd_rev_parse(args)
    elif args.command == "rm":
        cmd_rm(args)
    elif args.command == "show-ref":
        cmd_show_ref(args)
    elif args.command == "tag":
        cmd_tag(args)




if __name__ == '__main__':
    '''
    Executes the main method when the script is called.
    '''
    main()