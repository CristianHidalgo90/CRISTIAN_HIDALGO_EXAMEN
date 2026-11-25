from errno import EILSEQ

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ejercicio1',methods=['GET','POST'])
def ejercicio1():
        if request.method == 'POST':
            nombre=(request.form['nombre'])
            edad=int(request.form['edad'])
            cantidad=int(request.form['cantidad'])
            if edad>=18 and edad<=30:
                total=cantidad*9000
                descuento=total*0.15
                total_condesc=total-descuento
            elif edad>30:
                total=cantidad*9000
                descuento = total*0.25
                total_condesc = total-descuento
            else:
                total=cantidad*9000
                descuento=0
                total_condesc=total
            return render_template('ejercicio1.html',nombre=nombre,edad=edad,cantidad=cantidad,total=total,descuento=descuento,total_condesc=total_condesc)
        return render_template('ejercicio1.html')

@app.route('/ejercicio2',methods=['GET','POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario=(request.form['usuario'])
        pswrd=(request.form['pswrd'])
        if usuario=='juan' and pswrd=='admin':
            mensaje="Bienvenido administrador Juan"
        elif usuario=='pepe' and pswrd=='user':
            mensaje="Bienvenido usuario Pepe"
        else:
            mensaje="Usuario o contraseña incorrectos"
        return render_template('ejercicio2.html',usuario=usuario,pswrd=pswrd,mensaje=mensaje)
    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)