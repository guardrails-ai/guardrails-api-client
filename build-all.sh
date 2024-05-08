#!/bin/bash

npm run openapi-gen || exit 1;

bash ./ts-build.sh || exit 1;

bash ./py-build.sh  || exit 1;