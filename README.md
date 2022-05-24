# Django-Filesystem

## Setup system
### Initialization of the Virtual Environment
    python3 -m venv .venv
    source .venv/bin/activate

### Install requirement packages
    pip install -r requirements.txt

### Create database
    python manage.py makemigrations
    python manage.py migrate

### Insert initial data (definition of the root folder)
    python manage.py loaddata data.json

### Start server
    python manage.py runserver

## Route information
### List all paths
    GET: /api/v1/path/
    return a list of all paths
    
    {
		"id": 5,
		"pathname": "/Dados",
		"foldername": "Dados",
		"parent": 1
	},

### Create a path
    POST: /api/v1/path/
    - foldername: name of the folder
    - parent: ID of the path where the new folder will be created.
    
    {
        "foldername": "libs",
        "parent": 5
    }

### Remove a path
    DELETE: /api/v1/path/[id]
    Removes a directory and its subdirectories informed by the ID.

### List all files in a path
    GET: /api/v1/path/[id]/listfiles
    Lists all files inside the directory informed by the path ID

### List all subpath of a path
    GET: /api/v1/path/[id]/listpaths
    Lists all subdirectories informed by the path ID

### List all files
    GET: /api/v1/file
    - id: id of the file
    - folder: reference to the path
    - size: size of file in bytes
    - name: name of the file
    - description: info about the file
    - specs: url to be downloaded the file

    {
		"id": 8,
		"folder": {
			"pathname": "/"
		},
		"size": 11312,
		"name": "database01.ods",
		"description": "arquivo libreoffice",
		"specs": "http://localhost:8000/media/specs/database01.ods"
	},

### List specific file
    GET: /api/v1/file/[id]
    Gets data from the file informed by the ID, similar to the previous item.

### Add a file
    POST: /api/v1/file

    [multipart/form-data]
    description: info about the file.
    specs: [file] file to be added.
    path: ID of the directory where the file will be added.

### Move file
    PATCH: /api/v1/file/[id]
    Move the file informed by the ID to the path id

    {
	    "path": 6
    }

### Delete a file
    DELETE: /api/v1/file/[id]
    Deletes the file informed by the ID.
