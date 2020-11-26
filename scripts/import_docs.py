import os

class Importer(object):
    docs = ['dreq2Defn.xml',  'dreq2Sample.xml',  'dreqSuppDefn.xml',  'dreqSupp.xml',  'dreq.xml']
    docs_xsd = ['dc1.xsd',  'dreq2Schema.xsd',  'dreqSuppSchema.xsd',  'pav.xsd',  'xlink.xsd',   'xml.xsd']

    def __init__(self,idir='/data/svn/exarch/CMIP6dreq/tags', odir='./Documents'):
        assert os.path.isdir(idir), '%s not found' % idir
        self.idir = idir
        assert os.path.isdir(odir), '%s not found' % odir
        self.odir = odir

    def pull(self,version):
        sdir = '%s/%s' % (self.idir,version)
        assert os.path.isdir( sdir ), '%s not found' % sdir
        sdir += '/dreqPy/docs'
        assert os.path.isdir( sdir ), '%s not found' % sdir
        srcs = ['%s/%s' % (sdir,x) for x in (self.docs + self.docs_xsd)]
        assert all( [os.path.isfile(x) for x in srcs] ), 'Source files missing in %s' % sdir
        for s in srcs:
            os.popen( 'cp %s %s' % (s,self.odir ) )


if __name__ == "__main__":
    import sys
    version = sys.argv[1]
    imp = Importer()
    imp.pull(version)
