Python package to internationalize your program

## To start with ##
Use .lang-files in format:
```
internationalize.value1=localize.value1
internationalize.value2=localize.value2
...
```
It is recommended to give names to files in the form "lang_LANG".
Default language is English so you should always create a file "en_EN.lang".
Default directory path is "./assets/lang/". You can change path and language.

To use this library firstly import it in your main file. You can change default settings here (language and path) and it applies for whole project.


## Usage: ##
#### 0) Import: ####
```Python
import pyI18n
```
    
#### 1) Localize: ####
```Python
pyI18n.format("internationalize.string")

>>> "localize.string"

# Firstly search for translatable string in currently selected file
# If can't find, search for it in "en_EN.lang" file
# If can't find it again, return itself
```

#### 2) Setup language: ####
```Python
pyI18n.set_lang("en_EN")  # You can enter the name of any .lang file instead of it
```

#### 3) Get selected language: ####
```Python
pyI18n.get_lang()

>>> "en_EN"  # Default language
```

#### 4) Set new path: ####
```Python
pyI18n.set_path("new_path")  # It is recommended to set here absolute path
```

#### 5) Get current path: ####
```Python
pyI18n.get_path()
>>> "./assets/lang"  # Default path
```
    
#### 6) Get all accepted languages: ####
```Python
pyI18n.get_all_langs()
>>> ["en_EN", ...]  # List of langs
```

#### 7) Add new lang inside of programm: ####
```Python
pyI18n.addLang(name, dict)
# "name" is future file name and "dict" is a dictionary which will transform in .lang file in format
# key=value
```
