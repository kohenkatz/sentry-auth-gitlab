from sentry.auth.providers.oauth2 import OAuth2Callback, OAuth2Provider, OAuth2Login
from .constants import AUTHORIZE_URL, ACCESS_TOKEN_URL, CLIENT_ID, CLIENT_SECRET, SCOPE
from .views import ConfirmEmail, FetchUser, GitLabConfigureView, SelectOrganization

class GitLabOAuth2Provider(OAuth2Provider):
    name = 'GitLab'
    client_id = CLIENT_ID
    client_secret = CLIENT_SECRET

    def __init__(self, **config):
        super().__init__(**config)

    def get_configure_view(self):
        return GitLabConfigureView.as_view()

    def get_auth_pipeline(self):
        return [
            OAuth2Login(AUTHORIZE_URL, client_id=CLIENT_ID, scope=SCOPE),
            OAuth2Callback(
                access_token_url=ACCESS_TOKEN_URL,
                client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
            ),
            FetchUser()
        ]

    def get_refresh_token_url(self):
        return ACCESS_TOKEN_URL

    def build_config(self, config):
        return {}

    def build_identity(self, state):
        data = state['data']
        user_data = state['user']
        return {
            'id': user_data['id'],
            'email': user_data['email'],
            'name': user_data['name'],
            'data': self.get_oauth_data(data),
        }
