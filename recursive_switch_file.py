import sublime, sublime_plugin
import os.path
import platform

def compare_file_names(x, y):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        return x.lower() == y.lower()
    else:
        return x == y

def find_in_current_dir(basename, extensions):
    for ext in extensions:
        new_path = basename + '.' + ext

        if os.path.exists(new_path):
            return new_path
    
    return None

def find_in_special_dirs(basename, extensions, special_dirs):
    root, fbase = os.path.split(basename)

    dirname = True
    
    while dirname:
        root, dirname = os.path.split(root)

        if dirname in special_dirs:
            index = special_dirs.index(dirname)
            others = special_dirs[index + 1:] + special_dirs[:index]
            
            for d in others:
                for wroot, dirs, files in os.walk(os.path.join(root, d), topdown=False):
                    for ext in extensions:
                        found = [x for x in files if compare_file_names(x, fbase + '.' + ext)]
                        if found:
                            return os.path.join(wroot, found[0])

    return None


class RecursiveSwitchFileCommand(sublime_plugin.WindowCommand):
    def run(self, extensions=[], special_dirs=[]):
        if not self.window.active_view():
            return

        fname = self.window.active_view().file_name()
        if not fname:
            return

        path = os.path.dirname(fname)
        base, ext = os.path.splitext(fname)

        search_extensions = None
        try:
            index = extensions.index(ext[1:].lower())
            search_extensions = extensions[index + 1:] + extensions[:index]
        except:
            return

        new_path = find_in_current_dir(base, search_extensions)

        if not new_path:
            new_path = find_in_special_dirs(base, search_extensions, special_dirs)

        if new_path and os.path.exists(new_path):
            self.window.open_file(new_path)
