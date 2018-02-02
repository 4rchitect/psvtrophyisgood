import os
os.getcwd()
def decryptPFS(path):
    print "Decrypting "+ path
    print "Executing: "+os.path.dirname(os.path.realpath(__file__))+'/psvpfsparser --title_id_src="'+path+'" --title_id_dst="'+path+'_decrypted" --f00d_url=cma.henkaku.xyz'
    os.system(os.path.dirname(os.path.realpath(__file__))+'/psvpfsparser --title_id_src="'+path+'" --title_id_dst="'+path+'_decrypted" --f00d_url=cma.henkaku.xyz')
