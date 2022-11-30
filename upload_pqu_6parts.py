from pipeline.backend.pipeline import PipeLine
import os

data_base = "/home/yanfeng/fate"
guest = 20000
pipeline_upload = PipeLine().set_initiator(role='guest', party_id=guest).set_roles(guest=guest)
partition = 4


n4wl = {"name": "n4wl", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n4wl.csv",
                                table_name=n4wl["name"],
                                namespace=n4wl["namespace"],
                                head=1, partition=partition)

n5 = {"name": "n5", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n5.csv",
                                table_name=n5["name"],  # table name
                                namespace=n5["namespace"],  # namespace
                                head=1, partition=partition)  # data info

n6 = {"name": "n6", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n6.csv",
                                table_name=n6["name"],  # table name
                                namespace=n6["namespace"],  # namespace
                                head=1, partition=partition)  # data info

n7 = {"name": "n7", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n7.csv",
                                table_name=n7["name"],  # table name
                                namespace=n7["namespace"],  # namespace
                                head=1, partition=partition)  # data info

n8 = {"name": "n8", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n8.csv",
                                table_name=n8["name"],  # table name
                                namespace=n8["namespace"],  # namespace
                                head=1, partition=partition)  # data info

n9 = {"name": "n9", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n9.csv",
                                table_name=n9["name"],  # table name
                                namespace=n9["namespace"],  # namespace
                                head=1, partition=partition)  # data info

pipeline_upload.upload(drop=1)
