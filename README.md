# Marvin Bot

This is an example to build a chatbot on Facebook Messenger using Flask, RiveScript
and Redis as a session storage.

## Deploying to Heroku

```
heroku create bot
heroku config:set FACEBOOK_PAGE_TOKEN=<PAGE_TOKEN>
heroku config:set FACEBOOK_VERIFICATION_TOKEN=<VERIFICATION_TOKEN>
heroku plugins:install heroku-redis
heroku addons:create heroku-redis:hobby-dev -a sushi
heroku git:remote -a bot
git push heroku master
```
