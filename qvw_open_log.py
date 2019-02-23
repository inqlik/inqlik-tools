# -*- encoding: UTF-8 -*-
import sublime
import sublime_plugin
import os
import re
class QlikviewOpenLogCommand(sublime_plugin.WindowCommand):
  view = None
  def run(self, commandVariant=None):    
    view = self.window.active_view()
    useInfovizion = view.settings().get("use_infovizion",False)
    firstLine = view.substr(view.line(0))
    fileName = view.file_name()
    if useInfovizion:
      baseName, ext = os.path.splitext(os.path.basename(fileName))
      testFile = os.path.join(os.path.dirname(fileName),'logs',baseName +'.qvw.log') 
      if not os.path.exists(testFile):
        print('Log file not found: %s' % testFile)
        sublime.error_message('Log file not found: %s' % testFile)
      else:
        self.view = self.window.open_file(testFile)
    else:    
      baseName, ext = os.path.splitext(os.path.basename(fileName))
      testFile = ''
      if re.match(r'\/\/\#\!', firstLine):
        shebang = re.sub(r'\/\/\#\!','',firstLine)
        if shebang.endswith('.qvw'):
          testFile = shebang
          if os.path.exists(shebang):
            testFile = shebang + '.log'
        else: 
          testFile = os.path.abspath(os.path.join(os.path.dirname(fileName),shebang,baseName + '.qvw.log'))
      else:
        testFile = os.path.join(os.path.dirname(fileName),baseName +'.qvw.log') 
      if not os.path.exists(testFile):
        print('Log file not found: %s' % testFile)
        sublime.error_message('Log file not found: %s' % testFile)
      else:
        self.view = self.window.open_file(testFile)
        self.transform()
  def transform(self):
    if self.view.is_loading():
        sublime.set_timeout_async(self.transform,100)
    else:
        self.view.run_command('qlikview_transform_log') 
  def is_enabled(self):
    return self.window.active_view().file_name().upper().endswith('.QVS')