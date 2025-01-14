**There are three types of CSS:**



1. Inline CSS
    - Directly embedded in [HTML](contents-html.md)
    - No link required
    - Used like [Attributes](common-tags.md)
    - Example:
```html
 <p font-size=large>This is a paragraph</p>
```

2. `<style>` [Tag](common-tags.md)
	- Also directly embedded and no `<link>` tag
	- Example:
	
```html
<style>
	.paragraph-class {
	    font-size: large;
	}
</style>

<p class=paragraph-class>This is a large paragraph</p>
```

3. External file:
	Like in [this](link-css.md) file


### The best way to embed CSS is the 3 way