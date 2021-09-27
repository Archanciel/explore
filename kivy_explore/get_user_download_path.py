from pathlib import Path
import os
downloads_path = str(Path.home() / "Downloads" / 'Audio')
downloads_path_2 = os.path.join(os.path.expanduser('~'), 'Downloads\Audio')
print(downloads_path)
print(downloads_path_2)

