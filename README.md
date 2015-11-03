# sublime-text-switch-file
Sublime Text command to switch between header/source files that are located in different directories.

It's designed to work and configure like the Sublime Text 3 built-in switch_file command (`alt+o`), but with a twist. It supports moving switch between files that are in different folders. If a set of special directory names ('include' and 'src' by default) is given, it'll go down the folder path until it finds a folder named with one of the given special name.
Once it finds a special name, it'll look if any of it's sibling directory have one of the other special name and walk up those directory until it finds a file with the same basename but different extension as the current file.
If none is found it'll continue looking down the directory path.

It mostly naive and may become slow if it has to search through huge codebase with huge hierarchy of folder under the special directory name and doesn't offer any smart mechanism like caching to speed-up the seach time, but empirical testing shows it's almost instantaneous on the 12000+ source files project I work on.

## Installation
For now, clone the repository in your `<data_path>/Packages` folder (see https://www.sublimetext.com/docs/3/packages.html). I'll probably add the package to Package Control later.

## Customization
Default key binding will replace the `alt+o` from the default `switch_file` command to `recursive_switch_file` like this:
```javascript
{
    "keys": ["alt+o"],
    "command": "recursive_switch_file",
    "args":
    {
        "extensions": ["cpp", "cxx", "cc", "c", "hpp", "hxx", "hh", "h", "ipp", "inl", "m", "mm"],
        "special_dirs": ["include", "src"]
    }
}
```
To customize searched `extensions` or `special_dirs` parameters, simply copy the binding to your User defined key bindings file and alter it.

