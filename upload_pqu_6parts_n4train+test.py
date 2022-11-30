from pipeline.backend.pipeline import PipeLine
import os

data_base = "/home/yanfeng/fate"
guest = 20000
pipeline_upload = PipeLine().set_initiator(role='guest', party_id=guest).set_roles(guest=guest)
partition = 4


n4wltrain = {"name": "n4wl_train", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n4wl_train.csv",
                                table_name=n4wltrain["name"],
                                namespace=n4wltrain["namespace"],
                                head=1, partition=partition)

n4wltest = {"name": "n4wl_test", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n4wl_test.csv",
                                table_name=n4wltest["name"],  # table name
                                namespace=n4wltest["namespace"],  # namespace
                                head=1, partition=partition)  # data info



pipeline_upload.upload(drop=1)
