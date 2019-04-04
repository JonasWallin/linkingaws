import boto3


class LinkingHandler(object):
	"""
		Class for setting up amazon cluster

	"""

	def __init__(self):
		"""

		"""

		self.ec2      = boto3.resource('ec2')
		self.ids 	  = []
		self.instance = None



	def __del__(self):
		"""
			closing down, terminating the instances
		"""
		if self.instance is not None:
			for instance in self.instances:
				self.ec2.instances.filter(InstanceIds = instace.id).stop()
				self.ec2.instances.filter(InstanceIds = instace.id).terminate()

	def create_instance(self, ImageID, InstanceType):
		"""
			ImageId - ami-image-id

		"""

		self.instances = self.ec2.create_instances(ImageId=ImageID, 
					   			  				   MinCount=1, 
											 	   MaxCount=1,
											 	   InstanceType = InstanceType)

	def load_instance(self):
		"""
			load a previously started instance
		"""

		pass