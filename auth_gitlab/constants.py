from django.conf import settings

CLIENT_ID = getattr(settings, 'GITLAB_APP_ID', None)
CLIENT_SECRET = getattr(settings, 'GITLAB_APP_SECRET', None)

BASE_DOMAIN = getattr(settings, 'GITLAB_BASE_DOMAIN', None)
SCHEME = getattr(settings, 'GITLAB_HTTP_SCHEME', 'https')
API_VERSION = getattr(settings, 'GITLAB_API_VERSION', 4)
SCOPE = getattr(settings, 'GITLAB_AUTH_SCOPE', 'api')

ACCESS_TOKEN_URL = '{0}://{1}/oauth/token'.format(SCHEME, BASE_DOMAIN)
AUTHORIZE_URL = '{0}://{1}/oauth/authorize'.format(SCHEME, BASE_DOMAIN)
API_BASE_URL = '{0}://{1}/api/v{2}'.format(SCHEME, BASE_DOMAIN, API_VERSION)

# Just dummies from copied GitHub API so far
ERR_NO_ORG_ACCESS = "You do not have access to the required GitLab organization."
ERR_NO_PRIMARY_EMAIL = "We were unable to find a primary email address associated with your GitLab account."

ERR_NO_SINGLE_PRIMARY_EMAIL = "We were unable to find a single primary email address associated with your GitLab account."

ERR_NO_VERIFIED_PRIMARY_EMAIL = "We were unable to find a verified, primary email address associated with your GitLab account."

ERR_NO_SINGLE_VERIFIED_PRIMARY_EMAIL = "We were unable to find a single verified, primary email address associated with your GitLab account"
