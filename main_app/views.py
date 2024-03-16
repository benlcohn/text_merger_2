from django.shortcuts import render, redirect
from django.urls import reverse
from .utils import TextFilesMerger

def merge_files(request):
    if request.method == 'POST':
        merger = TextFilesMerger()
        files = request.FILES.getlist('files')

        # Here, we're simplifying the merge call since your TextFilesMerger doesn't take the extra parameters
        merged_content = merger.merge(files)

        # Store merged_content in the session to make it available for the next request
        request.session['merged_content'] = merged_content

        # Redirect to a URL that will display the merged results
        return redirect('merge_results')
    else:
        # If not POST, redirect to the index view
        return redirect('index')


# Adding a view to display merge results
def display_merge_results(request):
    merged_content = request.session.get('merged_content', '')
    print("Merged Content:", merged_content)  # Debugging statement
    return render(request, 'merge_results.html', {'merged_content': merged_content})







def index(request):
    return render(request, 'index.html')