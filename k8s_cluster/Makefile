#Some of the code can be found here:
# https://aws.amazon.com/blogs/opensource/kubernetes-ingress-aws-alb-ingress-controller/ 
# https://docs.aws.amazon.com/eks/latest/userguide/alb-ingress.html
# https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html

create_cluster:
	eksctl create cluster -f cluster.yaml

delete_cluster:
	eksctl delete cluster -f cluster.yaml

aws_identity:
	aws sts get-caller-identity

set_context:
	eksctl utils write-kubeconfig --cluster=inspire-cluster --set-kubeconfig-context=true

enable_iam_sa_provider:
	eksctl utils associate-iam-oidc-provider --cluster=inspire-cluster --approve

create_cluster_role:
	kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/aws-alb-ingress-controller/v1.1.4/docs/examples/rbac-role.yaml

create_iam_policy:
	curl -o iam_policy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.2.0/docs/install/iam_policy.json
	aws iam create-policy \
		--policy-name AWSLoadBalancerControllerIAMPolicy \
		--policy-document file://iam_policy.json

create_service_account:
	eksctl create iamserviceaccount \
      --cluster=inspire-cluster \
      --namespace=kube-system \
      --name=aws-load-balancer-controller \
      --attach-policy-arn=arn:aws:iam::428253719401:policy/AWSLoadBalancerControllerIAMPolicy \
      --override-existing-serviceaccounts \
      --approve

deploy_cert_manager:
	kubectl apply \
		--validate=false \
		-f https://github.com/jetstack/cert-manager/releases/download/v1.5.4/cert-manager.yaml

#nil
#apply_cert_manager_manifest:
#	kubectl apply \
#		--validate=false \
#		-f ./cert-manager.yaml

deploy_ingress_controller:
	kubectl apply -f v2_4_4_full.yaml

apply_ingress_class:
	kubectl apply -f v2_4_4_ingclass.yaml

deploy_application:
	kustomize build ./k8s | kubectl apply -f -

delete_application:
	kustomize build ./k8s | kubectl delete -f -
