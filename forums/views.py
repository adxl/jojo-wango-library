from django.shortcuts import render
from forums.models import Forum, Message
from forums.forms import MessageForm
from books.models import Book

def index(request, id):
    forum_channel = Forum.objects.get(id=id)
    book_id = forum_channel.book_id
    book = Book.objects.get(id=book_id)
    messages: list[Message] = Message.objects.filter(forum_id=forum_channel.id).order_by("created_at")

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.instance.forum_id = forum_channel.id
            form.save()
            return render(
        request,
        "forums/index.html",
        {"form": form, "forum_channel": forum_channel, "book": book, "messages_forum": messages},
    )

    else:
        form = MessageForm()

    return render(
        request,
        "forums/index.html",
        {"form": form, "forum_channel": forum_channel, "book": book, "messages_forum": messages},
    )