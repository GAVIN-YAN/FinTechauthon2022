import json

from pipeline.backend.pipeline import PipeLine
from pipeline.component import DataTransform
from pipeline.component import HeteroSecureBoost
from pipeline.component import Intersection
from pipeline.component import Reader
from pipeline.interface import Data
from pipeline.component import Evaluation
from pipeline.interface import Model

guest = 20000
hosts = [20001, 20002, 20003]

# data sets
guest_n4 = {"name": "n4wl_40", "namespace": "experiment"}
host_n9 = {"name": "n9", "namespace": "experiment"}
host_n6 = {"name": "n6", "namespace": "experiment"}
host_n8 = {"name": "n8", "namespace": "experiment"}


guest_validate_n4 = {"name": "n4wl_test", "namespace": "experiment"}
host_validate_n9 = {"name": "n9", "namespace": "experiment"}
host_validate_n6 = {"name": "n6", "namespace": "experiment"}
host_validate_n8 = {"name": "n8", "namespace": "experiment"}


# init pipeline
pipeline = PipeLine().set_initiator(role="guest", party_id=guest).set_roles(guest=guest, host=hosts)

# set data reader and data-io
reader_0, reader_1 = Reader(name="reader_0"), Reader(name="reader_1")
reader_0.get_party_instance(role="guest", party_id=guest).component_param(table=guest_n4)
reader_0.get_party_instance(role="host", party_id=hosts[0]).component_param(table=host_n9)
reader_0.get_party_instance(role="host", party_id=hosts[1]).component_param(table=host_n6)
reader_0.get_party_instance(role="host", party_id=hosts[2]).component_param(table=host_n8)


reader_1.get_party_instance(role="guest", party_id=guest).component_param(table=guest_validate_n4)
reader_1.get_party_instance(role="host", party_id=hosts[0]).component_param(table=host_n9)
reader_1.get_party_instance(role="host", party_id=hosts[1]).component_param(table=host_n6)
reader_1.get_party_instance(role="host", party_id=hosts[2]).component_param(table=host_n8)


data_transform_0, data_transform_1 = DataTransform(name="data_transform_0"), DataTransform(name="data_transform_1")


data_transform_0.get_party_instance(role="guest", party_id=guest).component_param(
    with_label=True,
    output_format="dense",
    label_name='v4',
    label_type="float64")
data_transform_0.get_party_instance(role="host", party_id=hosts[0]).component_param(with_label=False)
data_transform_0.get_party_instance(role="host", party_id=hosts[1]).component_param(with_label=False)
data_transform_0.get_party_instance(role="host", party_id=hosts[2]).component_param(with_label=False)


data_transform_1.get_party_instance(role="guest", party_id=guest).component_param(
    with_label=True,
    output_format="dense",
    label_name='v4',
    label_type="float64")
data_transform_1.get_party_instance(role="host", party_id=hosts[0]).component_param(with_label=False)
data_transform_1.get_party_instance(role="host", party_id=hosts[1]).component_param(with_label=False)
data_transform_1.get_party_instance(role="host", party_id=hosts[2]).component_param(with_label=False)


# data intersect component
intersect_0 = Intersection(name="intersection_0")
intersect_1 = Intersection(name="intersection_1")

# secure boost component
# https://fate.readthedocs.io/en/latest/zh/federatedml_component/ensemble/#federatedml.param.boosting_param.HeteroSecureBoostParam
hetero_secure_boost_0 = HeteroSecureBoost(name="hetero_secure_boost_0",
                                          num_trees=1000,  # max number of trees to build
                                          learning_rate=0.3,  # default: 0.3
                                          task_type="regression",
                                          objective_param={"objective": "lse"},
                                          encrypt_param={"method": "Paillier"},
                                          tree_param={"max_depth": 5,
                                                      "criterion_params": [0.4, 0],  # L2, L1
#                                                      'min_impurity_split': 0.001,
                                                      },

                                          validation_freqs=1,
                                          # cv_param={
                                          #     "need_cv": True,
                                          #     "n_splits": 5,
                                          #     "shuffle": True,
                                          #     "random_seed": 103
                                          # },
                                          
subsample_feature_rate=1,
                                          early_stopping_rounds=10,
                                          n_iter_no_change=True,
                                          tol=0.000000001,  # True and <tol, tree building process will stop
                                          use_first_metric_only=False,
                                          # bin_num=50,
                                          # metrics=['root_mean_squared_error', 'mean_absolute_error'],
                                          # feature_importance_type='split',  # split or gain
                                          )

# evaluation component
evaluation_0 = Evaluation(name="evaluation_0", eval_type="regression")

pipeline.add_component(reader_0)
pipeline.add_component(reader_1)
pipeline.add_component(data_transform_0, data=Data(data=reader_0.output.data))
pipeline.add_component(data_transform_1, data=Data(data=reader_1.output.data),
                       model=Model(data_transform_0.output.model))                  # 这一行有什么用？？？
pipeline.add_component(intersect_0, data=Data(data=data_transform_0.output.data))
pipeline.add_component(intersect_1, data=Data(data=data_transform_1.output.data))
pipeline.add_component(hetero_secure_boost_0, data=Data(train_data=intersect_0.output.data,
                                                        validate_data=intersect_1.output.data))
pipeline.add_component(evaluation_0, data=Data(data=hetero_secure_boost_0.output.data))

pipeline.compile()
pipeline.fit()

print("fitting hetero secure boost done, result:")
# print(pipeline.get_component("hetero_secure_boost_0").get_summary())
print(f"hetero_secure_boost_0:\n{json.dumps(pipeline.get_component('hetero_secure_boost_0').get_summary(), indent=4)}")

print(f"Evaluation summary:\n{json.dumps(pipeline.get_component('evaluation_0').get_summary(), indent=4)}")
