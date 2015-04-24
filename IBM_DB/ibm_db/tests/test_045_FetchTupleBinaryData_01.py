#
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import ibm_db
import config
from testfunctions import IbmDbTestFunctions

class IbmDbTestCase(unittest.TestCase):

  def test_045_FetchTupleBinaryData_01(self):
    obj = IbmDbTestFunctions()
    obj.assert_expect(self.run_test_045)
    
  def run_test_045(self):
    conn = ibm_db.connect(config.database, config.user, config.password)
    fp = open("tests/pic1_out.jpg", "wb")
    result = ibm_db.exec_immediate(conn, "SELECT picture FROM animal_pics WHERE name = 'Helmut'")
    row = ibm_db.fetch_tuple(result)
    if row:
      fp.write(row[0])
    else:
      print(ibm_db.stmt_errormsg())
    fp.close()
    cmp = (open('tests/pic1_out.jpg', 'rb').read() == open('tests/pic1.jpg', 'rb').read())
    print('Are the files the same: ' + str(cmp))


#__END__
#__LUW_EXPECTED__
#Are the files the same: True
#__ZOS_EXPECTED__
#Are the files the same: True
#__SYSTEMI_EXPECTED__
#Are the files the same: True
#__IDS_EXPECTED__
#Are the files the same: True
