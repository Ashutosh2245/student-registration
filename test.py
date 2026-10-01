import os

assert os.path.exists("index.html"), "index.html does not exist"

with open("index.html", "r", encoding="utf-8") as file:
    html = file.read().lower()

required_elements = [
    "<html",
    "<head",
    "<body",
    "<form",
    "<input",
    "<select",
    "<button",
    "<h1"
]

for element in required_elements:
    assert element in html, f"Missing element: {element}"

print("All HTML tests passed!")