# search-orchestration-demo

## How to Use

### consumer.py
```shell
python3 consumer.py --jenkins_url=http://192.168.1.7:8080/ \
  --jenkins_username=nota --jenkins_password=xxxxxxxx \
  --target_job_name=Handle_Search_Action --queue_name=hello \
  --message_server_host=192.168.1.7 --message_server_user=nota_modelsearch \
  --message_server_pass=dev180928
```
### sender.py
```shell
python3 sender.py --message_server_host=192.168.1.7 \
  --message_server_user=nota_modelsearch --message_server_pass=xxxxxxxx
```