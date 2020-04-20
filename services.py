from git import Repo
import yaml
import sys, getopt
from jinja2 import Environment, FileSystemLoader
import sys, getopt

def load_config(configfile):
	print("Reading config file", configfile)
	with open(configfile) as yaml_file:
	    config = yaml.safe_load(yaml_file)
	return config
	    
def git_clone(remote_url,local_path):
	git_url = remote_url
	repo_dir = local_path + "/source"
	Repo.clone_from(git_url, repo_dir)
	print("Cloned repo", git_url , "to location" ,repo_dir)

def load_fn_config(config):
	env = Environment(loader=FileSystemLoader('./templates'), trim_blocks=True, lstrip_blocks=True)
	
	template = env.get_template('./func.yaml')
	conf_content = template.render(fn_name=config["name"],fn_runtime=config["runtime"])
	filename = config["name"] + "/func.yaml"
	with open(filename,"w") as fh:
		fh.write(conf_content)
		print("Created", filename)

	template = env.get_template('./requirements.txt')
	conf_content = template.render()
	filename = config["name"] + "/requirements.txt"
	with open(filename,"w") as fh:
		fh.write(conf_content)
		print("Created", filename)

	template = env.get_template('./func.py')
	conf_content = template.render(module=config["invoke"]["module"],function=config["invoke"]["function"],parameters=config["invoke"]["parameters"]["name"])
	filename = config["name"] + "/func.py"
	with open(filename,"w") as fh:
		fh.write(conf_content)
		print("Created", filename)

	template = env.get_template('./Dockerfile')
	conf_content = template.render(basepath=config["invoke"]["basepath"])
	filename = config["name"] + "/Dockerfile"
	with open(filename,"w") as fh:
		fh.write(conf_content)
		print("Created", filename)




def main(argv):
   configfile = ''
   try:
      opts, args = getopt.getopt(argv,"c:",["configfile="])
   except getopt.GetoptError:
      print('services.py -c <configfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-c':
         configfile=arg
   config = load_config(configfile)
   git_clone(config['repo']['remote'],config['repo']['local'])
   load_fn_config(config)

if __name__ == "__main__":
   main(sys.argv[1:])

