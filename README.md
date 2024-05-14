pgbackup
========
A CLI tool for backing up remote PostgreSQL databases locally or to AWS S3. 

## Usage
Pass in a full database URL, the storage driver, and destination.

S3 Example w/ bucket name:
```
$ pgbackup postgresql://bob@example.com:5432/db_one --driver s3 backups
```
Local Example w/ local path:
```
$ pgbackup postgresql://bob@example.com:5432/db_one --driver local /
var/local/db_one/backups.sql
```
## Installation
### From Source
To install the pgbackup command line tool at the user level after you've cloned the repository, run the following command from the project's root directory:
```
$ pip install --user -e .
```
### From Wheel
Wheels are binary files created from python source code and used to distribute python packages. `.whl` files are much smaller than source code. Consequently, they take up less storage and can be transferred over the internet faster than source code. 

This project uses [PDM](https://pdm-project.org/latest/), a powerful python package manager with a strong emphasis on compliance with PEP standards. If pdm is installed, you can build a wheel with `pdm build`. Alternately, you can build with [`build`](https://pypi.org/project/build/), a build back-end agnostic build tool, by running `python -m build` [link](https://stackoverflow.com/a/60416265/10964962). You can then run `pip install ./dist/pgbackup-<etc.>.whl` to install from the wheel just built in your `dist` folder.

## Preparing for Development
Follow these steps to start developing with this project:
1. Ensure `pip` is installed
2. Clone repository: `git clone git@github.com:jacobarchambault/pgbackup`
3. `cd` into the repository
4. Create and activate your virtual environment: `python -m venv venv/ && . venv/bin/activate` 
5. To install and use the pgbackup command line tool as a package in venv using the latest versions of the project's dependencies, run `pip install -e .` from your activated virtual environment. 
6. Alternately, to test your wheel directly, you can run `pip install </path/to/pgbackup-etc.whl>` from a fresh virtual environment after building.

### Setting up a test postgresql database (optional)
This project comes with a bash script that can be used to set up a postgresql database running in a Docker container. Running the script requires installing [podman](https://podman.io/), a lightweight rootless and daemonless alternative to Docker for managing containers. Podman's command line interface overlaps heavily with that for Docker, making it easy to use for Docker users.

To run the bash script, `cd` into the root directory for this project, run `bash db_setup.sh` and follow the instructions to set up your username and password.

To test your database, you can run `psql postgresql://<username>:<password>@localhost:5432/sample -c "SELECT * FROM employees;"`, substituting the username and password you provided. This should print three rows of employee data to the console. 

## Updating project dependencies
This project comes with a `pip-tools`-generated `requirements.txt` file, which pins down and provides hashes for both direct and transitive dependencies. If you wish to install the exact project dependencies from this `requirements.txt` file, run `pip install -r requirements.txt` in your virtual environment

To update the list of pinned dependencies provided in requirements.txt, (cf. [link](https://stackoverflow.com/a/69081814/10964962)) run the following commands from within a fresh virtual environment:

1. `pip install pipreqs` (a tool for generating dependencies from your source code) 
2. `pip install pip-tools` (a tool used to create requirements.txt from requirements.in)
3. `pipreqs --savepath=requirements.in` (creates a requirements.in file from source code dependencies)
4. `rm requirements.txt & pip-compile --strip-extras --generate-hashes` (auto-generates requirements.txt from requirements.in, with transitive dependencies explicitly stated)

## About
This project is forked from https://github.com/linuxacademy/content-python3-sysadmin/tree/master/pgbackup . This version includes the following updates and improvements:
1. A `pyproject.toml` file built with `pdm` in place of the original project's `setup.py`. 
2. replacement of the original file's reliance on `Pipenv` and `Pipenv.lock` files with a `pip-tools`-based `requirements.in` and `requirements.txt`. 
3. A trimmed, podman-compatible db_setup.sh file with fewer rows inserted into the sample database's `EMPLOYEES` table to minimize AWS S3 storage costs.
4. A more comprehensive `README`. 
5. More targeted imports using `from _ import _ ` over `import _` to decrease project size.
6. Improved modularity, separating out functions depending on different imports into different files. 
