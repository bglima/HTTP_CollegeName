# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 16:20:34 2018

@author: bglim
"""

import urllib
import urllib.request

server_url = 'http://localhost:8000'

while True:
    cmd = input('\n[INFO] Input command (ex.: GET, POST, DELETE, PUT, EXIT): ')
    
    if len(cmd)==0:
        print('[ERR] Null command is not valid. Please, enter something')
        continue
        
    # Convert command to lowercase
    cmd = cmd.lower()

    if cmd == 'exit':
        break
    elif cmd == 'get':  # Returns all college names
        try:
            with urllib.request.urlopen(server_url) as f:
                response = f.read().decode('utf-8')
                names = response.split(',')
                print('[RESP] Server returned the following names: ')
                for name in names:
                    print(name)
        except Exception as e:
            print('[ERR]', e)

    elif cmd == 'post': # Add a new college name
        name = input('[INFO] Type the college name to POST: ')
        print('[INFO] You typed: ', name)
        data = urllib.parse.urlencode({'name': name}).encode('utf-8')
        try:
            with urllib.request.urlopen(server_url, data) as f:
                response = f.read().decode('utf-8')
                print('[RESP]', response)
        except Exception as e:
            print('[ERR]', e)
            
    elif cmd == 'delete':   # Remove an existing college name
        name = input('[INFO] Type the college name to DELETE: ')
        print('[INFO] You typed: ', name)
        data = urllib.parse.urlencode({'name': name}).encode('utf-8')
        req = urllib.request.Request(server_url, data=data, method='DELETE')
        try:
            with urllib.request.urlopen(req) as f:
                response = f.read().decode('utf-8')
                print('[RESP]', response)
        except Exception as e:
            print('[ERR]', e)

    elif cmd == 'put':  # Update an existing college name
        name = input('[INFO] Type the old college name: ')
        print('[INFO] You typed: ', name)
        new_name = input('[INFO] Type the new college name: ')
        print('[INFO] You typed: ', name)
                
        data = urllib.parse.urlencode({'name': name, 'new_name': new_name}).encode('utf-8')
        req = urllib.request.Request(server_url, data=data, method='PUT')
        try:
            with urllib.request.urlopen(req) as f:
                response = f.read().decode('utf-8')
                print('[RESP]', response)
        except Exception as e:
            print('[ERR]', e)
            
