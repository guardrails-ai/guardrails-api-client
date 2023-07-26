#!/bin/bash
merged=$(yq ea '. as $item ireduce ({}; . * $item )' ./service-specs/*.yml)
yq -P <<< $merged > open-api-spec.yml
consolidated=$(yq eval-all 'select(fileIndex==0).info = select(fileIndex==1).info | select(fileIndex==0)'  ./open-api-spec.yml ./service-specs/guardrails-service-spec.yml)
yq -P <<< $consolidated > open-api-spec.yml
