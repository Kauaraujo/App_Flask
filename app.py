from flask import Flask, render_template, request

app = Flask(__name__)

frutas = []
registros = []

@app.route('/', methods=["GET", "POST"])
def principal():
	#frutas = ['Banana', 'Maça', 'Laranja', 'Uva', 'Melancia']
	if request.method == "POST":
		if request.form.get("fruta"):
			frutas.append(request.form.get("fruta"))
	return render_template("index.html", frutas=frutas)


@app.route('/sobre', methods=["GET", "POST"])
def sobre():
	#notas = {"Kaue":10, "Ana":9, "Maju":8, "Manu":7}
	if request.method == "POST":
		if request.form.get("aluno") and request.form.get("nota"):
			registros.append({"aluno": request.form.get("aluno"), "nota": request.form.get("nota")})
	return render_template("sobre.html", registros=registros)


@app.route('/login', methods=["GET", "POST"])
def login():
	return render_template("login.html")

app.run(debug=True)