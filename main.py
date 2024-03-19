from flask import Flask,render_template,send_file,request
import qrcode
project = Flask(__name__)
my_skills = [ ("Html",80),("CSS",70),("Python",60),("C++",30),("Bootstarp",10),("Flask",5),("SQLite",3) ]
@project.route("/")
def home():
    return render_template("index.html")
@project.route("/QR")
def main():
  return render_template("QRcode.html")

@project.route("/", methods=["POST"])
def generate_qrcode():
  url = request.form.get("url")
  if not url:
    return render_template("QRcode.html", error="يجب إدخال رابط URL")

  qr = qrcode.QRCode(version=5)
  qr.add_data(url)
  qr.make()
  img = qr.make_image()

  filename = "QR-Code.png"
  img.save(filename)

  return send_file(filename, mimetype="image/png", as_attachment=True)
  return render_template("QRcode.html", qr_code=filename)

@project.route("/skills")
def skills():
    return render_template("skills.html", skills = my_skills  )
if __name__  == "__main__":
    project.run(debug=True,port=443)
