from flask import Flask, request, Response
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route("/generate_qr", methods=["GET"])
def generate_qr():
    # Get the URL from the query string
    url = request.args.get("url")
    # Generate QR code from URL
    img = qrcode.make(url)
    # Save QR code as PNG file
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    # Return QR code as response
    return Response(img_io.getvalue(), content_type='image/png')

if __name__ == "__main__":
    app.run()
