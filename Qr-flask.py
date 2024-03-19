from flask import Flask, render_template, request, send_file
import qrcode

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("QRcode.html")

@app.route("/", methods=["POST"])
def generate_qrcode():
  url = request.form.get("url")
  if not url:
    return render_template("QRcode.html", error="يجب إدخال رابط URL")

  qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L)
  qr.add_data(url)
  qr.make()
  img = qr.make_image()

  # تخزين الصورة مؤقتًا
  filename = "qr_code.png"
  img.save(filename)

  return send_file("qr_code.png", mimetype="image/png", as_attachment=True)
  return render_template("QRcode.html", qr_code=filename)

if __name__ == "__main__":
  app.run(debug=True)
