"""Settings for the expense tracker, read from the environment."""

import os

# Secret for the receipt upload. Set AWS_SECRET_ACCESS_KEY in the environment;
# never write the value itself into this file.
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
