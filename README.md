# GitHub Action: Create GitHub Secrets

This action creates (or updates) a set of GitHub secrets using the GitHub API.

## Configuring a GitHub App for Authentication

In order to use the action, a GitHub App must be created with the correct scopes:

1. Navigate to Organization > Settings > GitHub Apps
2. Create a new App with the following settings:
   - <b>scopes</b>: {secrets: read-write, environments: read-write}
   - <b>homepage</b>: https://www.rivelinrobotics.com
   - <b>webhooks</b>: disabled
3. Install the App to each Repository the action needs to write to
4. Create a pair of Secrets in the repository using this action:
   - Generate a Private Key for the App (at the bottom of the App Settings)
   - The App ID should be saved as `<APP_NAME>_APP_ID`
   - The Private Key should be saved as `<APP_NAME>_PRIVATE_KEY`

Currently, the action supports:

- Creation of a set of Secrets in an Environment of a Repository (if the Secrets do not exist)
- Updation of a set of Secrets in an Environment of a Repository (if the Secrets do exist)

## Action Inputs

| *Input*           | *Type*  | *Required* | *Default* | *Description*                                              |
|-------------------|---------|------------|-----------|------------------------------------------------------------|
| app-id            | string  | yes        |           | The ID of a GitHub App with the above permissions          |
| private-key       | string  | yes        |           | The Private Key of a GitHub App with the above permissions |
| repositories      | string  | yes        |           | The names of the Repositories, comma delimited             |
| environment       | string  | yes        |           | The name of an Environment in each Repository              |
| secrets           | string  | yes        |           | Secrets of the form `k1=v1 k2=v2 ...`                      |

## Action Outputs

This Action does not generate any outputs.

## Example Usage

```yaml
jobs:
  update-secrets:
    runs-on: ubuntu-latest
    steps:
      - name: Create Secrets
        uses: rivelinrobotics/create-github-secrets@v3.0.0
        with:
          app-id: ${{ secrets.<APP_NAME>_APP_ID }}
          private-key: ${{ secrets.<APP_NAME>_PRIVATE_KEY }}
          repositories: repository_1,repository_2
          environment: Development
          secrets: SECRET_1=FOO SECRET_2=BAR
```
