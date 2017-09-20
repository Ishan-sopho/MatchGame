## A simple game to match input with choices
written in python 2.7, using the Django framework

### working urls
 * `game/` : the actual url of the game
 * `responses/` : where the responses are processed, it redirects back to `game/`
 * `login/` : user login is required to play game, user can be registered only by admin
 * `logout/` : to logout user, it redirects back to `login/`

## deploying on server
* delete `local.py`
* change values of `ALLOWED_HOSTS`, `STATIC_ROOT` in `production.py` as required

## setting up on pythonanywhere
1. making virtual environment [tutorial](https://help.pythonanywhere.com/pages/FollowingTheDjangoTutorial/) for python anywhere
2. deploying exisiting django project to python anywhere [tutorial](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/)  
*Note:* The part about creating virtual environment and setting up django. Follow tutorial 1. clone project folder. cd into folder. type `pip install -r requirements.txt`

