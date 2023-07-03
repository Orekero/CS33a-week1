from django.shortcuts import render

import markdown2 as markdown

from . import util

#convert markdown to HTML
def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content) #fix this line

def index(request):
    entries = util.list_entries()
    css_file = util.get_entry("CSS")
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
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })
    

#search function

def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        html_content = convert_md_to_html(entry_search)
        if html_content is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": entry_search,
                "content": html_content
        })
    

         