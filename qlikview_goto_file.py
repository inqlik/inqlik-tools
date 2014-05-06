import sublime, sublime_plugin
import os
from fnmatch import fnmatch

class QlikviewGotoFile(sublime_plugin.WindowCommand):
    def find_files(self, fileName):
        result = set([])
        if os.path.isfile(fileName):
            return [fileName]
        for folder in sublime.active_window().folders():
            for root, dirs, files in os.walk(folder):
                for file in files:
                    if file.upper().endswith(fileName.upper()):
                        result.add(os.path.join(root, file))
        return list(result)
    def open_file(self,fileName):
        open_externally = False
        for gpat in sublime.active_window().active_view().settings().get("open_externally_patterns", []):
            if fnmatch(fileName, gpat):
                open_externally = True
        print(fileName)        
        if open_externally:
            sublime.status_message("Opening file ...... " + fileName)
            os.startfile(fileName)
            sublime.status_message("")
        else:
            sublime.active_window().open_file(fileName)
    def run(self, fileName = None):
        print ('qlikview_goto_file');
        orig_sel = None
        v = self.window.active_view()
        if v:
            orig_sel = [r for r in v.sel()]

        if not fileName and not v:
            return

        if not fileName:
            pt = v.sel()[0]

            fileName = v.substr(v.expand_by_class(pt,
                sublime.CLASS_WORD_START | sublime.CLASS_WORD_END,
                "[]{}()<>:="))
        print('Find and open file %s' % fileName)
        fileName = fileName.strip('\\/');
        files = self.find_files(fileName)
        print (files)
        if len(files) == 0:
            sublime.status_message("Unable to find " + fileName)
        elif len(files) == 1:
            print('Opening')
            self.open_file(files[0])
        else:
            self.window.show_quick_panel(
                files,
                lambda x: self.open_file(files[x]))
