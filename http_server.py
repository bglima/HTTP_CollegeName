# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 13:41:20 2018

@author: bglim
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import urllib
from data_handler import load_data, save_data

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Header
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        # Load from CSV
        names = load_data()
        for name in names:
            # Send each name
            self.wfile.write(bytes(name, 'utf-8'))
            if name != names[-1]: self.wfile.write(bytes(',', 'utf-8'))

    def do_POST(self):
        # Header
        self.send_response(200)
        self.end_headers()
        
        # Extract data from request
        content_len = int(self.headers['Content-Length'])
        data = self.rfile.read(content_len).decode('utf-8')
        # Extract dictionary with params
        data = urllib.parse.parse_qs(data)
        print('[INFO] Data decoded: ', data)     
        # Extract college name, the param with key 'name'
        new_name = str(data['name'][0])
        
        # Load database
        names = load_data()
        # Check if name already exists in database
        if new_name in names:
            self.wfile.write(bytes('[ERR] This name already exists in database', "utf-8"))
        # If not exists, save new name into database
        else:
            names.append(new_name)
            save_data(names) # Sort and save
            self.wfile.write(bytes('[INFO] Added {} to database'.format(new_name), "utf-8"))
    
    def do_DELETE(self):
        self.send_response(200)
        self.end_headers()
        # Extract data from request
        content_len = int(self.headers['Content-Length'])
        data = self.rfile.read(content_len).decode('utf-8')
        data = urllib.parse.parse_qs(data)
        college_name = str(data['name'][0])
        # Search for this name into the database
        # Load database
        names = load_data()
        # Check if name already exists in database
        if college_name in names:
            names.remove(college_name)
            self.wfile.write(bytes('[INFO] Deleting name in database', "utf-8"))
            save_data(names) # Sort and save
        # If not exists, return an error
        else:
            self.wfile.write(bytes('[ERR] {} was not found in database'.format(college_name), "utf-8"))

    def do_PUT(self):
        self.send_response(200)
        self.end_headers()
        # Extract data from request
        content_len = int(self.headers['Content-Length'])
        data = self.rfile.read(content_len).decode('utf-8')
        # Extract dict with parameters
        data = urllib.parse.parse_qs(data)
        # Extract params from dict
        old_name = str(data['name'][0])
        new_name = str(data['new_name'][0])
        
        # Search for this name into the database
        names = load_data()
        if old_name in names:
            names.remove(old_name)
            names.append(new_name)
            self.wfile.write(bytes('[INFO] Updating name in database', "utf-8"))
            save_data(names) # Sort and save
        else:
            self.wfile.write(bytes('[ERR] {} was not found in database'.format(old_name), "utf-8"))
               
def main():
    # Declare IP and port
    hostName = "localhost"
    hostPort = 8000
    
    # Instantiate server
    myServer = HTTPServer((hostName, hostPort), MyServer)
    # Show init time
    print(time.asctime(), "[INFO] Server init at {}:{} ".format(hostName, hostPort))
    # Start serving
    try:
        myServer.serve_forever()
    except KeyboardInterrupt:
        pass

    # Close server and free port
    myServer.server_close()
    print(time.asctime(), "[INFO] Server stopped at {}:{} ".format(hostName, hostPort))
    
if __name__ == '__main__':
    main()