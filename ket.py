from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import os
import subprocess
import json
import traceback

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))).replace(os.sep, '/') + '/'

with open("prefs.json", 'r') as openfile:
    prefs = json.load(openfile)

port = prefs["port"]
csx3dif_args = prefs["csx3dif_args"].split(' ')
pq_directory = prefs["pq_directory"]
csx3dif = __location__ + "csx3dif.exe"

if pq_directory == "":
    pq_directory = __location__[:2] + "/Users/" + os.environ.get('USERNAME') + "/AppData/Roaming/PlatinumQuest"

if not os.path.exists(pq_directory):
    print("Error: couldn't find PQ folder", pq_directory + ". Try setting it prefs?")
    _ = input()
    
if not os.path.isfile(csx3dif):
    print("Error: couldn't find csx3dif.exe next to script file.")
    _ = input()
    
class ketHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            query = parse_qs(self.path[2:])
            arg = [str(i) for i in query["args"]]
            action = str(query["action"][0])
            print("Got request from PQ:", action)
            
            if action == "checkConnection":
                self.send_header("Success", "connected with Python script")
            
            elif action == "convertCSX":
                args = [csx3dif, os.path.join(pq_directory, arg[0])]
                if csx3dif_args != ['']:
                    args = args + csx3dif_args
                    
                subprocess.run(args)
                self.send_header("Success", "created new dif")
            
        except Exception as error:
            print(traceback.format_exc())
            self.send_header("Error", str(type(error)) + ": " +  str(error))
        
        self.end_headers()
        
httpd = HTTPServer(('localhost', port), ketHandler)

print("Keppy's Editor Tools v0.1")
print("Listening for PQ on port " + str(port))
httpd.serve_forever()
