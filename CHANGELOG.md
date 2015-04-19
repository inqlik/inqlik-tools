###Changelog

####0.1.37

- Sublime Text introduced serious regression in default Build Systems behaviour. Default key binding `F7` and `Ctrl-Shift-B` currently not run alternative build tasks (`Reload` and `Open qvw file` in case if former build system for QVS files) but pops up some menu with some commmand variants. In this version I recover previous behaviour using basic syntax specific key-bindings. `F7` silently run `Reload` command. `Ctrl-Shift-B` run `Open qvw file` command as in previous revisions of ST3.
- Plugin optionally can use `Inqlik CLI` command line utility for some tasks. That utility now shipped with package
- `QlikView script settings` items added to `Package settings\Inqlik-Tools` menu.
- QlikView script settings extended to provide options for using `Inqlik CLI` for `Reload` and `Open qvw file` tasks. `Reload` task can include check syntax phase 
- Inqlik CLI supports сustom file name in relative build paths. [See feature request](https://github.com/inqlik/inqlik-tools/issues/5)
- Package settings defaults to using old python code for reload and open qvw file tasks

####0.1.36

- Add build system for Expression files. Use external (Inqlik CLI) tool

####0.1.35

- Bugfix for https://github.com/inqlik/inqlik-tools/issues/3

####0.1.34

- Bugfix for https://github.com/inqlik/inqlik-tools/issues/2


####0.1.33

- Permit unicode variable names. Again

####0.1.32

- By default TAG column in QDF variables file filled with values from SECTION, it ca be overloaded by explicit tag: tag, Added completions for qvs parser directives. Bugfix for

####0.1.31

- Bugfix for tabular csv export format for Expression Editor. Export format was erroneously named `CVS` both in README and in plugin code.
Name for tabular csv format fixed and changed to `CSV`

####0.1.30

- Some changes in auto-completion for functions
- Added menu command and key combination for command `Expand variables and export file` in Expression editor
- Plain QVS export format temporarily removed from Expression Editor.
- `.no-sublime-package` file flag added to project. Packaged format sometimes lead to bugs. 

####0.1.29

- Added auto-completion for most functions with cues for parameters

####0.1.28

- Bugfix in NewExpression snippet

####0.1.27

- Bugfix in goto_files

####0.1.24

- Tabular CSV format added for Expression Editor

####0.1.23

- Bugfix to qvw.log files viewer

####0.1.22

- Qvw.log file viewer added
- Menu and keyboard (ctrl-shilt+l) commands for opening and reformat qvw.log files

####0.1.21

- Package renamed to InQlik Tools
- Tags names changed to lowercase camelCase format
- Menu items for package preferences
- Default settings for variable files

####0.1.20

- Bugfix in error processing in variable files plugin
- Additional tags in variable files plugin

####0.1.19

- Symbols in qvs: suroutines, variables and table identifiers. Tabs are local symbols
- Symbols in expression files: expression names and \#SECTION tags

####0.1.18

- QVD Viewer plugin added. (ST3 only)

####0.1.17

- Expression file plugin refactored

####0.1.16

- qlikview_vars.py refactored
- Syntax for qlikview-vars files changed
- Support for most properties of qlikview expression added.
- Settings for configuration of derived variable names 

####0.1.15

- Bugfix for relative paths in shebang for Build system. Tested in QlikView Deployment Framework environment

####0.1.14

- Get rid of qvw_load.bat. Build system now runs custom-made command QlikviewReloadCommand. QlikView executable path can be changed in user settings

####0.1.13

- qvw_load.bat fixed. Build system now works with qvs scripts encoded with UTF8 with BOM

####0.1.12

- Readme sections for  Build system usage and installation added

####0.1.11

- Legacy syntax for expression files removed. Futher development will use QlikView variables files compatible with QlikView Deployment Framework
- Build system added. Able to run batch reload of qvw file in same directory or explicitely set by shebang syntax


####0.1.10

- Initial release for Package Control Channel