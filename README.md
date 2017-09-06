# Marvin, the Paranoid Android

[![Code Climate](https://codeclimate.com/github/magrathealabs/marvin-bot/badges/gpa.svg)](https://codeclimate.com/github/magrathealabs/marvin-bot)
[![license](https://img.shields.io/github/license/magrathealabs/mlabs-messenger.svg)](https://github.com/magrathealabs/mlabs-messenger/blob/master/LICENSE)

This is an example that shows how to deploy a chatbot on Facebook Messenger using Flask,
[RiveScript](https://www.rivescript.com/docs/tutorial) and Redis as a session storage.

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

## Demo

![Demo](https://github.com/magrathealabs/marvin-bot/blob/master/docs/images/demo.gif "Demo")

## Documentation

* [Facebook Messenger Documentation](https://developers.facebook.com/docs/messenger-platform)
* [RiveScript Tutorial](https://www.rivescript.com/docs/tutorial)

## License

The code in this repository is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).

## About Magrathea Labs

`marvin-bot` is maintained by Magrathea Labs. The names and logos for Magrathea Labs are trademarks of Magrathea Labs.

Magrathea Labs is a team of specialists in Software Engineering, Distributed Systems, Artificial Intelligence and
Data Science. We love to solve challenging problems and build amazing things. Want to do something amazing with us?
We are available for [hire](mailto:contact@magrathealabs.com).

