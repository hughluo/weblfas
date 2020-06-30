# weblfas

## Requirement
Python3
requests 

## Steps
* 更改 `weblfas.py` 中的 `appid` 和 `secret_key` （210行）
```
    api = RequestApi(appid="你的appid", secret_key="你的secret_key", upload_file_path=r"./target.mp3")
```
* 下载MP3文件 重命名为`target.mp3`并将其置于和`weblfas.py`同一目录下
* `python3 weblfas.py`
* 等待完成后，transcript 会创建并保存在 同一目录的`result.json`中
* `python3 parser.py`
* 等待完成后，transcript.csv 会创建并保存在 同一目录的`transcript.csv`中 （可以用excel打开）
