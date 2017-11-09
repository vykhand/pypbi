PBI_AUTHORITY =  "https://login.microsoftonline.com/common"
PBI_RESOURCE = "https://analysis.windows.net/powerbi/api"

#API strings
API_BASE = "https://api.powerbi.com/v1.0/myorg/"
API_BASE_GROUP = API_BASE + "groups/%(wks_id)/"
GROUPS_LIST = API_BASE + "groups"

DATASET_LIST_DEFAULT = API_BASE + "datasets"
DATASET_LIST = API_BASE + "groups/%(wks_id)/datasets"

DATASET_BY_ID_DEFAULT = API_BASE + "datasets/%(ds_id)"
DATASET_BY_ID = API_BASE_GROUP + "datasets/%(ds_id)"

TABLES_LIST_DEFAULT = API_BASE + "/datasets/%(ds_id)/tables"
TABLES_LIST = API_BASE_GROUP + "datasets/%(ds_id)/tables"
