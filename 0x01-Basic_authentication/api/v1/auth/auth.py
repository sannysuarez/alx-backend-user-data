#!/usr/bin/env python3
from flask import request
from typing import List, TypeVar
'''
Model to manage the API authentication
'''

class Auth:
    '''
    manage the API authentication
    '''

def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
    '''
    check if authentication is required to access path
    '''
    return False

def authorization_header(self, request=None) -> str:
    '''
    '''
    return

def current_user(self, request=None) -> TypeVar('User'):
    '''
    '''
    return

if __name__=='__main__':
    a = Auth()

    print(a.require_auth("/api/v1/status/", ["/api/v1/status"]))
    print(a.authorization_header())
    print(a.current_user())








  
  
