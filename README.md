# webdiff(Python Flask Application)

Web diff on Python Flask & Pygments.

Modified from: https://github.com/wagoodman/diff2HtmlCompare

## Bugs Fixed:
- upgrade to the latest pygments;
- allow empty line in lexer;
- empty code when file does not exist;

## Features Added:
- add anchor to line no link;
- apply macro define header file(.h) for original & modified code: the macro in code will show tooltip in diff code view;

## Sample code
```
make start
```
visit: http://localhost:3000/?original=sample/original/hello.c&modified=sample/modified/hello.c
