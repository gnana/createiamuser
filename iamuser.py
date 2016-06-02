import boto3
import yaml
from password import GeneratePassword

client = boto3.client('iam')
iam = boto3.resource('iam')

class IAMUser(object):

    def __init__(self, username, role=None, password_only=False,
                accesskey_only=False):
        self.username = username
        self.role = role
        self.password_only = password_only
        self.accesskey_only = accesskey_only
        self.password = None
        self.accesskey = None
        self.secretkey = None
        self.groups = []

    def createuser(self):
        if not self.checkuserexists():
            try:
                response = client.create_user(UserName=self.username)
            except Exception, e:
                print ("%s - Error creating user" % (self.username))
                raise
            if (self.password_only or (not self.password_only and not self.accesskey_only)):
                self.password = self.setpassword()
            if (self.accesskey_only or (not self.password_only and not self.accesskey_only)):
                self.accesskey, self.secretkey = self.setsecretkey()
            if self.role:
                self.setrole()
            return True
        else:
            print ("%s: User already exists" % (self.username))
            print ("%s: Skipping user" % (self.username))
            return False

    def setrole(self):
        try:
            with open('roles.yml', 'r') as f:
                roles = yaml.load(f)
        except Exception as e:
            raise
        if roles:
            try:
                groups = roles[self.role]
            except Exception, e:
                print ("Cannot find role - %s" % (self.role))
                raise
        if groups:
            for group in groups:
                try:
                    response = client.add_user_to_group(GroupName=group,UserName=self.username)
                    self.groups.append(group)
                except Exception, e:
                    print ("%s: Error adding user to group - %s" % (self.username, group))
                    print ("%s: Skipping group - %s" % (self.username, group))
        return

    def checkuserexists(self):
        try:
            response = client.get_user(UserName=self.username)
        except Exception, e:
            return False
        if response:
            username = response['User']['UserName']
            if username == self.username:
                return True
        else:
            return False

    def setpassword(self):
        password = GeneratePassword.getpassword(12)
        login_profile = iam.LoginProfile(self.username)
        try:
            login_profile = login_profile.create(Password=password,PasswordResetRequired=True)
        except Exception, e:
            raise
        return password

    def setsecretkey(self):
        try:
            response = client.create_access_key(UserName=self.username)
        except Exception, e:
            print ("%s: Error creating AccessKey" % (self.username))
            raise
        if response:
            return response['AccessKey']['AccessKeyId'], response['AccessKey']['SecretAccessKey']
