L'ERREUR QUE J'AI EN SUIVANT LE TUTO SIMPLEISBETTERTHANCOMPLEX :


(venv) selim@selim-UX305CA:~/Desktop/PROG/Projects_Portfolio/venv/531_calculator$ python3 manage.py runserver
Traceback (most recent call last):
  File "manage.py", line 22, in <module>
    main()
  File "manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "/home/selim/Desktop/PROG/Projects_Portfolio/venv/lib/python3.8/site-packages/django/core/management/__init__.py", line 401, in execute_from_command_line
    utility.execute()
  File "/home/selim/Desktop/PROG/Projects_Portfolio/venv/lib/python3.8/site-packages/django/core/management/__init__.py", line 345, in execute
    settings.INSTALLED_APPS
  File "/home/selim/Desktop/PROG/Projects_Portfolio/venv/lib/python3.8/site-packages/django/conf/__init__.py", line 83, in __getattr__
    self._setup(name)
  File "/home/selim/Desktop/PROG/Projects_Portfolio/venv/lib/python3.8/site-packages/django/conf/__init__.py", line 70, in _setup
    self._wrapped = Settings(settings_module)
  File "/home/selim/Desktop/PROG/Projects_Portfolio/venv/lib/python3.8/site-packages/django/conf/__init__.py", line 177, in __init__
    mod = importlib.import_module(self.SETTINGS_MODULE)
  File "/home/selim/Desktop/PROG/Projects_Portfolio/venv/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 783, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/home/selim/Desktop/PROG/Projects_Portfolio/venv/531_calculator/531_calculator/settings.py", line 78, in <module>
    default=config('DATABASE_URL')
NameError: name 'config' is not defined


L'ERREUR QUE J'AI SINON :


(venv) selim@selim-UX305CA:~/Desktop/PROG/Projects_Portfolio/venv/531_calculator$ python3 manage.py runserver
Traceback (most recent call last):
  File "manage.py", line 22, in <module>
    main()
  File "manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "/home/selim/Desktop/PROG/Projects_Portfolio/venv/lib/python3.8/site-packages/django/core/management/__init__.py", line 401, in execute_from_command_line
    utility.execute()
  File "/home/selim/Desktop/PROG/Projects_Portfolio/venv/lib/python3.8/site-packages/django/core/management/__init__.py", line 345, in execute
    settings.INSTALLED_APPS
  File "/home/selim/Desktop/PROG/Projects_Portfolio/venv/lib/python3.8/site-packages/django/conf/__init__.py", line 83, in __getattr__
    self._setup(name)
  File "/home/selim/Desktop/PROG/Projects_Portfolio/venv/lib/python3.8/site-packages/django/conf/__init__.py", line 70, in _setup
    self._wrapped = Settings(settings_module)
  File "/home/selim/Desktop/PROG/Projects_Portfolio/venv/lib/python3.8/site-packages/django/conf/__init__.py", line 177, in __init__
    mod = importlib.import_module(self.SETTINGS_MODULE)
  File "/home/selim/Desktop/PROG/Projects_Portfolio/venv/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 783, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/home/selim/Desktop/PROG/Projects_Portfolio/venv/531_calculator/531_calculator/settings.py", line 77, in <module>
    'default': dj_database_url.config(
  File "/home/selim/Desktop/PROG/Projects_Portfolio/venv/lib/python3.8/site-packages/dj_database_url.py", line 55, in config
    config = parse(s, engine, conn_max_age, ssl_require)
  File "/home/selim/Desktop/PROG/Projects_Portfolio/venv/lib/python3.8/site-packages/dj_database_url.py", line 103, in parse
    engine = SCHEMES[url.scheme] if engine is None else engine
KeyError: 'psql'
