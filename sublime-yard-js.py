import sublime_plugin


def insert_line(view, content):
  view.run_command('insert_snippet', {'contents': '\n'+content})


class AddCommentLine(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_line(self.view, "* ")

class AddFirstCommentLine(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_line(self.view, " * ")
