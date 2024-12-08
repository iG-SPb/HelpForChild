```markdown
# Dr.Web Test Framework for Linux

Этот репозиторий содержит фреймворк для тестирования Dr.Web на Linux, использующий `pytest` и `allure`.

## Структура проекта

* **`test_drweb_fs_u_sf_av_1.py`**: Пример тестового файла.  Демонстрирует базовый тест обнаружения известных вирусов (EICAR).
* **`drweb_file_utils.py`**: Утилиты для работы с файлами (копирование по SSH, работа с Samba, чтение конфигурации).
* **`drweb_control_utils.py`**: Утилиты для управления Dr.Web через командную строку (запуск команд, установка параметров).
* **`conftest.py`**: Фикстуры pytest для настройки тестового окружения.

## Зависимости

* `pytest`
* `allure-pytest`
* `paramiko`
* `pysmb`

Установите зависимости с помощью pip:

<pre><code class="bash">
pip install pytest allure-pytest paramiko pysmb
</code></pre>

## Конфигурация

Конфигурация тестов хранится в JSON-файлах в директории, указанной в `conftest.py` (по умолчанию `/opt/jenkins/test_config/`).  Имя файла конфигурации формируется динамически: `drweb_config_test_{test_name}.json`, где `{test_name}` — имя теста (без префикса `test_` и расширения `.py`).

Пример файла конфигурации (`drweb_config_test_example.json`):

```json
{
  "test_name": "example",
  "log_file": "/var/log/drweb/test.log",
  "log_level": "debug",
  "update_interval": "60",
  "config_default_commands": "/opt/jenkins/test_config/drweb_config_default_commands.json",
  "config_test_commands": "/opt/jenkins/test_config/drweb_config_test_commands.json",
  "remote_host": "10.4.8.14",
  "remote_eicar_path": "/opt/jenkins/test_eicar/test_fs_u_sf_av_1",
  "scan_dir": "/tmp/test_scan",
  "search_strings": [
    "EICAR-Test-File",
    "eicar.com"
  ]
}
```

Файл с командами по умолчанию (`drweb_config_default_commands.json`):

```json
{
  "set_log_file": [
    "sudo",
    "drweb-ctl",
    "settings",
    "--set",
    "log-file={log_file}"
  ],
  "set_log_level": [
    "sudo",
    "drweb-ctl",
    "settings",
    "--set",
    "log-level={log_level}"
  ],
  "set_update_interval": [
    "sudo",
    "drweb-ctl",
    "settings",
    "--set",
    "update-interval={update_interval}"
  ]
}

```

Файл с тестовыми командами (`drweb_config_test_commands.json`):


```json
{
    "linuxspider_start_no": [
        "sudo",
        "/etc/init.d/drweb-linuxspider",
        "start",
        "no"
    ],
    "linuxspider_start_default": [
        "sudo",
        "/etc/init.d/drweb-linuxspider",
        "start"
    ]
}

```



## Запуск тестов

```bash
pytest --alluredir=allure-results
```

## Генерация отчета Allure

```bash
allure serve allure-results
```


## Описание функций

Подробное описание функций и их параметров представлено в docstrings внутри каждого файла.


## Примечания

*  Фреймворк предполагает, что Dr.Web уже установлен в системе.
*  Необходимы права root для выполнения некоторых команд.
*  Убедитесь, что тестовые файлы EICAR доступны на удаленном сервере по указанному пути.

```
