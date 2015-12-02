import sys
import os
import re
import logging
import pysam

#
# Class definitions
#
class annotator:


    def __init__(self, tabix_db, header, num_output_column):
        self.tabix_db = tabix_db
        self.header = header
        self.num_output_column = int(num_output_column)


    def annotate(self, in_mutation_file, output):
    
        tb = pysam.TabixFile(self.tabix_db)

        # tabix open
        srcfile = open(in_mutation_file,'r')
        hResult = open(output,'w')

        if self.header:
            header = srcfile.readline().rstrip('\n')  
            header_array = self.header.split(',')
            newheader = "\t".join(map(str,header_array))
            print >> hResult, (header +"\t"+ newheader)
         
        ori_result = ""
        for num in range(self.num_output_column):
            ori_result = ori_result + "---\t"
        ori_result = ori_result[:-1]


        for line in srcfile:
            line = line.rstrip()
            itemlist = line.split('\t')

            # input file is annovar format (not zero-based number)
            chr = itemlist[0]
            start = (int(itemlist[1]) - 1)
            end = int(itemlist[2])
            ref = itemlist[3]
            alt = itemlist[4]

            chridx = chr.find('chr')
            if chridx < 0:
                chr = 'chr' + str(chr)

            # tabix databese is a zero-based number 
            result = ori_result
            try:
                records = tb.fetch(chr, start, end)
                for record_line in records:
                    record = record_line.split('\t')
                    ref_db = record[3]
                    alt_db = record[4]

                    if ref == ref_db and alt == alt_db:
                        result = record[5].replace(";","\t")

            except ValueError:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                logging.error( ("{0}: {1}:{2}".format( exc_type, fname, exc_tb.tb_lineno) ) )
                print >> hResult, (line + "\t" + result)
                continue
          
            ####
            print >> hResult, (line + "\t" +result)

        ####
        hResult.close()
        srcfile.close()
        tb.close()


