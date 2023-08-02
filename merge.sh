#!/bin/bash
echo "merging files"
yq eval-all '. as $item ireduce ({}; . * $item )' ./service-specs/*.yml > open-api-spec.yml

echo "consolidating info"
yq eval-all --inplace 'select(fileIndex==0).info = select(fileIndex==1).info | select(fileIndex==0)' ./open-api-spec.yml ./service-specs/guardrails-service-spec.yml
