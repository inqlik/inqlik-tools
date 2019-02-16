# -*- encoding: UTF-8 -*-
import sublime
import sublime_plugin
import os
import re
class QlikviewReloadCommand(sublime_plugin.WindowCommand):
  def run(self, commandVariant=None):
    self.window.run_command('save')
    view = self.window.active_view()
    qv_executable = view.settings().get("qv_executable","c:\\Program Files\\QlikView\\qv.exe")
    useInfovizion = view.settings().get("use_infovizion",False)
    if view.settings().get('qv_script_use_cli') == True:
      self.runCli(view, qv_executable, commandVariant)
    else:
      if useInfovizion == True:
        self.runByInfovizion(view, commandVariant)
      else:
        self.runPython(view, qv_executable, commandVariant)
  def runPython(self, view, qv_executable, commandVariant=None):
    self.window.run_command('save')
    firstLine = view.substr(view.line(0))
    fileName = view.file_name()
    baseName, ext = os.path.splitext(os.path.basename(fileName))
    qvwFile = ''
    testFile = ''
    print (firstLine)
    if re.match(r'\/\/\#\!', firstLine):
      shebang = re.sub(r'\/\/\#\!','',firstLine)
      if shebang.endswith('.qvw'):
        testFile = shebang
        if os.path.exists(shebang):
          qvwFile = shebang
      else: 
        testFile = os.path.abspath(os.path.join(os.path.dirname(fileName),shebang,baseName + '.qvw'))
        if os.path.exists(testFile):
          qvwFile = testFile
    else:
      testFile = os.path.join(os.path.dirname(fileName),baseName +'.qvw') 
      if os.path.exists(testFile):
        qvwFile = testFile
    if qvwFile == '':
      sublime.error_message('File not found: %s' % testFile)
    else:
      sublime.status_message('Reloading file %s' % qvwFile)
      print("commandVariant", commandVariant)
      if commandVariant is None:
        self.window.run_command("exec", { "cmd": [qv_executable,"/R","/nodata","/Nosecurity",qvwFile]})
      else:
        self.window.run_command("exec", { "cmd": ["cmd","/C",qv_executable,qvwFile]})
  def runCli(self, view, qv_executable, commandVariant=None):
    file_regex = "^>* Parse error. File: \"(...*?)\", line: ([0-9]*)"    
    scriptPath = "%s\\Inqlik-Tools\\bin\\inqlik.bat" % sublime.packages_path()
    fileName = view.file_name() 
    if commandVariant is None:
      cliCommand = 'just_reload'
      include = 'default_include.qvs'
      if view.settings().get('qv_script_check_syntax') == True:
        cliCommand = view.settings().get('qv_script_check_syntax_mode','force_reload')
        include = view.settings().get('qv_script_check_syntax_impicit_include_file','default_inqlude.qvs')
      self.window.run_command("exec", { "file_regex": file_regex, "cmd": [scriptPath,"qvs", "--command=%s" % cliCommand, fileName]})
      print([scriptPath,"qvs", "--command=%s" % cliCommand, fileName])
    else:
      self.window.run_command("exec", { "file_regex": file_regex, "cmd": [scriptPath,"qvs", "--command=open",fileName]})
  def runByInfovizion(self, view, commandVariant=None):    
    file_regex = "^File: (.+), line: (.+)"
    executable = "c:\\Programs\\infovizion\\bin\\dart"
    snapshot = "c:\\Programs\\infovizion\\bin\\infovizion.dart.snapshot"
    work_dir = "c:\\Programs\\infovizion\\"
    fileName = view.file_name() 
    if view.settings().get('qv_script_check_syntax') == True:
      dummy = True
    self.window.run_command("exec", { "working_dir": work_dir, "file_regex": file_regex, "cmd": [executable, snapshot,"sense","app-reload", "--script", fileName]})    


