# webdiff

Web diff on Python Flask & Pygments.

Modified from: https://github.com/wagoodman/diff2HtmlCompare

Bugs Fixed:
- allow empty line in lexer;
- empty code when file does not exist;
- add anchor to line no link

## Sample
```
make start
```
visit: http://localhost:3000/?original=sample/original/hello.c&modified=sample/modified/hello.c
