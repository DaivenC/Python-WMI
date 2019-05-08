from win32com.client import GetObject

#VBS Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\WMI")
objWMIService = GetObject('winmgmts:/root/WMI')

#VBS Set objShare = objWMIService.Get("EasiCPU.InstanceName='ACPI\PNP0C14\0x0_0'")
EasiCPU = objWMIService.InstancesOf('EasiCPU')

for Object in EasiCPU:
    print("EasiCPU")
    print(" InstanceName:",  Object.Properties_('InstanceName'))
    print(" Active:", Object.Properties_('Active'))

def SetCPUMaxSpeed(Value):
    print('SetCPUMaxSpeed(',Value, ')')
    for Object in EasiCPU:
        objInParam = Object.Methods_('SetCPUMaxSpeed').InParameters.SpawnInstance_()
        objInParam.Properties_.Item("uStatus").Value = Value
        OutParams = Object.ExecMethod_('SetCPUMaxSpeed', objInParam )
        print("  Result :",OutParams.Result)

def GetCPUDTS():
    print("GetCPUDTS()")
    for Object in EasiCPU :
        OutParams = Object.ExecMethod_('GetCPUDTS')
        print ("  Result :", OutParams.Result)

def enum_namespace(name):
    try:
        wmi = GetObject('winmgmts:/' + name)
        namespaces = wmi.InstancesOf('__Namespace')
        for namespace in namespaces:
            enum_namespace('{name}/{subname}'.format(name=name,
                                                     subname=namespace.Name))
    except pywintypes.com_error:
        print(name, 'limit of authority')
    else:
        print(name)

GetCPUDTS()
SetCPUMaxSpeed(100)
#enum_namespace('root/WMI')