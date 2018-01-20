# Brython Related Notes

## Laying out html and python

Include the brython js script. Also include brython_stdlib, if u are import python modules.

```
    <head>
        ...
        <script type="text/javascript" src="brython.js"></script>
        <script type="text/javascript" src="brython_stdlib.js"></script>
        ...
    <\head>
```

In the html body, add this at beginning and before the end tag:

```
    <body onLoad="brython(2)">
        ...
        ...
        ...
        <script type="text/python">
PLACEHOLDER_APP_PY <- your python content.
        </script>
    </body>
```

Since python code is not html, you want to maintain them separately,
do the PLACEHOLDER_APP_PY as shows above, and replace it later with
sed like this:

```
	sed -e '/PLACEHOLDER_APP_PY/r app.py' -e 's/PLACEHOLDER_APP_PY//' page.html > index.html
```

## Brython modules and classes

Not bad.. will be quick to read
Reading: https://brython.info/static_doc/en/dom_api.html

* browser.document --> is the whole document
* browser.window   --> is the window
* browser.window   --> is the window

You access any element using
* document.getElementById()
* docuemnt["idOfElement"]
* document.createElement('htmlType') -- returns the created element
* document.appendChild(element)

## Access a element

document['id'].text = "some_text - notice the string value. stringize ints"
your_str_value = document['id'].text
your_number_input = int(document['id'].value)

