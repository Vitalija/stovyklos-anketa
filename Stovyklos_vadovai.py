 #KOSMOSAS BE NGROK VEIKAI, j KODEL????? 
#def noriu sukurti, suteiksiku pati pavadinima
#pasiimam reikalingus irankius, flask leissukurti internetine anketa, html formatu bus render_tepmplate_string
from flask import Flask, render_template_string, request
import smtplib #leidimas siusti el,laisku
from email.mime.text import MIMEText

app = Flask(__name__) #sukuria laikina serveri per kuri eis anketa
#html tekstas forma, J
HTML_FORM = '''  
<!DOCTYPE html>
<html lang="lt">
<head>
    <meta charset="UTF-8">
    <title>Vadovo atrankos forma</title>
</head>
<body style="font-family:sans-serif;">
    <h2>Stovyklos vadovo atrankos anketa</h2>
    <form method="POST">
        <label>1. Vardas: <input type="text" name="vardas" required></label><br><br>
        <label>2. Pavardė: <input type="text" name="pavarde" required></label><br><br>
        <label>3. Telefono numeris: <input type="text" name="telefonas" required></label><br><br>
        <label>4. El. paštas: <input type="email" name="elpastas" required></label><br><br>
        <label>5. Miestas: <input type="text" name="miestas" required></label><br><br>
        <label>6. Ar reikėtų nakvynės? <input type="text" name="nakvyne" required></label><br><br>
        <label>7. Amžius: <input type="number" name="amzius" required></label><br><br>
        <label>8. Ar turi patirties stovyklų vedime? <input type="text" name="patirtis" required></label><br><br>
        <label>9. Ar turi pedagoginį išsilavinimą arba kurso pažymą? <input type="text" name="pedagogika" required></label><br><br>
        <label>10. Jei ne, ar sutinki išsilaikyti (apie 150 EUR)? <input type="text" name="sutinka_islaikyti" required></label><br><br>
        <label>11. Ar turi pažymą apie neteistumą? <input type="text" name="neteistumas" required></label><br><br>
        <label>12. Jei ne, ar išsiimtum? <input type="text" name="isims" required></label><br><br>
        <label>13. Ar turi komandą, kuri norėtų dirbti kartu? <input type="text" name="komanda" required></label><br><br>
        <label>14. Ar gali dirbti visas 10 savaičių nuo birželio vidurio? <input type="text" name="laikas" required></label><br><br>
        <label>15. Koks norimas savaitinis atlyginimas prieš mokesčius? <input type="text" name="atlyginimas" required></label><br><br>
        <label>16. Klausimai / komentarai:<br>
        <textarea name="komentarai" rows="4" cols="40" required></textarea></label><br><br>

        <input type="submit" value="Siųsti anketą">
    </form>
</body>
</html>
'''
#is cia gaunasi mano anketos puslapis http://127.0.0.1:5000 
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = "\n".join([f"{k}: {v}" for k, v in request.form.items()])
        send_email("Nauja stovyklos vadovo anketa", content)
        return "Ačiū! Jūsų anketa sėkmingai gauta."
    return render_template_string(HTML_FORM)

def send_email(subject, body):
    sender = "info@bugelendas.lt"
    password = "Vitalija81."  #matosi mano slaptazodis, reikisreikes i env perkelti faila, dar to nezinau)
    recipient = "info@bugelendas.lt"

    msg = MIMEText(body, "plain", "utf-8") #is kur siunciam laiska, kodel J toki pasirinko, galejo kita
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    try:
        with smtplib.SMTP_SSL("tamarina.serveriai.lt", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())
        print(" Laiškas išsiųstas!")
    except Exception as e:
        print(" Klaida siunčiant laišką:", e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
