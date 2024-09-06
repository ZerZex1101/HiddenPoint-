from flask import Flask, request, jsonify, abort, render_template_string

app = Flask(__name__)

# Define a hidden endpoint
@app.route('/hidden/flag', methods=['GET'])
def get_flag():
    user_agent = request.headers.get('User-Agent')
    if user_agent and 'curl' in user_agent:
        flag = "HACKOPS{Z0ro_1$_#3r0}"
        return jsonify({"flag": flag})
    else:
        abort(403)

# Define a public endpoint with some basic information
@app.route('/', methods=['GET'])
def index():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hidden Flag Challenge</title>
        <style>
            /* General Reset */
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            /* Body */
            body {
                font-family: 'Arial', sans-serif;
                background: #0e1a2b;
                color: #f0f4f8;
                line-height: 1.6;
                overflow: hidden; /* Hide scrollbar */
            }

            /* Canvas */
            #matrix {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: -1; /* Behind other content */
            }

            /* Container */
            .container {
                width: 80%;
                margin: auto;
                overflow: hidden;
                position: relative; /* For proper stacking context */
                z-index: 1; /* Above the matrix background */
            }

            /* Header */
            header {
                background: #002d4f;
                color: #00bfae;
                padding: 20px 0;
                text-align: center;
                border-bottom: 3px solid #00bfae;
            }

            header h1 {
                font-size: 2.5em;
            }

            header p {
                font-size: 1.2em;
            }

            /* Info Section */
            .info {
                margin: 20px 0;
                padding: 20px;
                background: #003459;
                border-radius: 8px;
            }

            .info p {
                font-size: 1.2em;
            }

            /* Footer */
            footer {
                background: #002d4f;
                color: #00bfae;
                padding: 10px 0;
                text-align: center;
                border-top: 3px solid #00bfae;
                position: fixed;
                bottom: 0;
                width: 100%;
            }
        </style>
    </head>
    <body>
        <canvas id="matrix"></canvas>
        <div class="container">
            <header>
                <h1>Welcome to the Hidden Flag Challenge!</h1>
                <p>Try to find the secret endpoint.</p>
            </header>
            <section class="info">
                <p>Explore the website and use your skills to uncover hidden secrets!</p>
            </section>
            
        </div>
        <script>
            // Matrix effect JavaScript
            const canvas = document.getElementById('matrix');
            const ctx = canvas.getContext('2d');
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;

            const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
            const fontSize = 10;
            const columns = canvas.width / fontSize;
            const drops = Array(Math.floor(columns)).fill(1);

            function drawMatrix() {
                ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                ctx.fillStyle = '#ff0000'; // Red color for matrix effect
                ctx.font = `${fontSize}px monospace`;

                for (let i = 0; i < drops.length; i++) {
                    const text = characters[Math.floor(Math.random() * characters.length)];
                    ctx.fillText(text, i * fontSize, drops[i] * fontSize);

                    if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                        drops[i] = 0;
                    }

                    drops[i]++;
                }
            }

            setInterval(drawMatrix, 33);

            // Resize canvas on window resize
            window.addEventListener('resize', () => {
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            });
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
