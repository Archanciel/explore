from configobj import ConfigObj

filename = 'test2.ini'
config = ConfigObj(filename)
config['section1'] = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'
    }
config['section1'].comments = {
    'key1': ['Comment before keyword1',],
    'key2': [],
    'key3': []
    }
config['section1'].inline_comments = {
    'key1': 'Inline comment 1',
    'key2': 'Inline comment 2',
    'key3': ''
    }
config.write()