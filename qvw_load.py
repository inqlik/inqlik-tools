# -*- encoding: UTF-8 -*-
import sublime
import sublime_plugin
import os
import re
class QlikviewReloadCommand(sublime_plugin.WindowCommand):
  def run(self, commandVariant=None):
    file_regex = "^>* Parse error. File: \"(...*?)\", line: ([0-9]*)"
    scriptPath = "%s\\Inqlik-Tools\\bin\\inqlik.bat" % sublime.packages_path()
    view = self.window.active_view()
    fileName = view.file_name() 
    if commandVariant is None:
      self.window.run_command("exec", { "file_regex": file_regex, "cmd": [scriptPath,"qvs", "--command=check_and_reload",fileName]})
    else:
      self.window.run_command("exec", { "file_regex": file_regex, "cmd": [scriptPath,"qvs", "--command=open",fileName]})

