'''
Repository Class Objects
'''

import configparser
import os

from helpers import repo_helpers

class GitRepository(object):
    '''
    A Git Repository
    '''

    worktree = None
    gitdir = None
    conf = None

    def __init__(self, path, force=False):
        '''
        Constructor
        '''

        self.worktree = path
        self.gitdir = os.path.join(path, '.git')

        if not (force or os.path.isdir(self.gitdir)):
            raise Exception("Not a Git repository %s" % path)

        # Read configuration file in .git/config
        conf = configparser.ConfigParser()
        cf = repo_helpers.repo_file(self, "config")

        if cf and os.path.exists(cf):
            conf.read([cf])
        elif not force:
            raise Exception("Configuration file missing")

        if not force:
            vers = int(conf.get("core", "repositoryformatversion"))
            if vers != 0:
                raise Exception(
                    "Unsupported repositoryformatversion %s" % vers)


class GitObject (object):
    '''
    Abstract Class for Git Objects
    '''

    repo = None

    def __init__(self, repo, data=None):
        self.repo = repo

        if data != None:
            self.deserialize(data)

    def serialize(self):
        '''
        This function MUST be implemented by subclasses.
        It must read the object's contents from self.data, a byte string, and do
        whatever it takes to convert it into a meaningful representation.  
        What exactly that means depend on each subclass.
        '''
        raise Exception("Unimplemented!")

    def deserialize(self, data):
        raise Exception("Unimplemented!")
