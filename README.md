This repository has four parts: `app`, `GitHub workflow` `IAC`, and `k8s_cluster`.

<br>

`APP:`<br>
This is a flask web application. A dockerfile exists in this repository to dockerise the flask application.<br>
The application is divided into two microservices: Flask microservice and Postgres microservice. Each can be seen in `k8s_cluster`.
To run the app locally with the configurations for postgres on localhost (and without the S3 bucket configurations):
```
python3 app.py
```
<br>


`GITHUB WORKFLOW:`<br>
This automatically pushes any changes made to DockerHub. Although the Docker file is only for `app`, this is a project work; thereby all the other folders like `IAC` and `k8s_cluster` are inlcuded in this repository.

<br>


`IAC:`<br>
This part contains Terraform configuration files to provision `route 53`, `S3 bucket`, and a `dynamoDB` on AWS cloud.<br>
To run the Terraform file:
```
Terraform init
Terraform plan
Terraform apply
```

<br>

`K8S_CLUSTER:`<br>
This contains the deployment, service, and ingress configurations for the two microservices.<br>
It also contains YAML files for the `AWS cluster` creation. and a `Makefile` to run the commands.<br>
To test the microservices locally, run:
```
kubectl port-forward services/inspire-service :80
```
To run the `Makefile` commands, run `make command` e.g:
```
make deploy_application
```
