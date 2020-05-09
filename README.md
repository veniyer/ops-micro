# Ops-Micro - Serverless Containerized Microservices

Ops-Micro is (visioned to be) an end-to-end onboarding and operating platform for serverless, containerized microservices.

## Getting started

Install ops-micro and start its servers using the following

```curl https://raw.githubusercontent.com/veniyer/ops-micro/master/install/install.sh | sh```

Define a service in the <service-name>.yaml. The contents of the file are
```  
# name of the microservice
name: foo
# remote repo and local clone location
repo:
  remote: https://github.com/veniyer/python-samples.git
  local: foo
# runtime for the microservice. Default is python v3.6
runtime: python 
# how to invoke the microservice
invoke:
  # basepath of the python function within the source code repo
  basepath: hello-fn
  # if a module has to be included to call this python function
  module: hello
  # name of the function
  function: hellofn
  # parameter(s) for the function. Needs to be modified to be a list
  parameters: 
    name: name
    type: string
```

Then create a service using the following command

```
python3 services.py -c service.yaml
```
where ```service.yaml``` is the service definition file as specified above

Deploy service using the following command

```
./service-deploy.sh ./foo fooapp foofn
```

### Hardware

Ops-Micro will work seamlessly across your data centers and Cloud Providers.

### Software

So far, it has been tested with 

```
CentOS 7
python3
fn 0.5.96
Docker 19.03.8
```

It is intended in future to work for your codebase in

```
Go
Java
Node.js
Ruby
```

## Built With

* [Docker](http://www.docker.com) - For the containerized environment
* [fn](https://fnproject.io/) - For the serverless environment
* [Ansible](https://www.ansible.com) - For configuration management

## Contributing

For contributing, feel free to fork or branch and submit pull requests.

## Versioning

This is version 0.1 of the software.

## Authors

* **Ven Iyer** - *Initial work* - [Ops-Micro](https://github.com/veniyer/ops-micro)

See also the list of [contributors](https://github.com/veniyer/ops-micro/contributors) who participated in this project.

## License

This project is licensed under the <pending> - see the [LICENSE.md](LICENSE.md) file for details. Whichever license is adopted, the code will be free and open-source.

## Acknowledgments

* Docker
* fn
* Ansible
* python
* jinja2
