from flask import Flask, render_template, request, redirect

app = Flask(__name__)


expenses = []    
total = 0         

@app.route("/")
def home():
    return render_template("index.html", expenses=expenses, total=total)


@app.route("/add", methods=["POST"])
def add_expense():
    global total

    name = request.form.get("name", "").strip()
    amount_text = request.form.get("amount", "").strip()

   
    if name == "" or amount_text == "":
        return redirect("/")

    try:
        amount = float(amount_text)
    except ValueError:
        return redirect("/")

    if amount < 0:
        return redirect("/")

   
    expenses.append({"name": name, "amount": amount})
    total = total + amount

    return redirect("/")


@app.route("/delete/<int:index>")
def delete_expense(index):
    global total

    if 0 <= index < len(expenses):
        total = total - expenses[index]["amount"]
        expenses.pop(index)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)