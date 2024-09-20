# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### :sparkles: Added 

- New features go here

### :pencil2: Changed

- Changes in existing functionality go here

### :warning: Deprecated

 - Soon-to-be removed features go here

### :no_entry_sign: Removed

  - Now removed features go here

### :wrench: Fixed

   - Bug fixes go here

## [3.0.0] - 2024-09-20

### :sparkles: Added 

- `app-id` argument added for creating GitHub App Token
- `private-key` argument added for creating GitHub App Token

### :pencil2: Changed

- Modifies action to generate GitHub App Token internally
- `repositories` argument now takes a comma separated list

## [2.0.0] - 2024-06-10

### :sparkles: Added 

 - `repositories` argument added accepting a space separated list of repository names

### :no_entry_sign: Removed

 - `repository` argument removed in favour of `repositories`

## [1.0.1] - 2023-10-24

### :wrench: Fixed

 - Allows parsing of secrets that contain equals characters in the value

## [1.0.0] - 2023-10-04

### :sparkles: Added 

 - Adds initial create-github-secrets Action
 - Adds support for creating and updating Environment Secrets
 - Adds README
 - Adds LICENSE
 - Adds CHANGELOG
