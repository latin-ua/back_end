# Latin-ua API service
## API specification
Request `POST` to `/` returns a translated text.
Request body must contain a JSON encoded object described
bellow

```json
{
  "translationMethod": "str – the code of the method",
  "text": "str - the text to translate"
}
```

Request `GET` to `/translation-methods` return a list of
translation methods.

Each translation method has the following format

```json
{
  "code": "str",
  "title": "str"
}
```
