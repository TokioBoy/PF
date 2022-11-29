def main( ): 
	# get the date 
	dateStr = input("Enter a date ({0}/{1}/{2}): ".format("mm","dd","yyyy"))
	# split into components 
	monthStr , dayStr , yearStr = dateStr.split( "/" )
	# convert monthStr to the month name 
	months = [" January " , " February " , " March" , "April " , "May" , "June " ,  
                  "July " , "August " , " September ", " October " ,  
                  " November " , "December " ] 
	monthStr = months[int(monthStr) -1]
	# output result in month day , year format    
	print("The converted date is: {0}{1}{2}".format(dayStr, monthStr,yearStr))
	#format(first - day , then month and year)
	#Вначале был порядок: Месяц , день , год , но благодаря формату мы меняем порядок на день , месяц , год
main()
