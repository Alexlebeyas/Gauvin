# !!! DO NOT CHECK SECRET VALUES (passwords, API keys, etc.) INTO THIS FILE !!!
# See the README for handling secret values

# These variables are common to all environments, and can be overriden in an environment specific file.
location     = "canadacentral"
project_name = "gauvin"

# Look up Object IDs here: https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/Overview
key_vault_access_policies = [
  {
    name      = "Joshua Majonis"
    object_id = "c29870a6-bb74-47d3-bbc3-f4284b8df130"
  },
  {
    name      = "Romain Menu"
    object_id = "bda597e0-e9fc-4bcf-a4e3-2c8c46983469"
  },
  {
    name      = "Alexis Mouloum"
    object_id = "e933cab1-cc24-4db9-992c-92036c5ead17"
  },
]
