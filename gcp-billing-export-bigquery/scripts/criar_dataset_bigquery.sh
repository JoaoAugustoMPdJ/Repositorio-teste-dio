#!/bin/bash

# Script auxiliar para criar um dataset no BigQuery.
# A ativação da exportação de Billing deve ser feita no Console GCP em:
# Billing > Billing export > BigQuery export.

PROJECT_ID="SEU_PROJECT_ID"
DATASET_ID="billing_export"
LOCATION="US"

gcloud config set project "$PROJECT_ID"

bq --location="$LOCATION" mk   --dataset   --description "Dataset para exportacao do Cloud Billing"   "$PROJECT_ID:$DATASET_ID"
