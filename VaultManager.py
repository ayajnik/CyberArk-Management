__author__="Ayush Yajnik"

from api.cyberArkManager import cyberark
from argsparser.argsparser import get_run_args
from constants.runargs import Args
import sys

sys.path.append('..')

class cyberArkVault:
    
    def __init__(self) -> None:
        self.cybark_dict = {"hostname":get_run_args(Args.CYBERARK_HOST.value), "appId": get_run_args(Args.APPID.value), "safe": get_run_args(Args.SAFE.value),"object":get_run_args(Args.CA_OBJECT.value),"username":get_run_args(Args.CYBERARK_USERNAME.value)}

    def get_password(self):
        cyber_ark = cyberark(self.cybark_dict)
        pswddata = cyber_ark.execute_request()
        return pswddata['Content']
    
    def creationMethod(self):
        cyber_ark = cyberark(self.cybark_dict)
        creation_method = cyber_ark.execute_request()
        return creation_method['CreationMethod']
    
    def get_Address(self):
        cyber_ark = cyberark(self.cybark_dict)
        getAddr = cyber_ark.execute_request()
        return getAddr['Address']
    
    def get_Safe(self):
        cyber_ark = cyberark(self.cybark_dict)
        getSafe = cyber_ark.execute_request()
        return getSafe['Safe']
    
    def get_Owner(self):
        cyber_ark = cyberark(self.cybark_dict)
        getOwner = cyber_ark.execute_request()
        return getOwner['OwnerName']
    
    def get_UserName(self):
        cyber_ark = cyberark(self.cybark_dict)
        getUsrName = cyber_ark.execute_request()
        return getUsrName['UserName']
    
    def get_Object(self):
        cyber_ark = cyberark(self.cybark_dict)
        getObj = cyber_ark.execute_request()
        return getObj['Name']
    
    def is_password_changeInProgress(self):
        cyber_ark = cyberark(self.cybark_dict)
        get_password_change_status = cyber_ark.execute_request()
        status = get_password_change_status['PasswordChangeInProcess']
        message = "Password for this user is currently being changed: "+str(status)
        return message
    