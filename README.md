# Marvin Bot

This is an example to build a chatbot on Facebook Messenger using Flask and RiveScript.

## Deploying to Heroku

```
heroku create bot
heroku config:set FACEBOOK_PAGE_TOKEN=<PAGE_TOKEN>
heroku config:set FACEBOOK_VERIFICATION_TOKEN=<VERIFICATION_TOKEN>
heroku git:remote -a bot
git push heroku master
```
