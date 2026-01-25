 # Connect to gcp using ADC (identity verification)
 provider "google" {
   project = var.project
   region  = var.region
   zone    = var.zone
 }

 /* add these data blocks */
 
 # This data source gets a temporary token for the service account
 data "google_service_account_access_token" "default" {
   provider               = google
   target_service_account = "datalynn@project-023ecffe-f3f7-44d2-b1e.iam.gserviceaccount.com"
   scopes                 = ["https://www.googleapis.com/auth/cloud-platform"]
   lifetime               = "3600s"
 }
 
 # This second provider block uses that temporary token and does the real work
 provider "google" {
   alias        = "impersonated"
   access_token = data.google_service_account_access_token.default.access_token
   project      = var.project
   region       = var.region
   zone         = var.zone
 }
