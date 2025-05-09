import pathlib
from oauthenticator.generic import GenericOAuthenticator
from jupyterhub.spawner import SimpleLocalProcessSpawner


c.JupyterHub.spawner_class = SimpleLocalProcessSpawner

HERE = pathlib.Path(__file__).parent

c.JupyterHub.template_paths = [str(HERE / 'templates')]

c.JupyterHub.authenticator_class = GenericOAuthenticator

c.Authenticator.admin_users = [
    'sknapp'
]

c.JupyterHub.template_vars = {
    'custom': {
        "interface_selector": True,
        "default_url": "/lab",
        'org': {
            'name': 'University of Foo',
            'logo_url': 'https://jupyter.org/assets/nav_logo.svg',
            'url': 'https://jupyter.org',
        },
        'operated_by': {
            'name': 'Operating Org',
            'url': 'https://cal-icor.org'
        },
        'funded_by': {
            'name': 'Funding Org',
            'url': 'https://cal-icor.org'
        },
        'designed_by': {
            'name': 'cal-icor',
            'url': 'https://cal-icor.org'
        }
    }
}
