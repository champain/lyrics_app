# The Lyrics App

This is a demo app designed to demonstrate a basic REST API that does it's level
best to determine the parts of speech in popular song lyrics. Specifically it
has three paths:

* GET `/verbs/<artist>/<title>` => verbs [json]
* GET `/adjectives/<artist>/<title>` => adjectives [json]
* GET `/healthz` => response code 200

## Using this app

Just use `curl`!

```bash
curl 'http://127.0.0.1:8080/adjectives/Prince/Little%20Red%20Corvette'
```

```bash
curl 'http://127.0.0.1:8080/verb/Prince/Little%20Red%20Corvette'
```

And you're off to the races!
