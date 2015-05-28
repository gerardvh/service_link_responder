# HipChat Incident Webhook

This is a Python/Django web app that listens for incident numbers mentioned in HipChat and returns a response to the room with useful information about that incident.

### ToDo's

- Add configuration options to select what is returned to the room.
- Add listener functionality for KBase documents as well and add links / titles to the room.
- Add tests to keep from regressing during feature upgrades.
- Remember requests and keep them in the database. (For debugging and interest.)

