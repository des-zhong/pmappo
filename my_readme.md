主要需要编写的地方：envs/env_core.py

results文件夹中保存运行结果

runner文件夹中为训练和运行的代码，separated为分离参数，shared为共享参数

训练：直接运行train文件夹中train脚本即可

测试（可视化）运行test文件夹中test脚本，需指定模型位置，如：

```
python test/test.py --model_dir='./results/Bipedal/run1/models'
```

