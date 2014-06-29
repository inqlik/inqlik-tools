###Changelog

####0.1.29

- Added autocompletion for most functions with cuues for parameters

####0.1.28

- Bugfix in NewExpression snippet

####0.1.27

- Bugfix in goto_files

####0.1.24

- Tabular cvs format added for Expression Editor

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