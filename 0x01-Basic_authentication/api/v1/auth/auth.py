#!/usr/bin/env python3
from flask import request
'''
Model to manage the API authentication
'''

class Auth:
    '''
    manage the API authentication
    '''
    def require_auth(self, path: str, excluded_paths: list[str]) -> bool:
        '''
        check if authentication is required to access path
        '''
        return False
    

    def authorization_header(self, request=None) -> None:
        '''
        ''' 
        return
    

    def current_user(self, request=None) -> None:
        '''
        '''
        return
    














  
  
