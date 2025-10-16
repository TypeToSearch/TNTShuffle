import webview
from js_interface import JsInterface

HTML_DIR = "../web/"


if __name__ == "__main__":
    api = JsInterface()
    webview.create_window(
        'TNT Shuffler',
        HTML_DIR+"index.html",
        js_api=api,
        min_size=(600, 450)
    )
    webview.start()

