"""
  Function:  updateChEMBL 
  --------------------
 
housekeeping pipeline to automatically update the tables pfam_domains and tools
when a new version of ChEMBL is available.
The old version of ChEMBL is dropped and the new uploaded.This script needs to 
be run as sudo ... the path o the directory should be given like ~/Desktop/chembl_06_mysql

momo.sander@googlemail.com
"""                                                  

def updateChEMBL(release, user, pword, host, port): 
  import os
  import sys
   
  os.system("wget ftp://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_%s/chembl_%s_mysql.tar.gz" %(release, release))
  os.system("tar -zxvf chembl_%s_mysql.tar.gz" % release)
  os.system("mysqladmin -u%s -p%s -h%s -P%s create chembl_%s" %(user, pword, host, port, release))    
  os.system("mysql -u%s -p%s -h%s -P%s chembl_%s < chembl_%s_mysql/chembl_%s.mysqldump.sql" % ( user, pword, host, port, release, release, release))

                                  	                                                     
if __name__ == '__main__':
  import sys                                        
  import os
  if len(sys.argv) != 6:                  
    print "specify path, release, user, pword, host, port"
    sys.exit()                                                                             
                                        
  release = str(sys.argv[1])
  user = str(sys.argv[2])
  pword = str(sys.argv[3])
  host = str(sys.argv[4])
  port = str(sys.argv[5])

  updateChEMBL(release, user, pword, host, port)

                                             
