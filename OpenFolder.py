import sublime_plugin
import subprocess
import os

class OpenFolderCommand(sublime_plugin.WindowCommand):
  def run(self, paths):
    path = '"' + paths[0] + '"'
    if os.name == 'nt' :
      subprocess.call('explorer /e /root,' + path)
    elif os.name == 'posix' :
      subprocess.call('open ' + path)

  def is_visible(self, paths):
    return len(paths) == 1 and os.path.isdir(paths[0])