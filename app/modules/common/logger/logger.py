import logging

class Logger:
    
   def __init__(self, name, level):
       self.level = level
       self.name = name
              
       logging.basicConfig(level=logging.INFO)
       self.log = logging.getLogger( name )
