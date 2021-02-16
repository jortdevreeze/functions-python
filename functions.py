def natural_keys(text):
    '''
    Create natural keys for all items in a list.
      from: [key1, key10, key11,  ...,  key23]
      to: [key1, key2, key3, ..., key23]
      
    Args:
      text: A list containing tuples (key, value)
    '''
    def atoi(text):
        return int(text) if text.isdigit() else text
    return [ atoi(c) for c in re.split(r'(\d+)', text[0]) ]

'''
Example of how to implement the natural keys function.
'''

l = [
  ('key1', False), 
  ('key10', False), 
  ('key2', False), 
  ('key3', False), 
  ('key4', False), 
  ('key5', False)
]

<<<<<<< HEAD
l.sort(key=natural_keys)
=======
l.sort(key=natural_keys)
>>>>>>> de28e159a9666ca901825bb4defaa35a3b0bf33d
