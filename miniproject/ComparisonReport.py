import difflib
first_file="\\Users\\Rajni\\Desktop\\Python\\imageto text\\img2box.txt"
second_file="\\Users\\Rajni\\Desktop\\Python\\imageto text\\img2txt.txt"
first_file_lines=open(first_file).readlines()
second_file_lines=open(second_file).readlines()
difference=difflib.HtmlDiff().make_file(first_file_lines,second_file_lines,first_file,second_file)
difference_report=open('\\Users\\Rajni\\Desktop\\Python\\imageto text\\difference_report.html','w')
difference_report.write(difference)
difference_report.close()

#\\Users\\Rajni\\Desktop\\Python\\imageto text\\img2box.txt