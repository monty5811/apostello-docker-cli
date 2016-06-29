import os

import click


def load_config():
    """Parse existing .env file.

    Taken from https://github.com/theskumar/python-dotenv/.
    """
    config = {}

    if not os.path.isfile('.env'):
        return config

    with open('.env', 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            k, v = line.split('=', 1)
            config[k] = v

    return config


def save_config(config):
    """Write new config to .env"""
    with open('.env', "w") as f:
        for k, v in config.items():
            f.write('{0}={1}\n'.format(k, v))


def prompt_for_update(config, key):
    """Prompt user for config var.

    Asks the user to provide a config value.

    If a value already existed in the .env file, it is
    shown as the default.
    """
    prompts = {
        'TWILIO_ACCOUNT_SID': 'Twilio account SID',
        'TWILIO_AUTH_TOKEN': 'Twilio auth token',
        'TWILIO_FROM_NUM': 'The phone number you want to use (you need to buy one on Twilio)',
        'TWILIO_SENDING_COST':
        'Cost of sending messages in your country (see: https://www.twilio.com/sms/pricing)',
        'DJANGO_EMAIL_HOST': 'Email host',
        'DJANGO_EMAIL_HOST_USER': 'Email user',
        'DJANGO_EMAIL_HOST_PASSWORD': 'Email password',
        'DJANGO_FROM_EMAIL':
        'From email (the address that apostello emails will appear to come from)',
        'DJANGO_TIME_ZONE':
        'Please enter your time zone, a list of which can be found here: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones',
        'CADDY_LE_EMAIL':
        'We use caddy as a web server\nThis allows automatic SSL, but you need to provide an email address for the Lets Encrypt process',
        'ELVANTO_KEY': 'Elvanto API Key',
        'COUNTRY_CODE': 'Country Phone number prefix, eg 44',
        'WHITELISTED_LOGIN_DOMAINS':
        'Comma separated list of domains (e.g. apostello.ninja,apostello.io)',
        'OPBEAT_APP_ID': 'Opbeat App ID:',
        'OPBEAT_ORGANIZATION_ID': 'Opbeat Org ID:',
        'OPBEAT_SECRET_TOKEN': 'Opbeat scret token',
        'OPBEAT_JS_APP_ID': 'Opbeat app ID',
        'OPBEAT_JS_ORG_ID': 'Opbeat org ID',
    }

    if key in config:
        config[key] = click.prompt(prompts[key], default=config[key])
    else:
        config[key] = click.prompt(prompts[key], )

    return config


@click.command('config')
def config():
    """Interactive config of env file"""
    click.echo('Welcome to apostello setup!')
    click.echo('')
    config = load_config()
    # twilio settings
    click.echo('First, we will setup Twilio so we can send SMS')
    config = prompt_for_update(config, 'TWILIO_ACCOUNT_SID')
    config = prompt_for_update(config, 'TWILIO_AUTH_TOKEN')
    config = prompt_for_update(config, 'TWILIO_FROM_NUM')
    config = prompt_for_update(config, 'TWILIO_SENDING_COST')
    # email
    click.echo(
        'apostello sends emails to manage account sign ups, so you need a way to send emails.')
    click.echo('We recommend using https://www.mailgun.com/')
    config = prompt_for_update(config, 'DJANGO_FROM_EMAIL')
    config = prompt_for_update(config, 'DJANGO_EMAIL_HOST')
    config = prompt_for_update(config, 'DJANGO_EMAIL_HOST_USER')
    config = prompt_for_update(config, 'DJANGO_EMAIL_HOST_PASSWORD')
    # misc
    config = prompt_for_update(config, 'DJANGO_TIME_ZONE')
    # ssl
    config = prompt_for_update(config, 'CADDY_LE_EMAIL')
    # elvanto
    if click.confirm('Do you want to import from Elvanto?'):
        config = prompt_for_update(config, 'ELVANTO_KEY')
        config = prompt_for_update(config, 'COUNTRY_CODE')
    else:
        # remove elvanto settings
        config.pop('ELVANTO_KEY', None)
        config['COUNTRY_CODE'] = '44'
    # opbeat
    if click.confirm(
            'Do you want to track backend apostello errors with opbeat?'):
        config = prompt_for_update(config, 'OPBEAT_ORGANIZATION_ID')
        config = prompt_for_update(config, 'OPBEAT_APP_ID')
        config = prompt_for_update(config, 'OPBEAT_SECRET_TOKEN')
    else:
        config.pop('OPBEAT_ORGANIZATION_ID', None)
        config.pop('OPBEAT_APP_ID', None)
        config.pop('OPBEAT_SECRET_TOKEN', None)
    if click.confirm(
            'Do you want to track frontend apostello errors with opbeat?'):
        config = prompt_for_update(config, 'OPBEAT_JS_ORG_ID')
        config = prompt_for_update(config, 'OPBEAT_JS_APP_ID')
    else:
        config.pop('OPBEAT_JS_ORG_ID', None)
        config.pop('OPBEAT_JS_APP_ID', None)
    # white listed login domains
    if click.confirm(
        'Do you want to whitelist any domains?\n' \
        '\tBe careful with this setting as it means anyone with an email account on a whitelisted domain is automatically approved after verifying their email address.\n'):
        config = prompt_for_update(config, 'WHITELISTED_LOGIN_DOMAINS:')

    # need to provide GUNICORN_MAX_REQUESTS:
    config['GUNICORN_MAX_REQUESTS'] = 0
    click.echo('')
    click.echo('Writing config to ".env" ...')
    save_config(config)
    click.echo('Config written to ".env"')
    click.echo('')
    click.echo('')
    click.echo(
        'You can rerun "apostello config" any time to update your configuration')


if __name__ == '__main__':
    config()
