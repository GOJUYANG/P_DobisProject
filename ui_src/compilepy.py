import os
import sys

if __name__ == '__main__':
    # name = 'main_frame'
    # name = 'equipment'
    # name = 'gard_name'
    # name = 'intro'
    name = 'this_is_boki_dialog'
    # name = 'main_frame(delete_button)'
    os.system(f'python -m PyQt5.uic.pyuic -x {name}.ui -o {name}.py')
    # os.system(f'python -m PyQt5.uic.pyuic -x {name}.ui -o main_frame.py')
