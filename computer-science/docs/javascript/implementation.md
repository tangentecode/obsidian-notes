1.  Writing your **JavaScript** code inside of the `<script>` [tag](common-tags.md) (Put it inside the `<head>`)

2. Linking to an external file:

```html
<script src="script.js"></script>
```

- If `<script>` was put into the head you need to ensure that the whole document was loaded before the **JavaScript** code gets executed
- Do this with this **special** [event listener](event-handling.md):

```javascript
document.eventListener('DOMContentLoaded', function(){
	// Execute code here
});
```
