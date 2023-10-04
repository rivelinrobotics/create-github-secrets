# GitHub Action: Create GitHub Secrets

This action creates (or updates) a set of GitHub secrets using the GitHub API.

In order to use the action, a Personal Access Token must be created with the following scopes:

    - Environments: `read-write`
    - Secrets `read-write`

Currently, the action supports:

- Creation of a set of Secrets in a Repository (if the Secrets do not exist)
- Updation of a set of Secrets in a Repository (if the Secrets do exist)
- Creation of a set of Secrets in an Environment of a Repository (if the Secrets do not exist)
- Updation of a set of Secrets in an Environment of a Repository (if the Secrets do exist)

## Action Inputs

| *Input*           | *Type*  | *Required* | *Default* | *Description*                                |
|-------------------|---------|------------|-----------|----------------------------------------------|
| repository        | string  | yes        |           | The name `org/repo` of the Repository        |
| environment       | string  | no         | Empty     | The name of an Environment in the Repository |
| secrets           | string  | yes        |           | Secrets of the form `k1=v1 k2=v2 ...`        |
| token             | string  | yes        |           | A PAT with permissions to update Secrets     |

## Action Outputs

This Action does not generate any outputs.

## Example Usage

```yaml
jobs:
  update-secrets:
    runs-on: ubuntu-latest
    steps:
      - name: Update Secrets
        uses: rivelinrobotics/update-github-secrets@v1
        with:
          repository: organisation/repository
          environment: Development
          token: ${{ secrets.REPOSITORY_PAT }}
          secrets: >
            SECRET_1=FOO
            SECRET_2=BAR
            SECRET_3=BAZ
```
