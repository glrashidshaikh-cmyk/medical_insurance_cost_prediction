from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv("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"))
api.upload_folder(
    folder_path="week_2_practice/deployment",     # the local folder containing your files
    repo_id="glrashidshaikh-cmyk/medical-insurance-cost-prediction",          # the target repo
    repo_type="space",                      # dataset, model, or space
    path_in_repo="",                          # optional: subfolder path inside the repo
)
