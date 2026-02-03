from flask import Flask, render_template, request
import os
from topsis import calculate_topsis
from werkzeug.utils import secure_filename
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)


# -------- Email Function --------
def send_email(receiver, file_path):

    sender = "m83383003@gmail.com"
    password = "egtdhiwwremvyldo"

    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("Attached is your TOPSIS result.")

    with open(file_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename=os.path.basename(file_path)
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)


# -------- Main Route --------
@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        file = request.files["file"]
        weights = request.form["weights"]
        impacts = request.form["impacts"]
        email = request.form["email"]

        if not file:
            return "File required"

        weights = list(map(float, weights.split(",")))
        impacts = impacts.split(",")

        # Validate impacts
        if any(i not in ['+', '-'] for i in impacts):
            return "Impacts must be + or -"

        filename = secure_filename(file.filename)
        upload_path = os.path.join(UPLOAD_FOLDER, filename)

        file.save(upload_path)

        result_path = os.path.join(RESULT_FOLDER, "result.csv")

        try:
            calculate_topsis(upload_path, weights, impacts, result_path)
            send_email(email, result_path)

            return "✅ Result sent to your email!"

        except Exception as e:
            return str(e)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
