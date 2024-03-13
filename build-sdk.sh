#!/bin/bash
python3 -m pip install openapi-python-client;
version=$(yq '.info.version' open-api-spec.yml);
rm -rf ./guardrails-api-client;
openapi-python-client generate --config ./config.json --path ./open-api-spec.yml --meta setup;