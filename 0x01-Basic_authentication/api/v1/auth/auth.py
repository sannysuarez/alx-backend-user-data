#!/usr/bin/env python3
from flask import request
from typing import List, TypeVar
'''
Model to manage the API authenticatio
'''
class Auth:
    '''
    manage the API authentication
    '''
    def require_auth(self, path: str, excluded_paths: list[str]) -> bool:
        '''
        check if authentication is required to access path
        '''
         # be slash tolerant: path=/api/v1/status and path=/api/v1/status/
        if path and not path.endwith('/'):
            path = path + '/'   
        # Return True if path is known
        if not path or path not in excluded_paths:
            return True
        # Return True if excluded_path is None or empty
        if not excluded_paths or excluded_paths == []:
            return True

        # Return False if path is in excluded_paths
        if path in excluded_paths:
            return False
        # You can assume excluded_paths contains string path alway sending by a /
        return False
    

    def authorization_header(self, request=None) -> str:
        '''
        ''' 
        return
    

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        '''
        return
    














  
  
