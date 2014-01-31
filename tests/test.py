#!/usr/bin/python
'''
* ApplySettings workflow, zistit cez Features ci sa zmeny aplikovali
* WipeDevice workflow, zistit cez Features ci to prebehlo
* LoadDevice workflow, zistit cez Features ci to prebehlo
* ResetDevice workflow

- zrejme v sucinnosti s inymi testami
  * ButtonRequest/ButtonAck workflow (vyvolat napr. pomocou GetEntropy, myslim ze ten GetEntropy vyzaduje PIN, ale ja by som to dal na button)
  * PinMatrixRequest/PinMatrixAck workflow (vyvolat napr. pomocou ChangePin)
  * PassphraseRequest/PassphraseAck workflow (vyvolat napr. pomocou GetAddress)

* rozsirit test_sign.tx o viac transakcii (zlozitejsich)

- chceme v tomto release(?)
  * SignMessage workflow
  * VerifyMessage workflow

* otestovat session handling (tento test bude zrejme failovat na RPi)
'''


'''
import sys
sys.path = ['../',] + sys.path

import time

ENABLE_DEBUG_LINK = True

from bitkeylib.transport_pipe import PipeTransport
from bitkeylib.transport_serial import SerialTransport
from bitkeylib.transport_fake import FakeTransport
from bitkeylib import proto

from bitkeylib.client import BitkeyClient
from bitkeylib.debuglink import DebugLink

transport = PipeTransport('../../bitkey-python/device.socket', is_device=False)

if ENABLE_DEBUG_LINK:
    debug_transport = PipeTransport('../../bitkey-python/device.socket.debug', is_device=False)
    debuglink = DebugLink(debug_transport)
else:
    debuglink = None

bitkey = BitkeyClient(transport, debuglink)

print bitkey.call(proto.Initialize())
#bitkey.call(proto.Ping(message='ahoj!'))
#bitkey.call(proto.GetUUID())

print bitkey.call(proto.GetEntropy(size=10), button=True)
bitkey.call(proto.SetMaxFeeKb(maxfee_kb=100000), button=True, pin_correct=False)
'''

'''
d = PipeTransport('../bitkey-python/device.socket', is_device=False)
#d = SerialTransport('../../bitkey-python/COM9')

#start = time.time()

#for x in range(1000):

call(proto.Initialize())
call(proto.Ping())
call(proto.GetUUID())
#call(proto.GetEntropy(size=10))
#call(proto.LoadDevice(seed='beyond neighbor scratch swirl embarrass doll cause also stick softly physical nice',
#                      otp=True, pin='1234', spv=True))

#call(proto.ResetDevice())
call(proto.GetMasterPublicKey(algo=proto.ELECTRUM))
#call(proto.ResetDevice())
''' 

#print 10000 / (time.time() - start)
