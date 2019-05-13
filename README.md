# Django Speech to text, Chat application
Django app to allow users to convert their speech into text and send that text as a message. This app record blobs in realtime to the server! After every 10 seconds recorded blob is converted into text and send as a message to chat.

# Commands to Setup the environment and run the server

> git clone https://github.com/ehtisham91/Django-Speech-to-text-Chat.git

> cd Django-Speech-to-text-Chat

> virtualenv venv

> source venv/bin/activate

> pip install -r requirements.txt

> python manage.py runserver


# Helpful Link
https://github.com/streamproc/MediaStreamRecorder/blob/master/demos/audio-recorder.html

I used it for recording audio in the browser as uncompressed pcm audio in .wav containers.

