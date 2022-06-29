from django.shortcuts import render, redirect, get_object_or_404

import contacts
from .models import Contact
from .forms import ContactForm, NoteForm
from .models import Note
from django.utils import timezone


# Create your views here.
def list_contacts(request):
    contacts = Contact.objects.all()
    notes = Note.objects.filter()
    # Django ORM running SQL queries for us in the database and returning instances of the Contact model
    return render(request, "contacts/list_contacts.html",
                {"contacts": contacts, "notes": notes})


def add_contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(data=request.POST)
        
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/add_contact.html", {"form": form})


def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'GET':
        form = ContactForm(instance=contact)
    else:
        form = ContactForm(data=request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/edit_contact.html",  {
        "form": form,
        "contact": contact
    }) 
    


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect(to='list_contacts')

    return render(request, "contacts/delete_contact.html",
                {"contact": contact})

def view_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    notes = Note.objects.filter(contact = pk)
    return render(request, "contacts/view_contact.html", {"contact": contact, "notes": notes})

def add_contact_note(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'GET':
        form = NoteForm()
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            new_note = form.save()
            new_note.contact = contact
            new_note.save()
            return redirect(to='view_contact', pk=pk)
    return render(request, "contacts/note_form.html", {"contact": contact, "form": form}) 

# def delete_contact_note(request, pk):
#     note = get_object_or_404(Contact, pk=pk)
#     if request.method =="POST":
#         note.delete()
#         return redirect(to='view_contact')
#     return render(request, "contacts/view_contact.html", {"contact": contact})