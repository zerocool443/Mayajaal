import shodan
import sys
key="**************" #Put you key here
api=shodan.Shodan(key);

if __name__ == '__main__':
	try:
		q=sys.argv[1];
		print "Scanning .........."
		results = api.search(q);
		print 'Results Found : '
		print len(results['matches'])
		for result in results['matches']:

			print """
                IP: %s
                HOSTNAME: %s
                OS: %s
                PORT: %s

        			""" % (result['ip_str'], result['hostnames'],result['os'],result['port'])
		fname=str(q)+"_results"
		ff=open(fname,'w')
		ff.write(results['matches'])

	except shodan.APIError, e:
		print 'Error: %s' % e
else:
	q=raw_input("Please provide me your query   ");
	try:
		results = api.search(q);
		print 'Results Found : '
		print len(results['matches'])
		for result in results['matches']:

			print """
                IP: %s
                HOSTNAME: %s
                OS: %s
                PORT: %s

        		""" % (result['ip_str'], result['hostnames'],result['os'],result['port'])

	except shodan.APIError, e:
			print 'Error: %s' % e


