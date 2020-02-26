from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse


from .models import Note
from .form import NoteForm

# Create your views here.
def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'core/notes_list.html', {'notes': notes})

def notes_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'core/notes_detail.html', {'note': note, 'pk': pk})

def notes_new(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('notes-detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'core/note_new.html', {'form': form})

def notes_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form= NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('notes-detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'core/note_edit.html', {'form': form})