"""
Copyright 2025 Everett M

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the “Software”),
to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from flask import Flask, request, render_template_string, url_for
from translate import convertcodon

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def adder_page():
    result = None

    if request.method == "POST":
        code = request.form.get("code")
        if code:
            result = convertcodon(code)

    html = f'''
        <html>
            <head>
                <title>Codon Converter</title>
                <link rel="icon" href="{url_for('static', filename='favicon.ico')}" type="image/x-icon">
                <style>
                    .footer {{
                        position: static; /* Default position */
                        width: 99%;
                        background-color: #f1f1f1;
                        padding: 10px;
                        color: #333;
                        text-align: center;
                        font-size: 14px;
                        margin-top: 20px; /* Add some space from content */
                    }}
                </style>
            </head>
            <body>
                <h1>Codon Converter</h1>

                <p>Enter your tRNA sequence (Uppercase, triplets separated by spaces): </p>
                <form method="post" action=".">
                    <p><input name="code" /></p>
                    <p><input type="submit" value="Convert!" /></p>
                </form>

                {f"<p>The result is: {result}</p>" if result else ""}

                <div class="footer">

                    <p>Copyright 2025 Everett M

                    <p>Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

                    <p>The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

                    <p>THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</div>
            </body>

        </html>
    '''
    return render_template_string(html)

if __name__ == "__main__":
    app.run()
