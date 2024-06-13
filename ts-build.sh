#!/bin/bash

# Generate Typescript models
npm run ts-gen;

# Remove previous build artifacts
rm -rf ./resources/ts/src;
rm -rf ./resources/ts/index;
rm -rf ./resources/ts/runtime;
rm -rf ./resources/ts/dist;
rm -rf ./resources/ts/node_modules;
rm -rf ./resources/ts/docs;

# Create target directory for Typescript models
mkdir -p ./resources/ts/src;

# Copy Typescript models to target directory
cp -r ./build/ts/src/apis ./resources/ts/src;
cp -r ./build/ts/src/models ./resources/ts/src;
cp -r ./build/ts/src/index.ts ./resources/ts/src;
cp -r ./build/ts/src/runtime.ts ./resources/ts/src;
cp -r ./build/openapi-spec.json ./resources/ts;

# Navigate to Typescript directory
cd ./resources/ts;

# Install Dependencies
npm ci;

# Apply Fixes and Replacements
npm run prebuild;

# Run QA w/ Auto-Fixes
npm run qa;

# Build the Typescript library
npm run compile;

# Rebuild the Docs
npm run docs

# Navigate back to root
cd ../..;


