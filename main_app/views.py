from django.shortcuts import render, redirect
from django.urls import reverse
from .utils import TextFilesMerger

def merge_files(request):
    if request.method == 'POST':
        merger = TextFilesMerger()
        files = request.FILES.getlist('files')
        rel_paths = request.POST.getlist('relPaths')  # Make sure this matches the client-side FormData field

        merged_content = merger.merge(files, rel_paths)

        request.session['merged_content'] = merged_content
        return redirect('merge_results')
    else:
        return redirect('index')


# Adding a view to display merge results
def display_merge_results(request):
    merged_content = request.session.get('merged_content', '')
    print("Merged Content:", merged_content)  # Debugging statement
    return render(request, 'merge_results.html', {'merged_content': merged_content})


def index(request):
    return render(request, 'index.html')