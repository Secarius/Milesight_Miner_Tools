from paramiko import SSHClient, AutoAddPolicy

class ssh_comms():
    def __init__(self):
        try:
            self.ssh = SSHClient()
            self.ssh.set_missing_host_key_policy(AutoAddPolicy())
        except:
            return None

    def set_config(self, addr=None, user=None, port=22, password=None):
        args = [addr, user, int(port), password]
        if all([arg != None for arg in args]):
            self.addr, self.user, self.port, self.password = args

    def connect(self):
        try:
            self.ssh.connect(self.addr,port=self.port, username=self.user, password=self.password)
            return 'Connected'
        except Exception as connecter:
            print(connecter)
            return connecter

    def disconnect(self):
        try:
            self.ssh.close()
        except:
            print('Error disconnecting')

    def exec_cmd(self, cmd=None):
        try:
            if cmd is not None:
                stdin, stdout, stderr = self.ssh.exec_command(cmd)
                return [stdout.read().decode(), stderr.read().decode()]
        except:
            print('Error on command')

    def scp_file(self, path=None):
        if path is not None:
            sftp = self.ssh.open_sftp()
            sftp.get(path, "processlogs/logs/console.log")
            sftp.close()

    def is_alive(self):
        if self.ssh.get_transport() is not None:
            return self.ssh.get_transport().is_active()
