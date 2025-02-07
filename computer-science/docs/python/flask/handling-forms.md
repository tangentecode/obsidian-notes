# Handling-forms

- Create a [form](forms.md) in an [HTML](contents-html.md) file and [render](html-templates.md) it:

```html
<form method="POST" action="/submit">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name">
    <button type="submit">Submit</button>
</form>
```
