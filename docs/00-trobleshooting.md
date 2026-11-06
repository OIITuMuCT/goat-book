# 1 Traceback: 
> File "<frozen posixpath>", line 77, in join 
> TypeError: expected str, bytes or os.PathLike object, not NoneType
```bash
FTraceback (most recent call last):
  File "/home/neko/.pyenv/versions/3.14.10/lib/python3.14/wsgiref/handlers.py", line 137, in run
    self.result = application(self.environ, self.start_response)
                  ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/neko/PycharmProjects/PythonProject6/.venv/lib/python3.14/site-packages/django/test/testcases.py", line 1700, in __call__
    return super().__call__(environ, start_response)
           ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/neko/PycharmProjects/PythonProject6/.venv/lib/python3.14/site-packages/django/core/handlers/wsgi.py", line 124, in __call__
    response = self.get_response(request)
  File "/home/neko/PycharmProjects/PythonProject6/.venv/lib/python3.14/site-packages/django/test/testcases.py", line 1683, in get_response
    return self.serve(request)
           ~~~~~~~~~~^^^^^^^^^
  File "/home/neko/PycharmProjects/PythonProject6/.venv/lib/python3.14/site-packages/django/test/testcases.py", line 1695, in serve
    return serve(request, final_rel_path, document_root=self.get_base_dir())
  File "/home/neko/PycharmProjects/PythonProject6/.venv/lib/python3.14/site-packages/django/views/static.py", line 45, in serve
    fullpath = Path(safe_join(document_root, path))
                    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "/home/neko/PycharmProjects/PythonProject6/.venv/lib/python3.14/site-packages/django/utils/_os.py", line 73, in safe_join
    final_path = abspath(join(base, *paths))
                         ~~~~^^^^^^^^^^^^^^
  File "<frozen posixpath>", line 77, in join
TypeError: expected str, bytes or os.PathLike object, not NoneType
Traceback (most recent call last):
  File "/home/neko/.pyenv/versions/3.14.10/lib/python3.14/wsgiref/handlers.py", line 137, in run
    self.result = application(self.environ, self.start_response)
                  ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/neko/PycharmProjects/PythonProject6/.venv/lib/python3.14/site-packages/django/test/testcases.py", line 1700, in __call__
    return super().__call__(environ, start_response)
           ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/neko/PycharmProjects/PythonProject6/.venv/lib/python3.14/site-packages/django/core/handlers/wsgi.py", line 124, in __call__
    response = self.get_response(request)
  File "/home/neko/PycharmProjects/PythonProject6/.venv/lib/python3.14/site-packages/django/test/testcases.py", line 1683, in get_response
    return self.serve(request)
           ~~~~~~~~~~^^^^^^^^^
  File "/home/neko/PycharmProjects/PythonProject6/.venv/lib/python3.14/site-packages/django/test/testcases.py", line 1695, in serve
    return serve(request, final_rel_path, document_root=self.get_base_dir())
  File "/home/neko/PycharmProjects/PythonProject6/.venv/lib/python3.14/site-packages/django/views/static.py", line 45, in serve
    fullpath = Path(safe_join(document_root, path))
                    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "/home/neko/PycharmProjects/PythonProject6/.venv/lib/python3.14/site-packages/django/utils/_os.py", line 73, in safe_join
    final_path = abspath(join(base, *paths))
                         ~~~~^^^^^^^^^^^^^^
  File "<frozen posixpath>", line 77, in join
TypeError: expected str, bytes or os.PathLike object, not NoneType
```
## Решение:
> Добавить STATIC_ROOT, MEDIA_ROOT, MEDIA_URL. 
```python
# settings.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Убедитесь, что эти переменные установлены:
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Не должно быть None!

# Если падает на медиа-файлах:
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'        # Не должно быть None!

```