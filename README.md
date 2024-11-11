# ftwd_datatalk
数据分析小工具 [WIP]

```shell
ftwd_datatalk assets --excel your/excel/file.xlsx --output c:/output
```

## 年度分析
```shell
ftwd_datatalk annual --excel your/excel/数据分析报告-1.xlsx --excel your/excel/数据分析报告-2.xlsx --output c:/output
```


## 开发环境设置
```shell
pip install -r requirements-dev.txt
```

### 构建exe
```shell
nox -s build-exe
```
