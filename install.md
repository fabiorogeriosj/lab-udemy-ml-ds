Caso tenha problemas no windows sobre:

```
C:\Users\fabio.jose>jupyter notebook
Traceback (most recent call last):
  File "c:\users\fabio.jose\appdata\local\programs\python\python36-32\lib\runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "c:\users\fabio.jose\appdata\local\programs\python\python36-32\lib\runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "C:\Users\fabio.jose\AppData\Local\Programs\Python\Python36-32\Scripts\jupyter-notebook.EXE\__main__.py", line 5, in <module>
  File "c:\users\fabio.jose\appdata\local\programs\python\python36-32\lib\site-packages\notebook\notebookapp.py", line 38, in <module>
    from jinja2 import Environment, FileSystemLoader
  File "c:\users\fabio.jose\appdata\local\programs\python\python36-32\lib\site-packages\jinja2\__init__.py", line 33, in <module>
    from jinja2.environment import Environment, Template
  File "c:\users\fabio.jose\appdata\local\programs\python\python36-32\lib\site-packages\jinja2\environment.py", line 15, in <module>
    from jinja2 import nodes
  File "c:\users\fabio.jose\appdata\local\programs\python\python36-32\lib\site-packages\jinja2\nodes.py", line 19, in <module>
    from jinja2.utils import Markup
  File "c:\users\fabio.jose\appdata\local\programs\python\python36-32\lib\site-packages\jinja2\utils.py", line 647, in <module>
    from markupsafe import Markup, escape, soft_unicode
  File "c:\users\fabio.jose\appdata\local\programs\python\python36-32\lib\site-packages\markupsafe\__init__.py", line 14, in <module>
    from markupsafe._compat import text_type, string_types, int_types, \
ModuleNotFoundError: No module named 'markupsafe._compat'
```

Tente instalar o markupsafe: `pip install markupsafe`

Caso tenha problemas para instalar o markupsafe:

```
Exception:
Traceback (most recent call last):
  File "c:\users\fabio.jose\appdata\local\programs\python\python36-32\lib\site-packages\pip\compat\__init__.py", line 73, in console_to_str
    return s.decode(sys.__stdout__.encoding)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf3 in position 9: invalid continuation byte

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "c:\users\fabio.jose\appdata\local\programs\python\python36-32\lib\site-packages\pip\basecommand.py", line 215, in main
    status = self.run(options, args)
  File "c:\users\fabio.jose\appdata\local\programs\python\python36-32\lib\site-packages\pip\commands\install.py", line 342, in run
    prefix=options.prefix_path,
  File "c:\users\fabio.jose\appdata\local\programs\python\python36-32\lib\site-packages\pip\req\req_set.py", line 784, in install
    **kwargs
  File "c:\users\fabio.jose\appdata\local\programs\python\python36-32\lib\site-packages\pip\req\req_install.py", line 878, in install
    spinner=spinner,
  File "c:\users\fabio.jose\appdata\local\programs\python\python36-32\lib\site-packages\pip\utils\__init__.py", line 676, in call_subprocess
    line = console_to_str(proc.stdout.readline())
  File "c:\users\fabio.jose\appdata\local\programs\python\python36-32\lib\site-packages\pip\compat\__init__.py", line 75, in console_to_str
    return s.decode('utf_8')
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf3 in position 9: invalid continuation byte
```

Instale a versão mais atual do pip e o problema pode ser resolvio: `python -m pip install -U https://github.com/pypa/pip/archive/master.zip`