# NOTE: This repo is not ready for production use

# python std lib
import logging
import os

log = logging.getLogger(__name__)


def _error(ret, err_msg):
    ret['result'] = False
    ret['comment'] = err_msg
    return ret


def _path(hkey, path, key):
    return "%s\\%s\\%s" % (hkey, path, key)


def managed(name, hkey, path, key, value):
    """
    foo:
      winreg.managed:
        - hkey: HKEY_LOCAL_MACHINE
        - path: SOFTWARE\\Salt
        - key: version
        - value: '54321'
    """
    ret = {"name": name,
           "changes": {},
           "result": None,
           "comment" :None}

    exists = __salt__["reg.read_key"](hkey, path, key)

    if not exists:
        if __opts__['test']:
            ret['result'] = None
            ret['comment'] = "Created missing key: {0} and set value: {1}".format(_path(hkey, path, key), value)
        else:
            __salt__["reg.create_key"](hkey, path, key, value)
            # must also set the key to ensure it exists proper, dunno why
            __salt__["reg.set_key"](hkey, path, key, value)

            ret["result"] = True
            ret["comment"] = "Created missing key: {0} and set value: {1}".format(_path(hkey, path, key), value)
            ret["changes"]["new"] = name
    else:
        if __opts__['test']:
            ret["result"] = None
            ret["comment"] = "Set key: {0} to value: {1}".format(_path(hkey, path, key), value)
        else:
            __salt__["reg.set_key"](hkey, path, key, value)
            ret["result"] = True
            ret["comment"] = "Set key: {0} to value: {1}".format(_path(hkey, path, key), value)
            ret["changes"]["updated"] = name

    return ret


def absent(name, hkey, path, key):
    """
    bar:
      winreg.absent:
        - hkey: HKEY_LOCAL_MACHINE
        - path: SOFTWARE\\Salt
        - key: version
    """
    # TOOD: Implement support for  ##  if __opts__['test']:
    ret = {"name": name,
           "changes": {},
           "result": None,
           "comment": None}

    exists = __salt__["reg.read_key"](hkey, path, key)
    if exists:
        __salt__["reg.delete_key"](hkey, path, key)

        # safty check: try to verify that the key was removed proper
        present = __salt__["reg.read_key"](hkey, path, key)
        if not present:
            ret["result"] = True
            ret["comment"] = "Removed key: {0} from registry".format(_path(hkey, path, key))
            ret["changes"]["removed"] = name
        else:
            return _error(ret, "failed to could not remove key: {0} from the system".format(_path(hkey, path, key)))
    else:
        # Key allready not present
        ret["result"] = True
        ret["comment"] = "Key: %s do not exists" % _path(hkey, path, key)

    return ret


def exists(name, hkey, path, key):
    """
    foobar:
      winreg.exists:
        - hkey: HKEY_LOCAL_MACHINE
        - path: SOFTWARE\\Salt
        - key: version
    """
    # TOOD: Implement support for  ##  if __opts__['test']:
    ret = {"name": name,
           "changes": {},
           "result": None,
           "comment": None}

    exists = __salt__["reg.read_key"](hkey, path, key)
    if exists:
        ret["result"] = True
        ret["comment"] = "Key: %s exists on the system" % _path(hkey, path, key)
    else:
        ret["result"] = False
        ret["comment"] = "Could not find key: %s on the system" % _path(hkey, path, key)

    return ret




# if __name__ == "__main__":
#     try:
#         import _winreg
#         HAS_WINDOWS_MODULES = True
#     except ImportError:
#         try:
#             import winreg as _winreg
#             HAS_WINDOWS_MODULES = True
#         except ImportError:
#             HAS_WINDOWS_MODULES = False

#     class Registry(object):
#         '''
#         Delay '_winreg' usage until this module is used
#         '''
#         def __init__(self):
#             self.hkeys = {
#                 "HKEY_USERS":         _winreg.HKEY_USERS,
#                 "HKEY_CURRENT_USER":  _winreg.HKEY_CURRENT_USER,
#                 "HKEY_LOCAL_MACHINE": _winreg.HKEY_LOCAL_MACHINE,
#             }
#         def __getattr__(self, k):
#             try:
#                 return self.hkeys[k]
#             except KeyError:
#                 msg = 'No hkey named \'{0}. Try one of {1}\''
#                 hkeys = ', '.join(self.hkeys)
#                 raise Exception(msg.format(k, hkeys))

#     def read_key(hkey, path, key):
#         print("reg.read_key")
#         registry = Registry()
#         hkey2 = getattr(registry, hkey)
#         fullpath = '\\\\'.join([path, key])
#         try:
#             handle = _winreg.OpenKey(hkey2, fullpath, 0, _winreg.KEY_READ)
#             return _winreg.QueryValueEx(handle, key)[0]
#         except Exception:
#             return False


#     def set_key(hkey, path, key, value):
#         print("reg.set_key")
#         registry = Registry()
#         hkey2 = getattr(registry, hkey)
#         fullpath = '\\\\'.join([path, key])

#         try:
#             handle = _winreg.OpenKey(hkey2, fullpath, 0, _winreg.KEY_ALL_ACCESS)
#             _winreg.SetValueEx(handle, key, 0, _winreg.REG_SZ, value)
#             _winreg.CloseKey(handle)
#             return True
#         except Exception:
#             handle = _winreg.CreateKey(hkey2, fullpath)
#             _winreg.SetValueEx(handle, key, 0, _winreg.REG_SZ, value)
#             _winreg.CloseKey(handle)
#         return True


#     def create_key(hkey, path, key, value=None):
#         print("reg.create_key")
#         registry = Registry()
#         hkey2 = getattr(registry, hkey)
#         fullpath = '\\\\'.join([path, key])

#         try:
#             handle = _winreg.OpenKey(hkey2, fullpath, 0, _winreg.KEY_ALL_ACCESS)
#             _winreg.CloseKey(handle)
#             return True
#         except Exception:
#             handle = _winreg.CreateKey(hkey2, fullpath)
#             if value:
#                 _winreg.SetValueEx(handle, key, 0, _winreg.REG_SZ, value)
#             _winreg.CloseKey(handle)
#         return True


#     def delete_key(hkey, path, key):
#         print("reg.delete_key")
#         registry = Registry()
#         hkey2 = getattr(registry, hkey)

#         try:
#             handle = _winreg.OpenKey(hkey2, path, 0, _winreg.KEY_ALL_ACCESS)
#             _winreg.DeleteKeyEx(handle, key)
#             _winreg.CloseKey(handle)
#             return True
#         except Exception:
#             _winreg.CloseKey(handle)
#         return True


#     __salt__ = {"reg.read_key": read_key, "reg.create_key": create_key, "reg.set_key": set_key, "reg.delete_key": delete_key}
    
#     print(managed("foobar", "HKEY_LOCAL_MACHINE", "SOFTWARE\\Salt", "version", "12345"))
#     print("")
#     print(exists("foobar", "HKEY_LOCAL_MACHINE", "SOFTWARE\\Salt", "version"))
#     print("")
#     print(absent("foobar", "HKEY_LOCAL_MACHINE", "SOFTWARE\\Salt", "version"))
#     print("")
#     print(exists("foobar", "HKEY_LOCAL_MACHINE", "SOFTWARE\\Salt", "version"))
#     print("")
