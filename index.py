import time
from flask import Flask, render_template

import sync_methods as s
import async_methods as a

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sync-loading')
def sync_loading():
    markup = "<h1>sync-loading</h1><a href='/'>Return</a><br><br>"
    start = time.perf_counter()
    urls = s.get_multiple_images(10)
    end = time.perf_counter()
    markup += f"Time taken: {end - start}<br><br>"
    for url in urls:
        markup += f'<img src="{url}"></img><br><br>'

    return markup


@app.route('/async-loading')
async def async_loading():
    markup = "<h1>async-loading</h1><a href='/'>Return</a><br><br>"
    start = time.perf_counter()
    urls = await a.get_multiple_images(10)
    end = time.perf_counter()
    markup += f"Time taken: {end - start}<br><br>"
    for url in urls:
        markup += f'<img src="{url}"></img><br><br>'

    return markup


if __name__ == '__main__':
    app.run(debug=True)
