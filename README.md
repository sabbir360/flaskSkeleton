## Flask Skeleton to make large/enterprize application

### MVC Pattern Hints
 - Each module will start with module name and followed by _mod (underscoremod).
 - Module will contain `controller, models, service, report` anything else if required/ templates also can be inside it, but not recommanding.
 - All templates related stuff inside `templates` directory.
 - To add new database schema or changes, add respective models and run `python migrate.py`
 - `config.py` in root will contain all configs and imported from required script/module.
 - `dbenginge.py` is Core SQLAlchemy implementation to work with Flask, modules model will extend from this script.
 - `app.py` will contain extending related stuff such as flask config, runtime changes, error pages and so on.
 - `application.py` will extend `app.py` and tear down ending stuff. Most importantly it will contain all **routes** final blueprint call.
 - For wsgi call of production deployment we will use `wsgi.py` 
 - It will also work as a windows service which can be implement over time with help of few other things.
 - For development run use `python devrun.py`
 - To add new python library add it to `requirements.txt` and then fire `pip install -r requirements.txt`
 - For further assistance reach me *sabbir1cse@outlook.com* 