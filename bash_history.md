# .bash_history
## Initial commit
```shell
git init
git add .
git commit -m "Initial commit"
# Create repository
git remote add origin git@gitflic.ru:deviur/async-flask-example.git
git push -u origin master
```
## Creating async Flask application
```shell
pip install --upgrade pip
pip install "Flask[async]"
pip install requests
pip freeze > requirements.txt
# Create & debug the application
t add .
git commit -m "Created sync & async examples "
git push
```