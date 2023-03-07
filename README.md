This repository has four parts: `app`, `GitHub workflow` `IAC`, and `k8s_cluster`.


`APP:`

This is a flask web application. A dockerfile exists in this repository to dockerise the flask application.

The application is divided into two microservices: Flask microservice and Postgres microservice. Each can be seen in `k8s_cluster`.
To run the app locally with the configurations for postgres on localhost (and without the S3 bucket configurations):
```
python3 app.py
```

![Home](app/static/imgs/Readme/Home.png)
![Login](app/static/imgs/Readme/Login.png)
![Home Details](app/static/imgs/Readme/Home_details.png)
![Admin Page Details](app/static/imgs/Readme/Details.png)

`GITHUB WORKFLOW:`

This automatically pushes any changes made to DockerHub. Although the Docker file is only for `app`, this is a project work; thereby all the other folders like `IAC` and `k8s_cluster` are inlcuded in this repository.



`IAC:`

This part contains Terraform configuration files to provision `route 53`, `S3 bucket`, and a `dynamoDB` on AWS cloud.


![Route 53](app/static/imgs/Readme/TF.png)

To run the Terraform file:
```
Terraform init
Terraform plan
Terraform apply
```

![Route 53](app/static/imgs/Readme/TF_R53.png)


`K8S_CLUSTER:`

This contains the deployment, service, and ingress configurations for the two microservices.

It also contains YAML files for the `AWS cluster` creation. and a `Makefile` to run the commands.

To see all the Kubernetes configuration, run:
```
kubectl get all
```

![Kubernetes configuration](app/static/imgs/Readme/K8s.png)

To test the microservices locally, run:
```
kubectl port-forward services/inspire-service :80
```
To run the `Makefile` commands, run `make command` e.g:
```
make deploy_application
```

Here is the application running successfully:

![Admin](app/static/imgs/Readme/admin.png)
![Application](app/static/imgs/Readme/Final_Home.png)
![Application Home](app/static/imgs/Readme/Final_H_Details.png)
![About](app/static/imgs/Readme/About.png)