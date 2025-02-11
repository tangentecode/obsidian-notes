# Methods

- Flask can utilize different [http](contents-http.md) [methods](computer-science/docs/basics/http/methods.md)
- For example use `POST` to hide data in the  the [url](url.md):
```python
@app.route("/greet", methods=["POST"])
def greet():
    return render_template("greet.html", name=request.form.get("name", "world"))
```


- Define one [[rout]]