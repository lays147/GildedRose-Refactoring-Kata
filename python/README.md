# Gilded Rose Kata

## Branches

01_unit_testing -> Add unit testing for existing code in Python 2.7  
02_instrumentation -> Add basic instrumentation tools to this project
03_feat_conjured -> Adding the feature to support conjured Good - Remove support of Python2.7

## Commands

### Requirements

- Python 3.8
- Poetry ^1.1.7
- Make ^4.2.1 (Lesser versions may work too) 

This project is configured with Poetry and you can run its commands via `poetry` CLI or the `make` commands

The following commands are available when using Makefile:

```sh
# Install dependencies for development environment
make setup/dev

#Install dependencies for production environment
make setup/prd

# Run the tests
test/run

# Format the files
format/run
```
