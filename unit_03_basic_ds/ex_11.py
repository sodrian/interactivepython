import re

COMMON_TAG_RE = re.compile(r'</{0,1}([a-zA-Z]+)/{0,1}>')
SINGLE_TAG_RE = re.compile(r'<([a-zA-Z]+)/{1}>')
OPENING_TAG_RE = re.compile(r'<([a-zA-Z]+)>')
CLOSING_TAG_RE = re.compile(r'</{1}([a-zA-Z]+)>')

class Stack(object):
    def __init__(self):
        self.c = []

    def push(self, item):
        self.c.append(item)

    def pop(self):
        return self.c.pop()


class BalancedHTML(object):
    def __init__(self, html_body):
        assert isinstance(html_body, str)
        self.html = html_body
        self.c = Stack()

    def is_single_tag(self, tag):
        return bool(SINGLE_TAG_RE.match(tag))

    def is_opening_tag(self, tag):
        return bool(OPENING_TAG_RE.match(tag))

    def is_closing_tag(self, tag):
        return bool(CLOSING_TAG_RE.match(tag))

    def tags_match(self, first, second):
        return first.groups() == second.groups()

    def check(self):
        balanced = True
        for match in COMMON_TAG_RE.finditer(self.html):
            if hasattr(match, 'group'):
                print(match.group())
            if self.is_single_tag(match.group()):
                pass
            elif self.is_opening_tag(match.group()):
                self.c.push(match)
            elif self.is_closing_tag(match.group()):
                try:
                    last_match = self.c.pop()
                except IndexError:
                    balanced = False
                    break
                if self.tags_match(last_match, match):
                    pass
                else:
                    balanced = False
                    break
        return balanced

s = '''
<html>
   <head>
      <title>
         <br/>
         Example
      </title>
      </title>
   </head>
   <body>
      <h1>Hello, world</h1>
   </body>
</html>'''

h = BalancedHTML(s)
h.check()
