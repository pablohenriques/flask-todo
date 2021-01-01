from flask import render_template, request, redirect, flash
from app import app, db
from app.models import Todo


@app.route("/")
def index():
    tarefas = Todo.query.order_by(Todo.date_created).all()
    return render_template("home.html", tarefas=tarefas)


@app.route("/adicionar-tarefa", methods=["GET", "POST"])
def adicionar_tarefa():
    conteudo = request.form["conteudo_tarefa"]
    nova_tarefa = Todo(content=conteudo)

    try:
        db.session.add(nova_tarefa)
        db.session.commit()
        flash("Tarefa inserida com sucesso.", "success")
    except Exception:
        flash("Erro. Tarefa não inserida.", "danger")

    return redirect("/")


@app.route("/atualizar-tarefa/<int:id>", methods=["GET", "POST"])
def atualizar_tarefa(id):
    tarefa = Todo.query.get_or_404(id)

    if request.method == "POST":
        tarefa.content = request.form["conteudo_tarefa"]

        try:
            db.session.commit()
            flash("Tarefa atulizada com sucesso.", "success")
        except Exception:
            flash("Erro. Tarefa não atualizada.", "danger")

        return redirect("/")

    return render_template("task-update.html", tarefa=tarefa)


@app.route("/deletar-tarefa/<int:id>")
def deletar_tarefa(id):
    tarefa = Todo.query.get_or_404(id)

    try:
        db.session.delete(tarefa)
        db.session.commit()
        flash("Tarefa deletada com sucesso.", "success")

    except Exception:
        flash("Erro. Tarefa não atualizada.", "danger")

    return redirect("/")



