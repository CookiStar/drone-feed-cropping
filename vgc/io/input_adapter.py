from .adapter import Adapter
import threading

class InputAdapter(Adapter):
    def __init__(self, pipeline):
        self.pipeline = pipeline 
        self.thread = threading.Thread(target=self.main)

    def start(self):
        pass 

    def main(self):
        pass 