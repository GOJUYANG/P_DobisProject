import os
import sys

if __name__ == '__main__':
    name = 'main_frame'
    # name = 'equipment'
    os.system(f'python -m PyQt5.uic.pyuic -x {name}.ui -o {name}.py')
