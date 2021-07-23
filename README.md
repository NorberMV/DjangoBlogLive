# Blog_app
This is a blog app Instagram Clone project based on the Python framework Django, with a Postgres DB managed by AWS RDS, the statics and the media files are being served from AWS S3.


# Pictures

<img src="https://github.com/NorberMV/DjangoBlogLive/blob/master/repo_pics/picBlog.gif" width="600">

## Usage

```python
# Create the virtual Environment and install the dependencies
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt

# Make the migrations
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

Author

Norberto Moreno | 2020