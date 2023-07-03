from django.shortcuts import render

import markdown2 as markdown

from . import util

def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        markdowner.convert(content) #fix this line

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

#check if the entry exists
def entry(request, title):
    html_content = convert_md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html", {
            "error": "Error: Page not found"
        })
    else:
        return render(request, "encyclopedia/entry.html")