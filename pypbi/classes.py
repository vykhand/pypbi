from . import constants as const
import logging
log = logging.getLogger()
import requests

class Workspace(object):
    def __init__(self, pbi, wks_id = None, wks_name = "", isReadOnly = False):
        '''
        initializes the Workspace class. requires powerbi object.
        If workspace id is passed as None(default), it assumes default (My Workspace)
        '''
        self._pbi = pbi
        self.wks_id = wks_id
        self.wks_name = wks_name
        self.isReadOnly = isReadOnly
    def __str__(self):
        s = "Workspace ID: %s Name: %s" % (self.wks_id, self.wks_name) \
                                    if self.wks_id is not None \
                                    else "Workspace ID: Default Name: My Workspace"
        return s
    def get_reports(self):
        pass
    def get_datasets(self):
        if self.wks_id is None:
            datasets = self._pbi.request(const.DATASET_LIST_DEFAULT)
        else:
            datasets = self._pbi.request(const.DATASET_LIST % self.wks_id)
        for ds in datasets:
            yield(Dataset(self,  ds_id = ds["id"], ds_name = ds["name"], details = ds))
    def get_dataset_by_id(self, ds_id):
        if self.wks_id is None:
            dataset = self._pbi.request(const.DATASET_BY_ID_DEFAULT % ds_id)
        else:
            dataset = self._pbi.request(const.DATASET_BY_ID % (self.wks_id, ds_id))

        return Dataset(self,  ds_id = dataset["id"],
                        ds_name = dataset["name"], details = dataset)

class Dataset(object):
    def __init__(self, wks, ds_id, ds_name = None, details = None):
        '''
        Constructs a dataset. If only the ID has been passed, retrieve the dataset
        '''
        if  details is None or ds_name is None:
            self = wks.get_dataset_by_id(ds_id)
            return self
        self._pbi = wks._pbi
        self._wks = wks
        self.ds_id = ds_id
        self.ds_name = ds_name
        self.details = details

    def __str__(self):
        return "Dataset ID: %s Name: %s" % (self.ds_id, self.ds_name)

    def get_tables(self):
        if "addRowsAPIEnabled" not in self.details:
            raise RuntimeError("cannot get the addRowsAPIEnabled property")
        if not self.details["addRowsAPIEnabled"]:
            log.warning("Non-push datasets do not support table API")
            return None

        wks_id = self._wks.wks_id
        if wks_id is None:
            tables = self._pbi.request(const.TABLES_LIST_DEFAULT % self.ds_id)
        else:
            tables = self._pbi.request(const.TABLES_LIST % (wks_id, self.ds_id))
        for t in tables:
            yield Table(self, t["name"])

class Table(object):
    def __init__(self, ds, tbl_name):
        self._pbi = ds._wks._pbi
        self._ds = ds
        self._wks = ds._wks
        self.tbl_name = tbl_name
        self._is_def_workspace = self._wks.wks_id is None

    def delete_rows(self):
        headers = {"Authorization": "Bearer " + self._pbi._aad_token}

        if self._is_def_workspace:
            req = const.TABLE_DELETE_ROWS_DEFAULT % (self._ds.ds_id, self.tbl_name)
        else:
            req = const.TABLE_DELETE_ROWS % (self._wks.wks_id, self._ds.ds_id, self.tbl_name)

        response = requests.delete(req, headers=headers)