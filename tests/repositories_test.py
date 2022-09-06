'''
Data Object Tests
'''

from assertpy import assert_that
from src.dataobjects.repositories import GitRepository
import os
    
def test_git_repository():
    '''
    Tests Instantiating GitRepository.
    '''
    
    repo = GitRepository('./output/sample', force=True)
    assert_that(repo.gitdir).is_equal_to_ignoring_case('./output/sample/.git')
    assert_that(repo.worktree).is_equal_to_ignoring_case('./output/sample')
    
    if os.path.exists('./output/sample'):
        os.removedirs('./output/sample')    
    
