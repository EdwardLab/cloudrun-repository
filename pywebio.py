import pywebio.input
from pywebio.input import *
from pywebio.output import *
from pywebio import *
from pywebio.session import *
def main():

    put_html("<h1>Hello BINPython CloudRun</h1>")
if __name__ == '__main__':
    start_server(main, debug=True, port=5100)
    set_env(title=f"CloudRun",output_max_width="100%", auto_scroll_bottom=True)
    pywebio.session.hold()
