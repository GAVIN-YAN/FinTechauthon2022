from pipeline.backend.pipeline import PipeLine
import os

data_base = "/home/yanfeng/fate"
guest = 20000
pipeline_upload = PipeLine().set_initiator(role='guest', party_id=guest).set_roles(guest=guest)
partition = 4

n4wl_20 = {"name": "n4wl_20", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n4wl_20.csv",
                                table_name=n4wl_20["name"],
                                namespace=n4wl_20["namespace"],
                                head=1, partition=partition)
n5_20 = {"name": "n5_20", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n5_20.csv",
                                table_name=n5_20["name"],  # table name
                                namespace=n5_20["namespace"],  # namespace
                                head=1, partition=partition)  # data info
n6_20 = {"name": "n6_20", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n6_20.csv",
                                table_name=n6_20["name"],  # table name
                                namespace=n6_20["namespace"],  # namespace
                                head=1, partition=partition)  # data info
n7_20 = {"name": "n7_20", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n7_20.csv",
                                table_name=n7_20["name"],  # table name
                                namespace=n7_20["namespace"],  # namespace
                                head=1, partition=partition)  # data info
n8_20 = {"name": "n8_20", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n8_20.csv",
                                table_name=n8_20["name"],  # table name
                                namespace=n8_20["namespace"],  # namespace
                                head=1, partition=partition)  # data info
n9_20 = {"name": "n9_20", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n9_20.csv",
                                table_name=n9_20["name"],  # table name
                                namespace=n9_20["namespace"],  # namespace
                                head=1, partition=partition)  # data info

################################
n4wl_40 = {"name": "n4wl_40", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n4wl_40.csv",
                                table_name=n4wl_40["name"],
                                namespace=n4wl_40["namespace"],
                                head=1, partition=partition)
n5_40 = {"name": "n5_40", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n5_40.csv",
                                table_name=n5_40["name"],  # table name
                                namespace=n5_40["namespace"],  # namespace
                                head=1, partition=partition)  # data info
n6_40 = {"name": "n6_40", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n6_40.csv",
                                table_name=n6_40["name"],  # table name
                                namespace=n6_40["namespace"],  # namespace
                                head=1, partition=partition)  # data info
n7_40 = {"name": "n7_40", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n7_40.csv",
                                table_name=n7_40["name"],  # table name
                                namespace=n7_40["namespace"],  # namespace
                                head=1, partition=partition)  # data info
n8_40 = {"name": "n8_40", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n8_40.csv",
                                table_name=n8_40["name"],  # table name
                                namespace=n8_40["namespace"],  # namespace
                                head=1, partition=partition)  # data info
n9_40 = {"name": "n9_40", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n9_40.csv",
                                table_name=n9_40["name"],  # table name
                                namespace=n9_40["namespace"],  # namespace
                                head=1, partition=partition)  # data info

###############################
n4wl_60 = {"name": "n4wl_60", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n4wl_60.csv",
                                table_name=n4wl_60["name"],
                                namespace=n4wl_60["namespace"],
                                head=1, partition=partition)
n5_60 = {"name": "n5_60", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n5_60.csv",
                                table_name=n5_60["name"],  # table name
                                namespace=n5_60["namespace"],  # namespace
                                head=1, partition=partition)  # data info
n6_60 = {"name": "n6_60", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n6_60.csv",
                                table_name=n6_60["name"],  # table name
                                namespace=n6_60["namespace"],  # namespace
                                head=1, partition=partition)  # data info
n7_60 = {"name": "n7_60", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n7_60.csv",
                                table_name=n7_60["name"],  # table name
                                namespace=n7_60["namespace"],  # namespace
                                head=1, partition=partition)  # data info
n8_60 = {"name": "n8_60", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n8_60.csv",
                                table_name=n8_60["name"],  # table name
                                namespace=n8_60["namespace"],  # namespace
                                head=1, partition=partition)  # data info
n9_60 = {"name": "n9_60", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n9_60.csv",
                                table_name=n9_60["name"],  # table name
                                namespace=n9_60["namespace"],  # namespace
                                head=1, partition=partition)  # data info


###############################
n4wl_80 = {"name": "n4wl_80", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n4wl_80.csv",
                                table_name=n4wl_80["name"],
                                namespace=n4wl_80["namespace"],
                                head=1, partition=partition)
n5_80 = {"name": "n5_80", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n5_80.csv",
                                table_name=n5_80["name"],  # table name
                                namespace=n5_80["namespace"],  # namespace
                                head=1, partition=partition)  # data info
n6_80 = {"name": "n6_80", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n6_80.csv",
                                table_name=n6_80["name"],  # table name
                                namespace=n6_80["namespace"],  # namespace
                                head=1, partition=partition)  # data info
n7_80 = {"name": "n7_80", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n7_80.csv",
                                table_name=n7_80["name"],  # table name
                                namespace=n7_80["namespace"],  # namespace
                                head=1, partition=partition)  # data info
n8_80 = {"name": "n8_80", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n8_80.csv",
                                table_name=n8_80["name"],  # table name
                                namespace=n8_80["namespace"],  # namespace
                                head=1, partition=partition)  # data info
n9_80 = {"name": "n9_80", "namespace": "experiment"}
pipeline_upload.add_upload_data(file=data_base + "/FL_data/n9_80.csv",
                                table_name=n9_80["name"],  # table name
                                namespace=n9_80["namespace"],  # namespace
                                head=1, partition=partition)  # data info

pipeline_upload.upload(drop=1)
