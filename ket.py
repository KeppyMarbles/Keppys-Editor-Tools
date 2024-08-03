import os
import subprocess
import json
import traceback
import socket
import threading
import time
import datetime

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
    print(f"Error: couldn't find PQ folder {pq_directory}. Try setting it prefs?")
    _ = input()
    
if not os.path.isfile(csx3dif):
    print("Error: couldn't find csx3dif.exe next to script file.")
    _ = input()
    
csxFiles = []
    
class CSX(object):
    def __init__(self, filepath):
        self.filepath = filepath
        self.fullpath = os.path.join(pq_directory, filepath)
        self.cached_stamp = os.stat(self.fullpath).st_mtime
    
    def isModified(self):
        stamp = os.stat(self.fullpath).st_mtime
        flag = stamp != self.cached_stamp
        if flag:
            self.cached_stamp = stamp
        return flag
        
def watch_csx(conn):
    csxFiles.clear()
    while True:
        try:
            conn.send(b'')
        except Exception:
            time_print("Stopping old csx watcher")
            return
    
        for csx in csxFiles:
            if csx.isModified():
                send_message(conn, f"Modified: {str(csx.filepath)}\n")
            
        time.sleep(0.25)
        
def get_csx(filepath):
    for csx in csxFiles:
        if csx.filepath == filepath:
            return csx
    return False

def recv_command(conn):
    while True:
        time_print("Awaiting command...")
        
        try:
            data = conn.recv(512)
            if not data:
                raise Exception
                
        except Exception:
            time_print("Stopping reciever\n")
            conn.close()
            start_server()
            return
        
        try:
            query = data.decode().split("|")
            
            action = query[0]
            filepath = query[1]
            
            time_print(f"Got command {action} with argument \"{filepath}\"")
            
            if action == "checkConnection":
                message = "Success: connected with Python script"
            
            elif action == "convertCSX":
                args = [csx3dif, os.path.join(pq_directory, filepath)]
                if csx3dif_args != ['']:
                    args = args + csx3dif_args
                    
                subprocess.run(args)
                message = "Success: created new dif"
                
            elif action == "watchCSX":
                if get_csx(filepath):
                    message = f"Note: {filepath} was already in the watch list"
                else:     
                    csxFiles.append(CSX(filepath))
                    message = f"Completed: Added {filepath} to the watch list"
                
            elif action == "stopWatchingCSX":
                csx = get_csx(filepath)
                if csx:
                    csxFiles.remove(csx)
                    message = f"Completed: Removed {filepath} from the watch list"
                else:
                    message = f"Note: {filepath} was not on the watch list"
                    
            elif action == "stopWatchingAll":
                message = f"Completed: Removed {len(csxFiles)} csx files from the watch list"
                csxFiles.clear()
               
            else:
                message = f"Error: unknown action {action}"
                
        except Exception as error:
            time_print(traceback.format_exc())
            message = f"Error: {str(type(error))}: {str(error)}"
            
        finally:
            send_message(conn, message)
            
def send_message(conn, message):
    time_print(f"Sending message: \"{message}\"")
    message += "\n"
    conn.sendall(message.encode())

def time_print(text):
    now = datetime.datetime.now().strftime('%H:%M:%S.%f')
    print(f"[{now}] {text}")

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", port))
        s.settimeout(None)
        
        print("Keppy's Editor Tools v0.2")
        time_print(f"Listening for PQ on port {str(port)}")
        
        s.listen()
        conn, addr = s.accept()
        
        time_print("Recieved connection from PQ")
        
        recv_thread = threading.Thread(target=recv_command, args=[conn])
        watch_thread = threading.Thread(target=watch_csx, args=[conn])
        
        time_print("Starting new reciever")
        recv_thread.start()
        
        time_print("Starting new csx watcher")
        watch_thread.start()

start_server()
