# FinTechauthon2022
Predcition of partition's bus voltage based on FATE 
- case1~3.py &nbsp; 集中式训练模型case1-3
- case4.py	&nbsp;联邦模型case4
- case5.py	&nbsp;联邦模型case5
- case6.py		&nbsp;联邦模型case6
- case7.py		&nbsp;联邦模型case7
- case8.py	&nbsp;联邦模型case8
- case9.py		&nbsp;联邦模型case9
- upload_pqu_6parts.py	&nbsp;上传功率信息和标签数据
- upload_pqu_6parts_2468.py	&nbsp;上传不同比例的样本数据20%，40%，60%，80%
- upload_pqu_6parts_n4train+test.py	&nbsp;上传测试数据
- docker-compose.yaml	&nbsp;单机版FATE的docker启动配置
- FL_data	&nbsp;upload的数据

## FL_data文件夹中：
- case1.csv	&nbsp;case1的训练数据
- case2.csv	&nbsp;case2的训练数据
- case3.csv	&nbsp;case3的训练数据
- n4wl.csv	&nbsp;分区1的训练数据
- n9.csv		&nbsp;分区2的训练数据
- n6.csv		&nbsp;分区3的训练数据
- n8.csv	&nbsp;分区4的训练数据
- ***_80.csv	&nbsp;训练数据80%
- ***_60.csv	&nbsp;训练数据60%
- ***_40.csv	&nbsp;训练数据40%
- ***_20.csv	&nbsp;训练数据20%
- n4wl_test.csv	&nbsp;测试数据

## csv文件中：
- p4, q4表示分区1的功率信息
- p9, q9表示分区2的功率信息
- p6, q6表示分区3的功率信息
- p8, q8表示分区4的功率信息
- v4表示分区1的电压信息，也是预测的label
- id表示不同的样本
