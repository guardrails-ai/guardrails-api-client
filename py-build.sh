#!/bin/bash

# Generate Typescript models
npm run py-gen;

# Remove previous build artifacts
rm -rf ./resources/py/guardrails_api_client;
rm -rf ./resources/py/.venv;
rm -rf ./resources/py/docs;

# Create target directory for Typescript models
mkdir -p ./resources/py/guardrails_api_client;
mkdir -p ./resources/py/docs;

# Copy Python models to target directory
cp -r ./build/py/guardrails_api_client/* ./resources/py/guardrails_api_client;
cp -r ./build/py/docs/* ./resources/py/docs;
cp -r ./build/py/.gitignore ./resources/py;
cp -r ./build/py/requirements.txt ./resources/py;
cp -r ./build/openapi-spec.json ./resources/py/guardrails_api_client;

# Navigate to Python directory
cd ./resources/py;

# Build the Python library
node ./scripts/prebuild.js;
rm -rf ./.venv;

python3 -m venv ./.venv;
source ./.venv/bin/activate && \
    echo "$(which pip)" && \
    make install-dev && \
    make lint-fix


# Navigate back to root
cd ../..;


