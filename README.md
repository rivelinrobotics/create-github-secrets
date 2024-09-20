# GitHub Action: Create GitHub Secrets

This action creates (or updates) a set of GitHub secrets using the GitHub API.

In order to use the action, a Personal Access Token or GitHub App must be created with the following scopes:

    - Environments: read-write
    - Secrets read-write

Currently, the action supports:

- Creation of a set of Secrets in an Environment of a Repository (if the Secrets do not exist)
- Updation of a set of Secrets in an Environment of a Repository (if the Secrets do exist)

## Action Inputs

| *Input*           | *Type*  | *Required* | *Default* | *Description*                                  |
|-------------------|---------|------------|-----------|------------------------------------------------|
| repositories      | string  | yes        |           | The names of the Repositories, space delimited |
| environment       | string  | yes        |           | The name of an Environment in each Repository  |
| secrets           | string  | yes        |           | Secrets of the form `k1=v1 k2=v2 ...`          |
| token             | string  | yes        |           | A PAT with permissions to update Secrets       |

## Action Outputs

This Action does not generate any outputs.

##

## Configuring a GitHub App for Authentication

1. Navigate to Organization > Settings > GitHub Apps
2. Create a new App with the following settings:
   - <b>scopes</b>: secrets: write
   - <b>redirect_url<b>: https://www.rivelinrobotics.com
   - <b>webhooks</b>: disabled
3. Install the App with the following settings:
   - Repository level
   - Install to each repository whose secrets you want to write to
4. Save the App secrets in the repository using this action:
   - Generate a Private Key for the App (at the bottom of the App Settings)
   - The App ID should be saved as `<APP_NAME>_APP_ID`
   - The Private Key should be saved as `<APP_NAME>_PRIVATE_KEY`

## Example Usage (with a GitHub App)

```yaml
jobs:
  update-secrets:
    runs-on: ubuntu-latest
    steps:
      - name: Fetch Token for Access to Write Secrets
        id: token
        uses: actions/create-github-app-token@v1
        with:
          app-id: ${{ secrets.<APP_NAME>_APP_ID }}
          private-key: ${{ secrets.<APP_NAME>_PRIVATE_KEY }}
          repositories: >
            repository_1,
            repository_2,
            repository_3
      - name: Update Secrets in other Repositories
        uses: rivelinrobotics/create-github-secrets@v2.0.0
        with:
          repositories: >
            repository_1
            repository_2
            repository_3
          environment: Development
          token: ${{ steps.token.outputs.token }}
          secrets: >
            SECRET_1=FOO
            SECRET_2=BAR
            SECRET_3=BAZ
```
