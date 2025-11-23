import sys

def handle_error(yourfault, error, fix):
    if not yourfault:
        raise BaseException (f'''
!!!!!!!!!!!!!!! BEGIN SUBMODULE ERROR !!!!!!!!!!!!!!!!
Web2Native error
==========================
/!\\ {error} /!\\
This error occurred in the Web2Native app submodule. It is not caused by your own code.
Possible fixes : {fix}
!!!!!!!!!!!!!!!! END SUBMODULE ERROR !!!!!!!!!!!!!!!!!''')
    return


try:
    import eel
except ImportError:
    handle_error(False, "Missing eel module.", "Please make sure the eel module is installed in your Python environment. You can install it using pip: pip install eel")
    sys.exit(1)

def launch(filename):
    eel.init('web')

    def close(page, sockets):
        sys.exit()

    eel.start(filename, size=(1200, 800), close_callback=close)
